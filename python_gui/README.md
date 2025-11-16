# 🎯 12가지 프롬프트 기법 셀렉터 (Python GUI)

PyWebView를 사용한 **데스크톱 GUI 애플리케이션**입니다.
웹 디자인의 아름다움과 Python의 강력함을 결합했습니다! 🚀

## ✨ 특징

- 🎨 **아름다운 UI** - HTML/CSS/JavaScript로 만든 모던한 디자인
- 💻 **네이티브 앱** - 독립 실행 가능한 데스크톱 애플리케이션
- 💾 **API 키 영구 저장** - 한 번 입력하면 계속 사용 가능
- 📝 **히스토리 자동 저장** - 모든 작업 기록 보관
- 🔄 **실시간 통신** - Python 백엔드와 JavaScript 프론트엔드 완벽 연동

## 📦 설치

### 1. 필수 요구사항

- Python 3.7 이상
- pip

### 2. 의존성 설치

```bash
cd python_gui
pip install -r requirements.txt
```

**설치되는 패키지:**
- `pywebview` - Python GUI 프레임워크
- `requests` - AI API 호출
- `python-dotenv` - 환경변수 관리

### 3. 플랫폼별 추가 요구사항

#### Windows
```bash
pip install pywebview[winforms]
```

#### macOS
```bash
pip install pywebview[cocoa]
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0
pip install pywebview[gtk]
```

## 🚀 실행

```bash
# GUI 앱 실행
python main_gui.py
```

또는 실행 권한 부여 후:

```bash
chmod +x main_gui.py
./main_gui.py
```

## 🎮 사용 방법

### 1단계: AI 모델 선택
- ChatGPT, Claude, Gemini 중 선택
- 마지막 사용 모델이 자동 선택됩니다

### 2단계: API 키 입력 및 저장
- API 키 입력
- 💾 **저장** 버튼 클릭 (선택사항)
- 저장하면 다음부터 자동으로 불러옵니다

### 3단계: 프롬프트 기법 선택
- 12가지 기법 중 하나 선택
- 난이도별로 분류되어 있습니다:
  - 🟢 쉬움
  - 🟡 보통
  - 🔴 어려움

### 4단계: 정보 입력
- 선택한 기법에 필요한 정보 입력
- 동적으로 생성되는 입력 폼 사용

### 5단계: 결과 받기
- ✨ "AI에게 전송하고 결과 받기" 클릭
- 결과 확인 및 복사

## 🎨 CLI vs GUI 비교

| 기능 | CLI 버전 | GUI 버전 |
|------|---------|----------|
| **인터페이스** | 터미널 | 그래픽 창 |
| **사용 편의성** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **시각적 디자인** | 없음 | 모던한 UI |
| **API 키 저장** | ✅ | ✅ |
| **히스토리** | ✅ | ✅ |
| **마우스 사용** | ❌ | ✅ |
| **초보자 친화성** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **고급 사용자** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |

**추천:**
- **처음 사용자** → GUI 버전 (쉬운 사용)
- **개발자/고급 사용자** → CLI 버전 (스크립팅 가능)
- **일반 사용자** → GUI 버전 (편리한 UI)

## 📁 파일 구조

```
python_gui/
├── main_gui.py          # 메인 실행 파일 (PyWebView 앱)
├── gui.html             # 프론트엔드 (HTML/CSS/JS)
├── requirements.txt     # 의존성 목록
└── README.md            # 이 파일

공유 모듈 (../python_app/):
├── techniques.py        # 12가지 기법 구현
├── api_clients.py       # AI API 클라이언트
├── config.py            # 설정 관리
└── utils.py             # 유틸리티 함수
```

## 🔧 기술 스택

### 프론트엔드
- **HTML5** - 구조
- **Tailwind CSS** - 스타일링
- **JavaScript (ES6+)** - 로직

### 백엔드
- **Python 3.7+** - 메인 언어
- **PyWebView** - GUI 프레임워크
- **Requests** - HTTP 통신

### 통신
- **PyWebView API** - Python ↔ JavaScript 양방향 통신

## 🎯 주요 기능

### 1️⃣ API 키 관리
```python
# Python 백엔드에서 관리
- 환경변수 지원
- 설정 파일 영구 저장
- 보안 마스킹 처리
```

### 2️⃣ 프롬프트 생성
```python
# 12가지 기법 동적 로드
- Few-Shot, 역할 지정, 마크다운...
- 각 기법별 맞춤 입력 폼
- 실시간 유효성 검사
```

### 3️⃣ AI 응답 생성
```python
# 3가지 AI 모델 지원
- OpenAI (ChatGPT)
- Anthropic (Claude)
- Google (Gemini)
```

### 4️⃣ 히스토리 저장
```python
# 자동 기록
- 최근 100개 작업 저장
- 프롬프트 및 결과 요약
- ~/.12prompt/history.json
```

## 🐛 문제 해결

### PyWebView 설치 오류

**Windows에서 설치 실패:**
```bash
pip install --upgrade pip
pip install pywebview[winforms]
```

**Linux에서 설치 실패:**
```bash
sudo apt-get update
sudo apt-get install python3-gi gir1.2-webkit2-4.0
pip install pywebview[gtk]
```

### 앱이 실행되지 않음

1. **Python 버전 확인:**
   ```bash
   python --version  # 3.7 이상 필요
   ```

2. **의존성 재설치:**
   ```bash
   pip install --force-reinstall -r requirements.txt
   ```

3. **디버그 모드 실행:**
   ```python
   # main_gui.py에서 debug=True로 설정
   webview.start(debug=True)
   ```

### API 키 문제

**저장된 키가 작동하지 않음:**
```bash
# 설정 파일 삭제 후 재시도
rm -rf ~/.12prompt/config.json
```

**환경변수 사용:**
```bash
# .env 파일 사용
cp ../python_app/.env.example .env
# .env 파일 편집
```

## 📦 독립 실행 파일 만들기 (선택사항)

PyInstaller를 사용해서 `.exe` 파일로 배포할 수 있습니다:

```bash
# PyInstaller 설치
pip install pyinstaller

# 실행 파일 생성
pyinstaller --onefile --windowed main_gui.py

# dist/ 폴더에 실행 파일 생성됨
```

## 🆚 다른 버전과 비교

### 🌐 웹 버전 (`prompt-selector.html`)
- ✅ 설치 불필요
- ✅ 브라우저에서 실행
- ❌ API 키 영구 저장 불가
- ❌ 히스토리 없음

### 💻 Python CLI (`python_app/`)
- ✅ API 키 영구 저장
- ✅ 히스토리 자동 저장
- ❌ 터미널 전용
- ❌ GUI 없음

### 🎨 Python GUI (`python_gui/`) ⭐ 추천
- ✅ API 키 영구 저장
- ✅ 히스토리 자동 저장
- ✅ 아름다운 GUI
- ✅ 마우스 사용 가능
- ✅ 초보자 친화적

## 🔐 보안 주의사항

1. **API 키 관리**
   - API 키는 `~/.12prompt/config.json`에 평문으로 저장됩니다
   - 공용 컴퓨터에서는 저장하지 마세요
   - 사용 후 삭제 권장: `rm ~/.12prompt/config.json`

2. **네트워크 보안**
   - API 호출은 HTTPS로 암호화됩니다
   - 공용 Wi-Fi에서는 주의하세요

## 🎓 개발자 가이드

### Python-JavaScript 통신 예시

**Python (백엔드):**
```python
class API:
    def get_techniques_list(self):
        return list_techniques()
```

**JavaScript (프론트엔드):**
```javascript
const techniques = await pywebview.api.get_techniques_list();
```

### 새 기능 추가하기

1. **Python API 메서드 추가** (`main_gui.py`)
2. **JavaScript에서 호출** (`gui.html`)
3. **UI 업데이트**

## 📞 지원

문제가 발생하면:
1. 이 README의 "문제 해결" 섹션 확인
2. Python 및 PyWebView 버전 확인
3. GitHub Issues에 버그 리포트

## 📜 라이센스

MIT License

---

**Made with ❤️ for AI Prompt Engineering**
**Powered by PyWebView + Python + HTML/CSS/JS**
