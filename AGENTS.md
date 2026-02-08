# 프로젝트 가이드라인: Streamlit Modern UI Kit

## 1. 핵심 기술 스택
- **언어**: Python 3.12+ (강제 사항)
- **프레임워크**: Streamlit
- **배포 환경**: Streamlit Cloud
- **시각화**: `pyecharts`를 최우선으로 사용 (필요시 plotly, altair 병행 가능)

## 2. UI/UX 디자인 원칙
- **테마**: 반드시 **Light Mode**를 기준으로 작업합니다.
- **분위기**: Minimal, Modern, Clean, Sharp.
- **아이덴티티**: "Streamlit 기본 앱처럼 보이지 않게" 만드는 것이 목표입니다.
- **타이포그래피**: 
  - 영문: Inter
  - 한글: Pretendard
  - CSS를 통해 Google Fonts 또는 CDN으로 폰트를 강제 적용하세요.

## 3. 핵심 제약 사항 (Must-Follow)
- **여백 관리**: 메인 페이지 상단의 거대한 여백(`#root > div:nth-child(1) > ...`)을 CSS로 제거하거나 대폭 축소하세요.
- **표(Table) 출력**: `st.write`, `st.dataframe` 사용을 지양합니다. `st-aggrid`, `streamlit-awesome-table` 또는 커스텀 HTML/CSS 기반 테이블을 사용하여 동적이고 세련된 디자인을 제공하세요.
- **커스텀 CSS**: 모든 앱에는 기본적으로 `style.css`를 주입하거나 `st.markdown(..., unsafe_allow_html=True)`를 통해 기본 UI 컴포넌트의 디자인을 덮어써야 합니다.