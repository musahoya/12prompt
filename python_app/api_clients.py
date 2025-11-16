"""
AI API 클라이언트 모듈
"""

import requests
import json


class AIClient:
    """AI API 클라이언트 기본 클래스"""

    def __init__(self, api_key):
        self.api_key = api_key

    def generate(self, prompt):
        """프롬프트를 AI에게 전송하고 응답 받기"""
        raise NotImplementedError


class OpenAIClient(AIClient):
    """OpenAI (ChatGPT) API 클라이언트"""

    def __init__(self, api_key):
        super().__init__(api_key)
        self.url = "https://api.openai.com/v1/chat/completions"
        self.model = "gpt-4o"

    def generate(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        payload = {
            "model": self.model,
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 4000,
            "temperature": 0.7
        }

        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            raise Exception(f"OpenAI API 오류: {str(e)}")
        except (KeyError, IndexError) as e:
            raise Exception(f"응답 파싱 오류: {str(e)}")


class AnthropicClient(AIClient):
    """Anthropic (Claude) API 클라이언트"""

    def __init__(self, api_key):
        super().__init__(api_key)
        self.url = "https://api.anthropic.com/v1/messages"
        self.model = "claude-3-5-sonnet-20241022"

    def generate(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01"
        }

        payload = {
            "model": self.model,
            "max_tokens": 4000,
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data['content'][0]['text']
        except requests.exceptions.RequestException as e:
            raise Exception(f"Claude API 오류: {str(e)}")
        except (KeyError, IndexError) as e:
            raise Exception(f"응답 파싱 오류: {str(e)}")


class GeminiClient(AIClient):
    """Google (Gemini) API 클라이언트"""

    def __init__(self, api_key):
        super().__init__(api_key)
        self.model = "gemini-2.0-flash-exp"
        self.url = f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent?key={api_key}"

    def generate(self, prompt):
        headers = {
            "Content-Type": "application/json"
        }

        payload = {
            "contents": [
                {"parts": [{"text": prompt}]}
            ],
            "generationConfig": {
                "temperature": 0.7,
                "maxOutputTokens": 4000
            }
        }

        try:
            response = requests.post(self.url, headers=headers, json=payload, timeout=60)
            response.raise_for_status()
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']
        except requests.exceptions.RequestException as e:
            raise Exception(f"Gemini API 오류: {str(e)}")
        except (KeyError, IndexError) as e:
            raise Exception(f"응답 파싱 오류: {str(e)}")


def get_client(model_name, api_key):
    """모델 이름으로 적절한 클라이언트 반환"""
    clients = {
        'gpt': OpenAIClient,
        'chatgpt': OpenAIClient,
        'openai': OpenAIClient,
        'claude': AnthropicClient,
        'anthropic': AnthropicClient,
        'gemini': GeminiClient,
        'google': GeminiClient
    }

    client_class = clients.get(model_name.lower())
    if not client_class:
        raise ValueError(f"지원하지 않는 모델: {model_name}")

    return client_class(api_key)
