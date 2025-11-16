"""
12가지 프롬프트 엔지니어링 기법 정의
"""

class PromptTechnique:
    """프롬프트 기법 기본 클래스"""

    def __init__(self, name, description, difficulty, fields):
        self.name = name
        self.description = description
        self.difficulty = difficulty  # 'easy', 'medium', 'hard'
        self.fields = fields  # List of field definitions

    def generate_prompt(self, inputs):
        """입력값을 받아 프롬프트 생성"""
        raise NotImplementedError


class FewShotTechnique(PromptTechnique):
    """Few-Shot 기법"""

    def __init__(self):
        super().__init__(
            name="🎯 Few-Shot 기법",
            description="소수의 예시로 패턴 학습",
            difficulty="medium",
            fields=[
                {"id": "example1_input", "label": "예시 1 - 입력", "type": "text"},
                {"id": "example1_output", "label": "예시 1 - 출력", "type": "text"},
                {"id": "example2_input", "label": "예시 2 - 입력", "type": "text"},
                {"id": "example2_output", "label": "예시 2 - 출력", "type": "text"},
                {"id": "example3_input", "label": "예시 3 - 입력", "type": "text"},
                {"id": "example3_output", "label": "예시 3 - 출력", "type": "text"},
                {"id": "actual_input", "label": "실제 분석할 내용", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""다음 예시들을 참고하여 패턴을 학습하고, 동일한 형식으로 답변해주세요:

예시1:
입력: {inputs['example1_input']}
출력: {inputs['example1_output']}

예시2:
입력: {inputs['example2_input']}
출력: {inputs['example2_output']}

예시3:
입력: {inputs['example3_input']}
출력: {inputs['example3_output']}

이제 다음 내용을 분석해주세요:
입력: {inputs['actual_input']}
출력:"""


class RolePlayingTechnique(PromptTechnique):
    """역할 지정 기법"""

    def __init__(self):
        super().__init__(
            name="👤 역할 지정 기법",
            description="전문가 역할 부여",
            difficulty="easy",
            fields=[
                {"id": "role", "label": "역할 (직업)", "type": "text"},
                {"id": "experience", "label": "경력/자격", "type": "text"},
                {"id": "personality", "label": "성격/태도", "type": "text"},
                {"id": "scope", "label": "업무 범위", "type": "textarea"},
                {"id": "constraints", "label": "제약사항", "type": "textarea"},
                {"id": "question", "label": "질문/작업", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""당신은 {inputs['experience']}의 {inputs['role']}입니다.
성격: {inputs['personality']}

업무 범위:
{inputs['scope']}

제약사항:
{inputs['constraints']}

질문/작업: {inputs['question']}

위 역할과 제약사항을 준수하여 답변해주세요."""


class MarkdownTechnique(PromptTechnique):
    """마크다운 활용 기법"""

    def __init__(self):
        super().__init__(
            name="📝 마크다운 활용 기법",
            description="구조화된 문서 작성",
            difficulty="easy",
            fields=[
                {"id": "title", "label": "문서 제목", "type": "text"},
                {"id": "sections", "label": "주요 섹션 (쉼표로 구분)", "type": "text"},
                {"id": "content_requirement", "label": "내용 요구사항", "type": "textarea"},
                {"id": "format_requirement", "label": "형식 요구사항", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""다음 마크다운 구조로 문서를 작성해주세요:

# {inputs['title']}

주요 섹션: {inputs['sections']}

내용 요구사항:
{inputs['content_requirement']}

형식 요구사항:
{inputs['format_requirement']}

위 구조를 따라 마크다운 형식으로 체계적인 문서를 작성해주세요.
제목은 #, ##, ###을 사용하고, 필요에 따라 표, 목록, 강조 등을 활용하세요."""


class FukkatsuTechnique(PromptTechnique):
    """후카츠 프롬프트 기법"""

    def __init__(self):
        super().__init__(
            name="⚙️ 후카츠 프롬프트 기법",
            description="4단계 구조화",
            difficulty="medium",
            fields=[
                {"id": "command", "label": "# 명령문 (역할과 작업)", "type": "textarea"},
                {"id": "constraints", "label": "# 제약조건", "type": "textarea"},
                {"id": "input", "label": "# 입력문 (처리할 데이터)", "type": "textarea"},
                {"id": "output", "label": "# 출력문 (결과 형식)", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""# 명령문
{inputs['command']}

# 제약조건
{inputs['constraints']}

# 입력문
{inputs['input']}

# 출력문
다음 형식으로 출력하세요:
{inputs['output']}"""


class FormatSpecTechnique(PromptTechnique):
    """형식 지정 기법"""

    def __init__(self):
        super().__init__(
            name="📊 형식 지정 기법",
            description="JSON/CSV 등 형식 고정",
            difficulty="easy",
            fields=[
                {"id": "format_type", "label": "출력 형식 (JSON/CSV/XML/YAML/표)", "type": "text"},
                {"id": "schema", "label": "스키마/구조", "type": "textarea"},
                {"id": "data_source", "label": "처리할 데이터/내용", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""다음 {inputs['format_type']} 형식으로 정확히 출력하세요:

스키마/구조:
{inputs['schema']}

중요: {inputs['format_type']} 형식만 출력하고, 다른 설명이나 텍스트는 포함하지 마세요.

처리할 데이터:
{inputs['data_source']}

{inputs['format_type']}:"""


class ShunsukeTechnique(PromptTechnique):
    """슌스케 템플릿 기법"""

    def __init__(self):
        super().__init__(
            name="🔧 슌스케 템플릿 기법",
            description="프로그래밍적 설계",
            difficulty="hard",
            fields=[
                {"id": "variables", "label": "변수 정의", "type": "textarea"},
                {"id": "steps", "label": "실행 단계", "type": "textarea"},
                {"id": "conditions", "label": "조건/반복 로직 (선택)", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        conditions_part = f"\n# === 조건/반복 로직 ===\n{inputs['conditions']}\n" if inputs.get('conditions') else ""
        return f"""# === 변수 정의 ===
{inputs['variables']}

# === 실행 단계 ===
{inputs['steps']}
{conditions_part}
위 단계를 순서대로 실행하고, 각 STEP의 결과를 명시하세요.
변수를 참조할 때는 $변수명 형식을 사용하세요."""


class QATechnique(PromptTechnique):
    """Q&A 기법"""

    def __init__(self):
        super().__init__(
            name="❓ Q&A 기법",
            description="질문-답변 패턴 학습",
            difficulty="medium",
            fields=[
                {"id": "q1", "label": "예시 질문 1", "type": "text"},
                {"id": "a1", "label": "예시 답변 1", "type": "textarea"},
                {"id": "q2", "label": "예시 질문 2", "type": "text"},
                {"id": "a2", "label": "예시 답변 2", "type": "textarea"},
                {"id": "actual_q", "label": "실제 질문", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""다음 Q&A 예시들의 스타일과 형식을 학습하여, 동일한 방식으로 답변해주세요:

Q: {inputs['q1']}
A: {inputs['a1']}

Q: {inputs['q2']}
A: {inputs['a2']}

이제 다음 질문에 같은 스타일로 답변해주세요:

Q: {inputs['actual_q']}
A:"""


class ContinuationTechnique(PromptTechnique):
    """이어쓰기 기법"""

    def __init__(self):
        super().__init__(
            name="✍️ 이어쓰기 기법",
            description="자연스러운 문장 완성",
            difficulty="easy",
            fields=[
                {"id": "context", "label": "맥락/배경", "type": "textarea"},
                {"id": "tone", "label": "톤/스타일", "type": "text"},
                {"id": "target", "label": "대상 독자", "type": "text"},
                {"id": "length", "label": "목표 길이", "type": "text"},
                {"id": "start_text", "label": "시작 텍스트", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""다음 조건에 맞춰 텍스트를 이어서 작성해주세요:

맥락/배경: {inputs['context']}
톤/스타일: {inputs['tone']}
대상 독자: {inputs['target']}
목표 길이: {inputs['length']}

시작 텍스트:
{inputs['start_text']}

위 시작 텍스트를 자연스럽게 이어서 작성해주세요:"""


class ChainOfThoughtTechnique(PromptTechnique):
    """Chain of Thought 기법"""

    def __init__(self):
        super().__init__(
            name="🧠 Chain of Thought 기법",
            description="단계별 추론",
            difficulty="hard",
            fields=[
                {"id": "problem", "label": "문제/질문", "type": "textarea"},
                {"id": "verification", "label": "검증 기준 (선택)", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        verification_part = f"\n검증 기준:\n{inputs['verification']}\n" if inputs.get('verification') else ""
        return f"""문제: {inputs['problem']}

위 문제를 해결하기 위해 단계별로 생각해봅시다:

단계 1: [문제 이해 및 분석]
단계 2: [접근 방법 결정]
단계 3: [세부 단계 실행]
단계 4: [중간 결과 확인]
단계 5: [최종 답변 도출]
{verification_part}
각 단계의 사고 과정을 명시적으로 보여주고, 최종 답변을 제시해주세요."""


class MultiPersonaTechnique(PromptTechnique):
    """멀티 페르소나 기법"""

    def __init__(self):
        super().__init__(
            name="👥 멀티 페르소나 기법",
            description="다각적 분석",
            difficulty="hard",
            fields=[
                {"id": "topic", "label": "분석 주제/문제", "type": "textarea"},
                {"id": "persona1", "label": "페르소나 1 (역할, 관점)", "type": "text"},
                {"id": "persona2", "label": "페르소나 2 (역할, 관점)", "type": "text"},
                {"id": "persona3", "label": "페르소나 3 (역할, 관점)", "type": "text"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""주제: {inputs['topic']}

위 주제에 대해 3가지 다른 전문가 관점에서 분석해주세요:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 페르소나 1: {inputs['persona1']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[이 관점에서의 분석]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 페르소나 2: {inputs['persona2']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[이 관점에서의 분석]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔧 페르소나 3: {inputs['persona3']}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[이 관점에서의 분석]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ 종합 결론
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[3가지 관점을 종합한 최종 결론과 권장사항]"""


class AntiHallucinationTechnique(PromptTechnique):
    """할루시네이션 방지 기법"""

    def __init__(self):
        super().__init__(
            name="🛡️ 할루시네이션 방지 기법",
            description="사실 기반 답변",
            difficulty="medium",
            fields=[
                {"id": "query", "label": "질문/확인 사항", "type": "textarea"},
                {"id": "domain", "label": "분야 (일반/의학/법률/금융/역사/뉴스)", "type": "text"}
            ]
        )

    def generate_prompt(self, inputs):
        domain_warnings = {
            '의학': '\n⚠️ 의학 정보는 일반적인 내용만 제공하며, 전문의 상담이 필수임을 명시하세요.',
            '건강': '\n⚠️ 의학 정보는 일반적인 내용만 제공하며, 전문의 상담이 필수임을 명시하세요.',
            '법률': '\n⚠️ 법률 정보는 참고용이며, 정확한 법적 조언은 변호사 상담이 필요함을 명시하세요.',
            '금융': '\n⚠️ 투자 정보는 참고용이며, 투자 결정은 본인 책임임을 명시하세요.',
            '투자': '\n⚠️ 투자 정보는 참고용이며, 투자 결정은 본인 책임임을 명시하세요.',
            '역사': '\n⚠️ 역사적 사실은 공식 기록을 기반으로 하며, 해석과 사실을 구분하세요.',
            '뉴스': '\n⚠️ 정보의 시점을 명확히 하고, 최신 정보 확인을 권장하세요.'
        }

        domain = inputs['domain']
        warning = domain_warnings.get(domain, '')

        return f"""질문: {inputs['query']}{warning}

다음 규칙을 엄격히 준수하여 답변하세요:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📋 필수 준수 사항
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. 확인된 사실만 답변
   - 공식 자료, 학술 자료, 정부 기관 자료 우선
   - 출처를 명시: [기관/저자, 발행일, URL/문헌]

2. 불확실성 표현
   - 확실: "~입니다"
   - 개연성 높음: "~로 알려져 있습니다"
   - 불확실: "정확한 정보를 확인할 수 없습니다"

3. 금지 사항
   - ❌ 존재하지 않는 출처 인용
   - ❌ 추측을 사실처럼 표현
   - ❌ 날짜, 숫자, 이름 추측
   - ❌ "아마도", "~것 같습니다" 등 애매한 표현

4. 모를 때의 답변
   "해당 정보를 확인할 수 없습니다. 다음 출처를 참고하세요: [신뢰할 수 있는 출처 제안]"

답변:"""


class ReActTechnique(PromptTechnique):
    """ReAct 기법"""

    def __init__(self):
        super().__init__(
            name="🔄 ReAct 기법",
            description="추론과 행동 반복",
            difficulty="hard",
            fields=[
                {"id": "goal", "label": "최종 목표", "type": "textarea"},
                {"id": "tools", "label": "사용 가능한 도구", "type": "textarea"}
            ]
        )

    def generate_prompt(self, inputs):
        return f"""목표: {inputs['goal']}

사용 가능한 도구:
{inputs['tools']}

ReAct 사이클을 사용하여 목표를 달성하세요. 각 사이클은 다음 형식을 따릅니다:

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔄 Cycle 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💭 Thought (생각):
현재 상황: [목표와 현재 상태]
알고 있는 것: [기존 정보]
모르는 것: [필요한 정보]
다음 행동: [계획]

🎯 Action (행동):
사용할 도구: [도구명]
실행 내용: [구체적 행동]

👁️ Observation (관찰):
결과: [행동의 결과]
발견: [새로 알게 된 정보]

📊 Evaluation (평가):
달성도: [0-100%]
다음 단계 필요: [예/아니오]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

필요한 만큼 사이클을 반복하고, 최종적으로 다음 형식으로 답변하세요:

✅ 최종 답변
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[목표에 대한 명확한 답변]

실행 과정 요약:
- 총 사이클 수: [N]
- 사용한 도구: [목록]
- 핵심 발견: [요약]"""


# 모든 기법 매핑
TECHNIQUES = {
    'few-shot': FewShotTechnique(),
    'role-playing': RolePlayingTechnique(),
    'markdown': MarkdownTechnique(),
    'fukkatsu': FukkatsuTechnique(),
    'format-spec': FormatSpecTechnique(),
    'shunsuke': ShunsukeTechnique(),
    'qa': QATechnique(),
    'continuation': ContinuationTechnique(),
    'cot': ChainOfThoughtTechnique(),
    'multi-persona': MultiPersonaTechnique(),
    'anti-hallucination': AntiHallucinationTechnique(),
    'react': ReActTechnique()
}


def get_technique(technique_id):
    """기법 ID로 기법 객체 가져오기"""
    return TECHNIQUES.get(technique_id)


def list_techniques():
    """모든 기법 목록 반환"""
    return TECHNIQUES
