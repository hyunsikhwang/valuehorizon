# Equity Bridge (📈 에쿼티 브릿지)

**Equity Bridge**는 흩어져 있는 투자 관련 Streamlit 애플리케이션들을 한 곳에서 쉽고 우아하게 접근할 수 있도록 도와주는 프리미엄 포털 사이트입니다.

## 주요 특징 (Key Features)

- **Premium Light Mode UI**: 세련되고 현대적인 라이트 모드 테마를 적용하여 전문적인 금융 포털의 느낌을 제공합니다.
- **Compact Card Design**: 각 애플리케이션을 깔끔한 카드 형태로 배치하여 가독성을 극대화했습니다.
- **Intelligent Tooltips**: 화면을 어지럽히지 않도록 상세 설명은 툴팁(마우스 오버) 형식으로 제공하여 미니멀한 UI를 유지합니다.
- **Flexible Management**: `config.py` 파일 수정을 통해 새로운 사이트를 추가하거나 기존 정보를 변경하는 등 유지보수가 매우 용이합니다.
- **Optimized Layout**: 카드 간 높이 불일치 문제를 해결하여 정규화된 균형 잡힌 레이아웃을 제공합니다.

## 설치 및 실행 방법 (Usage)

### 1. 관련 라이브러리 설치
이 프로젝트는 Streamlit을 기반으로 작동합니다.
```bash
pip install streamlit
```

### 2. 로컬에서 실행
```bash
streamlit run app.py
```

## 프로젝트 구조 (Directory Structure)

- `app.py`: 메인 애플리케이션 로직 및 UI 스타일링을 담당합니다.
- `config.py`: 포털에 표시될 애플리케이션 목록과 설정을 관리합니다.
- `assets/`: 각 사이트를 대표하는 아이콘 이미지들이 포함되어 있습니다.

## 유지보수 가이드 (Maintenance Guide)

새로운 사이트를 추가하고 싶다면 `config.py` 파일의 `APPS` 리스트에 다음 형식으로 데이터를 추가하세요:

```python
{
    "title": "Application Name",
    "url": "https://your-app.streamlit.app/",
    "description": "Short description shown as tooltip",
    "image": "assets/your_icon.png",
    "category": "Category Name"
}
```

---
*Created with the help of Antigravity AI.*