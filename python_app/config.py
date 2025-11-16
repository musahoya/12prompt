"""
설정 관리 모듈
"""

import os
import json
from pathlib import Path


class Config:
    """애플리케이션 설정 관리"""

    def __init__(self):
        self.config_dir = Path.home() / '.12prompt'
        self.config_file = self.config_dir / 'config.json'
        self.history_file = self.config_dir / 'history.json'
        self.ensure_config_dir()

    def ensure_config_dir(self):
        """설정 디렉토리 생성"""
        self.config_dir.mkdir(parents=True, exist_ok=True)

    def load_config(self):
        """설정 파일 로드"""
        if self.config_file.exists():
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}

    def save_config(self, config_data):
        """설정 파일 저장"""
        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(config_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ 설정 저장 실패: {e}")

    def get_api_key(self, model_name):
        """API 키 가져오기 (환경변수 > 설정파일 순)"""
        # 환경변수 확인
        env_keys = {
            'gpt': 'OPENAI_API_KEY',
            'chatgpt': 'OPENAI_API_KEY',
            'openai': 'OPENAI_API_KEY',
            'claude': 'ANTHROPIC_API_KEY',
            'anthropic': 'ANTHROPIC_API_KEY',
            'gemini': 'GEMINI_API_KEY',
            'google': 'GEMINI_API_KEY'
        }

        env_key = env_keys.get(model_name.lower())
        if env_key:
            api_key = os.getenv(env_key)
            if api_key:
                return api_key

        # 설정 파일 확인
        config = self.load_config()
        return config.get('api_keys', {}).get(model_name.lower())

    def set_api_key(self, model_name, api_key):
        """API 키 설정 파일에 저장"""
        config = self.load_config()
        if 'api_keys' not in config:
            config['api_keys'] = {}
        config['api_keys'][model_name.lower()] = api_key
        self.save_config(config)

    def save_to_history(self, entry):
        """히스토리에 저장"""
        history = self.load_history()
        history.append(entry)

        # 최대 100개까지만 보관
        if len(history) > 100:
            history = history[-100:]

        try:
            with open(self.history_file, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ 히스토리 저장 실패: {e}")

    def load_history(self):
        """히스토리 로드"""
        if self.history_file.exists():
            try:
                with open(self.history_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception:
                return []
        return []

    def get_last_model(self):
        """마지막으로 사용한 모델 가져오기"""
        config = self.load_config()
        return config.get('last_model')

    def set_last_model(self, model_name):
        """마지막으로 사용한 모델 저장"""
        config = self.load_config()
        config['last_model'] = model_name
        self.save_config(config)
