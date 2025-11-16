# 🎯 12가지 프롬프트 기법 셀렉터

AI 프롬프트 엔지니어링의 12가지 핵심 기법을 쉽게 활용할 수 있는 도구입니다.

**3가지 버전 제공:**
- 🌐 **웹 버전** (`prompt-selector.html`) - 브라우저에서 바로 실행
- 💻 **Python CLI 버전** (`python_app/`) - 터미널에서 고급 기능 사용
- 🎨 **Python GUI 버전** (`python_gui/`) - 아름다운 데스크톱 앱 ⭐ 추천

## 📚 지원하는 12가지 기법

1. **🎯 Few-Shot 기법** - 소수의 예시로 패턴 학습 (난이도: 중)
2. **👤 역할 지정 기법** - 전문가 역할 부여 (난이도: 하)
3. **📝 마크다운 활용 기법** - 구조화된 문서 작성 (난이도: 하)
4. **⚙️ 후카츠 프롬프트 기법** - 4단계 구조화 (난이도: 중)
5. **📊 형식 지정 기법** - JSON/CSV 등 형식 고정 (난이도: 하)
6. **🔧 슌스케 템플릿 기법** - 프로그래밍적 설계 (난이도: 상)
7. **❓ Q&A 기법** - 질문-답변 패턴 학습 (난이도: 중)
8. **✍️ 이어쓰기 기법** - 자연스러운 문장 완성 (난이도: 하)
9. **🧠 Chain of Thought 기법** - 단계별 추론 (난이도: 상)
10. **👥 멀티 페르소나 기법** - 다각적 분석 (난이도: 상)
11. **🛡️ 할루시네이션 방지 기법** - 사실 기반 답변 (난이도: 중)
12. **🔄 ReAct 기법** - 추론과 행동 반복 (난이도: 상)

## 🤖 지원 AI 모델

- **ChatGPT** (OpenAI GPT-4o)
- **Claude** (Anthropic Claude 3.5 Sonnet)
- **Gemini** (Google Gemini 2.0 Flash)

## 🚀 사용 방법

### 방법 1: 웹 버전 (빠른 시작)

```bash
# 프로젝트 디렉토리로 이동
cd /home/user/12prompt

# 웹 브라우저에서 파일 열기
# prompt-selector.html 파일을 더블클릭하거나
# 브라우저에서 직접 열기
```

### 2. 단계별 사용법

**STEP 1: AI 모델 선택**
- ChatGPT, Claude, Gemini 중 하나를 선택합니다

**STEP 2: API 키 입력**
- 선택한 AI 모델의 API 키를 입력합니다
- API 키 발급 링크가 제공됩니다

**STEP 3: 프롬프트 기법 선택**
- 12가지 기법 중 상황에 맞는 기법을 선택합니다
- 각 기법의 난이도와 설명을 확인할 수 있습니다

**STEP 4: 필요 정보 입력**
- 선택한 기법에 필요한 정보를 입력합니다
- 각 입력 필드에는 예시가 제공됩니다

**STEP 5: 생성 및 결과 확인**
- "AI에게 전송하고 결과 받기" 버튼을 클릭합니다
- AI의 응답을 확인하고 복사할 수 있습니다

### 방법 2: Python CLI 버전 (고급 사용자)

Python CLI 버전은 더 많은 기능을 제공합니다:
- ✅ API 키 영구 저장
- ✅ 프롬프트 히스토리 자동 저장
- ✅ 결과 파일 저장 기능
- ✅ 터미널 기반 인터페이스

#### 설치 및 실행

```bash
# 의존성 설치
cd python_app
pip install -r requirements.txt

# 실행
python main.py
```

자세한 사용법은 [`python_app/README.md`](python_app/README.md)를 참고하세요.

### 방법 3: Python GUI 버전 (가장 쉬움) ⭐ 추천

Python GUI 버전은 웹 디자인의 아름다움과 Python의 강력함을 결합했습니다:
- ✅ 아름다운 그래픽 인터페이스
- ✅ API 키 영구 저장
- ✅ 프롬프트 히스토리 자동 저장
- ✅ 독립 실행 가능한 데스크톱 앱
- ✅ 초보자에게 가장 친화적

#### 설치 및 실행

```bash
# 의존성 설치
cd python_gui
pip install -r requirements.txt

# 실행
python main_gui.py
```

자세한 사용법은 [`python_gui/README.md`](python_gui/README.md)를 참고하세요.

## 📁 파일 구조

```
12prompt/
├── 🌐 웹 버전
│   ├── prompt-selector.html       # 12가지 프롬프트 기법 웹앱
│   └── standalone.html            # 기존 5가지 기법 웹앱 (참고용)
│
├── 💻 Python CLI 버전
│   └── python_app/
│       ├── main.py                # CLI 메인 실행 파일
│       ├── techniques.py          # 12가지 기법 구현
│       ├── api_clients.py         # AI API 클라이언트
│       ├── config.py              # 설정 관리
│       ├── utils.py               # 유틸리티 함수
│       ├── requirements.txt       # 의존성
│       ├── .env.example           # 환경변수 예시
│       └── README.md              # CLI 버전 가이드
│
├── 🎨 Python GUI 버전 ⭐ 추천
│   └── python_gui/
│       ├── main_gui.py            # GUI 메인 실행 파일
│       ├── gui.html               # 프론트엔드 (HTML/CSS/JS)
│       ├── requirements.txt       # 의존성
│       └── README.md              # GUI 버전 가이드
│
├── 📚 참고 자료
│   ├── 12prompt.txt              # 12가지 기법 상세 가이드
│   ├── 12prompt_analysis.json    # 기법 분석 데이터
│   └── README.md                 # 이 파일
```

## 💡 각 기법 사용 시나리오

### 쉬운 난이도 (초보자 추천)
- **역할 지정**: 전문가 답변이 필요할 때
- **마크다운 활용**: 체계적인 문서 작성
- **형식 지정**: JSON/CSV 데이터 추출
- **이어쓰기**: 콘텐츠 자동 생성

### 중간 난이도
- **Few-Shot**: 특정 패턴 학습
- **후카츠**: 복잡한 작업 구조화
- **Q&A**: 일관된 답변 스타일
- **할루시네이션 방지**: 정확한 사실 확인

### 높은 난이도 (고급 사용자)
- **슌스케 템플릿**: 워크플로우 자동화
- **Chain of Thought**: 논리적 문제 해결
- **멀티 페르소나**: 다각적 전략 분석
- **ReAct**: 복잡한 에이전트 작업

## 🎓 기법 조합 추천

**비즈니스 전략 수립**
→ 멀티 페르소나 + Chain of Thought + 할루시네이션 방지

**기술 문서 작성**
→ 마크다운 활용 + 후카츠 + 형식 지정

**데이터 분석**
→ ReAct + Chain of Thought + 형식 지정

**창의적 콘텐츠**
→ 역할 지정 + 이어쓰기 + Few-Shot

## ⚠️ 주의사항

1. **API 키 보안**: API 키는 절대 공개하지 마세요
2. **비용 관리**: 각 API 호출은 비용이 발생할 수 있습니다
3. **할루시네이션**: AI는 잘못된 정보를 생성할 수 있으니 중요한 정보는 검증하세요
4. **고위험 분야**: 의학, 법률, 금융 정보는 전문가 상담을 권장합니다

## 🔗 API 키 발급 링크

- **OpenAI (ChatGPT)**: https://platform.openai.com/api-keys
- **Anthropic (Claude)**: https://console.anthropic.com/settings/keys
- **Google (Gemini)**: https://ai.google.dev/gemini-api/docs/api-key

## 📖 참고 자료

- `12prompt.txt`: 각 기법의 상세 설명, 예시, 주의사항
- `12prompt_analysis.json`: 기법별 데이터 및 성능 비교

## 🆚 3가지 버전 비교

| 기능 | 🌐 웹 버전 | 💻 Python CLI | 🎨 Python GUI ⭐ |
|------|-----------|--------------|------------------|
| **설치** | 불필요 | Python + pip | Python + pip |
| **실행** | 브라우저 | 터미널 | 데스크톱 앱 |
| **인터페이스** | HTML | 텍스트 | 그래픽 |
| **API 키 저장** | 세션만 | 영구 ✅ | 영구 ✅ |
| **히스토리** | 없음 | 자동 저장 ✅ | 자동 저장 ✅ |
| **결과 저장** | 복사만 | 파일 저장 ✅ | 복사 |
| **마우스 사용** | ✅ | ❌ | ✅ |
| **초보자 친화성** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **고급 기능** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **디자인** | 모던 | 기본 | 모던 ✅ |

**추천:**
- **처음 사용 / 빠른 테스트**: 웹 버전
- **일반 사용자 / 편리한 사용**: Python GUI ⭐
- **개발자 / 스크립팅**: Python CLI

---

**Made with ❤️ for AI Prompt Engineering**
