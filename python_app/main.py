#!/usr/bin/env python3
"""
12가지 프롬프트 기법 셀렉터 - Python CLI 버전
"""

import sys
from datetime import datetime

from techniques import list_techniques, get_technique
from api_clients import get_client
from config import Config
from utils import (
    clear_screen, print_header, print_section, print_success,
    print_error, print_warning, print_info, get_input,
    get_multiline_input, save_result, confirm, select_from_list,
    print_result, format_difficulty
)


class PromptSelector:
    """프롬프트 셀렉터 메인 애플리케이션"""

    def __init__(self):
        self.config = Config()
        self.selected_model = None
        self.selected_technique = None
        self.api_key = None
        self.client = None

    def run(self):
        """메인 실행"""
        clear_screen()
        print_header()

        # 모델 선택
        if not self.select_model():
            print_info("프로그램을 종료합니다.")
            return

        # API 키 설정
        if not self.setup_api_key():
            print_error("API 키 설정에 실패했습니다.")
            return

        # 메인 루프
        while True:
            # 프롬프트 기법 선택
            if not self.select_technique():
                if not confirm("프로그램을 종료하시겠습니까?"):
                    continue
                break

            # 입력값 수집
            inputs = self.collect_inputs()
            if not inputs:
                continue

            # 프롬프트 생성
            prompt = self.selected_technique.generate_prompt(inputs)

            # 프롬프트 확인
            if not self.confirm_prompt(prompt):
                continue

            # AI에게 전송
            result = self.generate_response(prompt)
            if not result:
                continue

            # 결과 출력
            print_result(result, truncate=True)

            # 결과 저장
            if confirm("결과를 파일로 저장하시겠습니까?"):
                try:
                    filepath = save_result(
                        result,
                        self.selected_technique.name,
                        self.selected_model
                    )
                    print_success(f"저장 완료: {filepath}")
                except Exception as e:
                    print_error(f"저장 실패: {e}")

            # 히스토리 저장
            self.save_to_history(prompt, result)

            # 계속할지 확인
            print()
            if not confirm("다른 작업을 계속하시겠습니까?"):
                break

        print()
        print_success("프로그램을 종료합니다. 감사합니다!")

    def select_model(self):
        """AI 모델 선택"""
        models = [
            "🤖 ChatGPT (OpenAI GPT-4o)",
            "🧠 Claude (Anthropic Claude 3.5 Sonnet)",
            "✨ Gemini (Google Gemini 2.0 Flash)"
        ]

        model_keys = ['gpt', 'claude', 'gemini']

        # 마지막 사용 모델 표시
        last_model = self.config.get_last_model()
        if last_model:
            print_info(f"마지막 사용 모델: {last_model}")
            print()

        choice = select_from_list(models, "AI 모델 선택", allow_cancel=True)

        if choice is None:
            return False

        self.selected_model = model_keys[choice]
        self.config.set_last_model(self.selected_model)

        print_success(f"선택: {models[choice]}")
        return True

    def setup_api_key(self):
        """API 키 설정"""
        # 저장된 API 키 확인
        saved_key = self.config.get_api_key(self.selected_model)

        if saved_key:
            print_info(f"저장된 API 키 발견: {saved_key[:10]}...{saved_key[-4:]}")
            if confirm("이 키를 사용하시겠습니까?"):
                self.api_key = saved_key
                return True

        # API 키 입력
        print_section("API 키 입력")
        print()
        self.print_api_key_info()
        print()

        api_key = get_input("API 키를 입력하세요").strip()

        if not api_key:
            print_error("API 키가 필요합니다.")
            return False

        self.api_key = api_key

        # API 키 저장 여부
        if confirm("이 API 키를 저장하시겠습니까?"):
            self.config.set_api_key(self.selected_model, api_key)
            print_success("API 키가 저장되었습니다.")

        return True

    def print_api_key_info(self):
        """API 키 발급 정보 출력"""
        info = {
            'gpt': "https://platform.openai.com/api-keys",
            'claude': "https://console.anthropic.com/settings/keys",
            'gemini': "https://ai.google.dev/gemini-api/docs/api-key"
        }

        url = info.get(self.selected_model)
        if url:
            print_info(f"API 키 발급: {url}")

    def select_technique(self):
        """프롬프트 기법 선택"""
        techniques = list_techniques()
        technique_list = []

        print_section("프롬프트 기법 선택")
        print()

        # 난이도별 그룹화
        easy = []
        medium = []
        hard = []

        for key, tech in techniques.items():
            if tech.difficulty == 'easy':
                easy.append((key, tech))
            elif tech.difficulty == 'medium':
                medium.append((key, tech))
            else:
                hard.append((key, tech))

        # 출력
        if easy:
            print("🟢 쉬운 난이도:")
            for key, tech in easy:
                print(f"  • {tech.name} - {tech.description}")
                technique_list.append((key, tech))
            print()

        if medium:
            print("🟡 보통 난이도:")
            for key, tech in medium:
                print(f"  • {tech.name} - {tech.description}")
                technique_list.append((key, tech))
            print()

        if hard:
            print("🔴 어려운 난이도:")
            for key, tech in hard:
                print(f"  • {tech.name} - {tech.description}")
                technique_list.append((key, tech))
            print()

        # 선택
        options = [f"{tech.name} - {tech.description}" for _, tech in technique_list]
        choice = select_from_list(options, "기법 선택", allow_cancel=True)

        if choice is None:
            return False

        technique_key, technique = technique_list[choice]
        self.selected_technique = technique

        print_success(f"선택: {technique.name}")
        return True

    def collect_inputs(self):
        """입력값 수집"""
        print_section(f"{self.selected_technique.name} - 정보 입력")
        print()

        inputs = {}

        for field in self.selected_technique.fields:
            field_id = field['id']
            label = field['label']
            field_type = field['type']

            print(f"📝 {label}")

            if field_type == 'textarea':
                value = get_multiline_input("")
            else:
                value = get_input("").strip()

            if not value and '선택' not in label:
                print_warning("값이 입력되지 않았습니다.")
                if not confirm("계속하시겠습니까?"):
                    return None

            inputs[field_id] = value
            print()

        return inputs

    def confirm_prompt(self, prompt):
        """프롬프트 확인"""
        print_section("생성된 프롬프트 확인")
        print()

        # 프롬프트 미리보기 (처음 500자만)
        preview = prompt[:500]
        if len(prompt) > 500:
            preview += "\n... (생략)"

        print(preview)
        print()

        if not confirm("이 프롬프트를 AI에게 전송하시겠습니까?"):
            return False

        return True

    def generate_response(self, prompt):
        """AI 응답 생성"""
        print()
        print_info("AI가 응답을 생성하고 있습니다... (최대 60초 소요)")
        print()

        try:
            # 클라이언트 생성
            if not self.client:
                self.client = get_client(self.selected_model, self.api_key)

            # AI 호출
            result = self.client.generate(prompt)

            print_success("응답 생성 완료!")
            return result

        except Exception as e:
            print_error(f"오류 발생: {e}")
            return None

    def save_to_history(self, prompt, result):
        """히스토리에 저장"""
        try:
            entry = {
                'timestamp': datetime.now().isoformat(),
                'model': self.selected_model,
                'technique': self.selected_technique.name,
                'prompt': prompt[:500],  # 처음 500자만
                'result': result[:500]   # 처음 500자만
            }
            self.config.save_to_history(entry)
        except Exception as e:
            print_warning(f"히스토리 저장 실패: {e}")


def main():
    """메인 함수"""
    try:
        app = PromptSelector()
        app.run()
    except KeyboardInterrupt:
        print("\n\n프로그램을 종료합니다.")
        sys.exit(0)
    except Exception as e:
        print_error(f"예상치 못한 오류: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
