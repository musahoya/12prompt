#!/usr/bin/env python3
"""
12가지 프롬프트 기법 셀렉터 - Python Flask GUI 버전
간단한 웹 서버로 브라우저에서 실행되는 GUI 애플리케이션
"""

from flask import Flask, render_template, request, jsonify
import sys
import os
import webbrowser
import threading
from pathlib import Path

# 상위 디렉토리의 모듈 임포트를 위해 경로 추가
sys.path.insert(0, str(Path(__file__).parent.parent / 'python_app'))

from techniques import list_techniques, get_technique
from api_clients import get_client
from config import Config

app = Flask(__name__)
config = Config()


@app.route('/')
def index():
    """메인 페이지"""
    html_file = Path(__file__).parent / 'gui.html'
    if not html_file.exists():
        return "Error: gui.html not found", 404

    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # PyWebView API 호출을 Flask API 호출로 변경
    html_content = html_content.replace(
        'pywebview.api.',
        'flaskAPI.'
    ).replace(
        "window.addEventListener('pywebviewready'",
        "window.addEventListener('DOMContentLoaded'"
    )

    # Flask API JavaScript 추가
    flask_api_script = """
    <script>
    // Flask API wrapper
    const flaskAPI = {
        async get_techniques_list() {
            const response = await fetch('/api/techniques');
            return await response.json();
        },
        async get_saved_api_key(model_name) {
            const response = await fetch(`/api/api_key/${model_name}`);
            const data = await response.json();
            return data.api_key;
        },
        async save_api_key(model_name, api_key) {
            const response = await fetch('/api/api_key', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({model_name, api_key})
            });
            return await response.json();
        },
        async get_last_model() {
            const response = await fetch('/api/last_model');
            const data = await response.json();
            return data.model;
        },
        async set_last_model(model_name) {
            await fetch('/api/last_model', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({model_name})
            });
        },
        async generate_prompt(technique_id, inputs) {
            const response = await fetch('/api/generate_prompt', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({technique_id, inputs})
            });
            return await response.json();
        },
        async generate_response(model_name, api_key, prompt) {
            const response = await fetch('/api/generate', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({model_name, api_key, prompt})
            });
            return await response.json();
        },
        async get_history(limit = 10) {
            const response = await fetch(`/api/history?limit=${limit}`);
            return await response.json();
        },
        async get_full_api_key(model_name) {
            const response = await fetch(`/api/full_api_key/${model_name}`);
            const data = await response.json();
            return data.api_key;
        }
    };
    </script>
    """

    # </head> 태그 바로 앞에 Flask API script 추가
    html_content = html_content.replace('</head>', f'{flask_api_script}\n</head>')

    return html_content


@app.route('/api/techniques')
def get_techniques():
    """모든 프롬프트 기법 목록 반환"""
    techniques = list_techniques()
    result = {}

    for key, tech in techniques.items():
        result[key] = {
            'name': tech.name,
            'description': tech.description,
            'difficulty': tech.difficulty,
            'fields': tech.fields
        }

    return jsonify(result)


@app.route('/api/api_key/<model_name>')
def get_api_key(model_name):
    """저장된 API 키 가져오기"""
    api_key = config.get_api_key(model_name)
    if api_key:
        # 보안을 위해 일부만 반환
        return jsonify({'api_key': f"{api_key[:10]}...{api_key[-4:]}"})
    return jsonify({'api_key': None})


@app.route('/api/full_api_key/<model_name>')
def get_full_api_key(model_name):
    """전체 API 키 가져오기 (실제 사용용)"""
    api_key = config.get_api_key(model_name)
    return jsonify({'api_key': api_key})


@app.route('/api/api_key', methods=['POST'])
def save_api_key():
    """API 키 저장"""
    try:
        data = request.json
        model_name = data.get('model_name')
        api_key = data.get('api_key')

        config.set_api_key(model_name, api_key)
        return jsonify({'success': True, 'message': 'API 키가 저장되었습니다.'})
    except Exception as e:
        return jsonify({'success': False, 'message': f'저장 실패: {str(e)}'})


@app.route('/api/last_model')
def get_last_model():
    """마지막 사용 모델 가져오기"""
    model = config.get_last_model()
    return jsonify({'model': model})


@app.route('/api/last_model', methods=['POST'])
def set_last_model():
    """마지막 사용 모델 저장"""
    data = request.json
    model_name = data.get('model_name')
    config.set_last_model(model_name)
    return jsonify({'success': True})


@app.route('/api/generate_prompt', methods=['POST'])
def generate_prompt():
    """프롬프트 생성"""
    try:
        data = request.json
        technique_id = data.get('technique_id')
        inputs = data.get('inputs')

        technique = get_technique(technique_id)
        if not technique:
            return jsonify({'success': False, 'message': '기법을 찾을 수 없습니다.'})

        prompt = technique.generate_prompt(inputs)
        return jsonify({'success': True, 'prompt': prompt})
    except Exception as e:
        return jsonify({'success': False, 'message': f'프롬프트 생성 실패: {str(e)}'})


@app.route('/api/generate', methods=['POST'])
def generate():
    """AI 응답 생성"""
    try:
        data = request.json
        model_name = data.get('model_name')
        api_key = data.get('api_key')
        prompt = data.get('prompt')

        # 클라이언트 생성
        client = get_client(model_name, api_key)

        # AI 호출
        result = client.generate(prompt)

        # 히스토리 저장
        save_to_history(model_name, prompt[:500], result[:500])

        return jsonify({'success': True, 'result': result})
    except Exception as e:
        return jsonify({'success': False, 'message': f'오류: {str(e)}'})


@app.route('/api/history')
def get_history():
    """히스토리 가져오기"""
    try:
        limit = int(request.args.get('limit', 10))
        history = config.load_history()
        result = history[-limit:] if len(history) > limit else history
        return jsonify(result)
    except Exception:
        return jsonify([])


def save_to_history(model, prompt, result):
    """히스토리 저장"""
    try:
        from datetime import datetime
        entry = {
            'timestamp': datetime.now().isoformat(),
            'model': model,
            'prompt': prompt,
            'result': result
        }
        config.save_to_history(entry)
    except Exception:
        pass  # 히스토리 저장 실패는 무시


def open_browser():
    """브라우저 자동 열기"""
    webbrowser.open('http://127.0.0.1:5000')


def main():
    """메인 실행 함수"""
    print("\n" + "="*60)
    print("🎯 12가지 프롬프트 기법 셀렉터 - Flask GUI 버전")
    print("="*60)
    print("\n브라우저가 자동으로 열립니다...")
    print("수동으로 열려면: http://127.0.0.1:5000")
    print("\n종료하려면 Ctrl+C를 누르세요.\n")

    # 1초 후 브라우저 열기
    threading.Timer(1.0, open_browser).start()

    # Flask 앱 실행
    app.run(host='127.0.0.1', port=5000, debug=False)


if __name__ == '__main__':
    main()
