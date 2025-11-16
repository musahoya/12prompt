"""
유틸리티 함수 모듈
"""

import os
import sys
from datetime import datetime


def clear_screen():
    """화면 지우기"""
    os.system('cls' if os.name == 'nt' else 'clear')


def print_header():
    """헤더 출력"""
    print("=" * 70)
    print("🎯 12가지 프롬프트 기법 셀렉터 (Python CLI)")
    print("=" * 70)
    print()


def print_section(title):
    """섹션 제목 출력"""
    print()
    print("─" * 70)
    print(f"  {title}")
    print("─" * 70)


def print_success(message):
    """성공 메시지 출력"""
    print(f"✅ {message}")


def print_error(message):
    """에러 메시지 출력"""
    print(f"❌ {message}")


def print_warning(message):
    """경고 메시지 출력"""
    print(f"⚠️  {message}")


def print_info(message):
    """정보 메시지 출력"""
    print(f"ℹ️  {message}")


def get_input(prompt, default=None):
    """사용자 입력 받기"""
    if default:
        prompt = f"{prompt} [{default}]: "
    else:
        prompt = f"{prompt}: "

    try:
        value = input(prompt).strip()
        return value if value else default
    except KeyboardInterrupt:
        print("\n\n종료합니다.")
        sys.exit(0)


def get_multiline_input(prompt):
    """여러 줄 입력 받기"""
    print(f"{prompt}")
    print("  (여러 줄 입력 가능, 빈 줄 입력 시 종료)")
    lines = []
    while True:
        try:
            line = input("  > ")
            if not line:
                break
            lines.append(line)
        except KeyboardInterrupt:
            print("\n\n종료합니다.")
            sys.exit(0)

    return "\n".join(lines)


def save_result(content, technique_name, model_name):
    """결과를 파일로 저장"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"result_{technique_name}_{model_name}_{timestamp}.txt"

    # 현재 디렉토리에 results 폴더 생성
    results_dir = "results"
    os.makedirs(results_dir, exist_ok=True)

    filepath = os.path.join(results_dir, filename)

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# 프롬프트 기법: {technique_name}\n")
            f.write(f"# AI 모델: {model_name}\n")
            f.write(f"# 생성 시간: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("\n" + "=" * 70 + "\n\n")
            f.write(content)

        return filepath
    except Exception as e:
        raise Exception(f"파일 저장 실패: {str(e)}")


def confirm(message):
    """확인 메시지"""
    response = get_input(f"{message} (y/n)", "n").lower()
    return response in ['y', 'yes', '예']


def display_menu(options, title="옵션 선택"):
    """메뉴 표시 및 선택"""
    print_section(title)
    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")
    print()


def select_from_list(options, title="옵션 선택", allow_cancel=True):
    """리스트에서 선택"""
    display_menu(options, title)

    if allow_cancel:
        print(f"  0. 취소")
        print()

    while True:
        try:
            choice = get_input("선택")
            if not choice:
                continue

            choice_num = int(choice)

            if allow_cancel and choice_num == 0:
                return None

            if 1 <= choice_num <= len(options):
                return choice_num - 1

            print_error(f"1-{len(options)} 사이의 숫자를 입력하세요.")
        except ValueError:
            print_error("숫자를 입력하세요.")
        except KeyboardInterrupt:
            print("\n\n종료합니다.")
            sys.exit(0)


def print_result(content, truncate=False, max_lines=50):
    """결과 출력"""
    print_section("AI 응답 결과")
    print()

    lines = content.split('\n')

    if truncate and len(lines) > max_lines:
        print('\n'.join(lines[:max_lines]))
        print()
        print(f"... (총 {len(lines)}줄 중 {max_lines}줄만 표시)")
        print()
        print_info("전체 내용을 보려면 파일로 저장하세요.")
    else:
        print(content)

    print()
    print("─" * 70)


def format_difficulty(difficulty):
    """난이도 포맷팅"""
    difficulty_map = {
        'easy': '🟢 쉬움',
        'medium': '🟡 보통',
        'hard': '🔴 어려움'
    }
    return difficulty_map.get(difficulty, difficulty)
