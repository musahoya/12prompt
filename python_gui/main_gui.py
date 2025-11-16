#!/usr/bin/env python3
"""
12가지 프롬프트 기법 셀렉터 - Python GUI 버전
PyWebView를 사용한 데스크톱 애플리케이션
"""

import webview
import sys
import os
from pathlib import Path

# 상위 디렉토리의 모듈 임포트를 위해 경로 추가
sys.path.insert(0, str(Path(__file__).parent.parent / 'python_app'))

from techniques import list_techniques, get_technique
from api_clients import get_client
from config import Config


class API:
    """JavaScript와 Python 간 통신을 위한 API 클래스"""

    def __init__(self):
        self.config = Config()
        self.client = None

    def get_techniques_list(self):
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

        return result

    def get_saved_api_key(self, model_name):
        """저장된 API 키 가져오기"""
        api_key = self.config.get_api_key(model_name)
        if api_key:
            # 보안을 위해 일부만 반환
            return f"{api_key[:10]}...{api_key[-4:]}"
        return None

    def save_api_key(self, model_name, api_key):
        """API 키 저장"""
        try:
            self.config.set_api_key(model_name, api_key)
            return {'success': True, 'message': 'API 키가 저장되었습니다.'}
        except Exception as e:
            return {'success': False, 'message': f'저장 실패: {str(e)}'}

    def get_last_model(self):
        """마지막 사용 모델 가져오기"""
        return self.config.get_last_model()

    def set_last_model(self, model_name):
        """마지막 사용 모델 저장"""
        self.config.set_last_model(model_name)

    def generate_prompt(self, technique_id, inputs):
        """프롬프트 생성"""
        try:
            technique = get_technique(technique_id)
            if not technique:
                return {'success': False, 'message': '기법을 찾을 수 없습니다.'}

            prompt = technique.generate_prompt(inputs)
            return {'success': True, 'prompt': prompt}
        except Exception as e:
            return {'success': False, 'message': f'프롬프트 생성 실패: {str(e)}'}

    def generate_response(self, model_name, api_key, prompt):
        """AI 응답 생성"""
        try:
            # 클라이언트 생성
            self.client = get_client(model_name, api_key)

            # AI 호출
            result = self.client.generate(prompt)

            # 히스토리 저장
            self._save_to_history(model_name, prompt[:500], result[:500])

            return {'success': True, 'result': result}
        except Exception as e:
            return {'success': False, 'message': f'오류: {str(e)}'}

    def _save_to_history(self, model, prompt, result):
        """히스토리 저장"""
        try:
            from datetime import datetime
            entry = {
                'timestamp': datetime.now().isoformat(),
                'model': model,
                'prompt': prompt,
                'result': result
            }
            self.config.save_to_history(entry)
        except Exception:
            pass  # 히스토리 저장 실패는 무시

    def get_history(self, limit=10):
        """히스토리 가져오기"""
        try:
            history = self.config.load_history()
            return history[-limit:] if len(history) > limit else history
        except Exception:
            return []

    def get_full_api_key(self, model_name):
        """전체 API 키 가져오기 (실제 사용용)"""
        return self.config.get_api_key(model_name)


def main():
    """메인 실행 함수"""
    # API 인스턴스 생성
    api = API()

    # HTML 파일 경로
    html_file = Path(__file__).parent / 'gui.html'

    if not html_file.exists():
        print(f"❌ 오류: {html_file} 파일을 찾을 수 없습니다.")
        sys.exit(1)

    # 윈도우 생성 및 실행
    window = webview.create_window(
        title='🎯 12가지 프롬프트 기법 셀렉터',
        url=str(html_file),
        js_api=api,
        width=1200,
        height=900,
        resizable=True,
        background_color='#FFFFFF'
    )

    webview.start(debug=True)


if __name__ == '__main__':
    main()
