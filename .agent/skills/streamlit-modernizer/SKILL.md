---
name: streamlit-modern-ui-expert
description: Streamlit 앱을 Python 기반의 모던하고 유니크한 웹 대시보드로 변신시킵니다.
triggers: ["create app", "UI setup", "design layout", "css injection", "table design"]
---

# Streamlit 모던 UI 최적화 가이드

## 1. 전역 스타일 및 폰트 주입 (Standard Injection)
에이전트는 모든 프로젝트의 초기 설정 단계에서 아래의 `inject_custom_css()` 함수를 반드시 포함하고 호출해야 합니다.

```python
import streamlit as st

def inject_custom_css():
    st.markdown("""
        <style>
            /* 폰트 로드: Pretendard & Inter */
            @import url('[https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css](https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css)');
            @import url('[https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap](https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap)');
            
            /* 전체 기본 폰트 설정 */
            html, body, [class*="css"] {
                font-family: 'Pretendard', 'Inter', sans-serif !important;
            }

            /* 상단 여백 제거 및 레이아웃 최적화 */
            .block-container {
                padding-top: 1rem !important;
                padding-bottom: 1rem !important;
                max-width: 95% !important;
            }

            /* Streamlit 기본 헤더/푸터 숨기기 (유니크한 느낌) */
            header, footer, #MainMenu {
                visibility: hidden;
                height: 0;
            }

            /* 모던한 카드 스타일의 컨테이너 디자인 */
            div[data-testid="stVerticalBlock"] > div:has(div.stMarkdown) {
                background-color: #ffffff;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
                border: 1px solid #f0f0f0;
                margin-bottom: 1rem;
            }
        </style>
    """, unsafe_allow_html=True)
```

## 2. 고급 데이터 테이블 구현 (Anti-Default Table)
st.dataframe 대신 디자인과 기능성이 뛰어난 라이브러리를 사용합니다.
- 우선순위: st-aggrid 또는 streamlit-antd-components의 Table 활용.
- 스타일 전략:
    - Zebra Striping(줄무늬) 적용.
    - 헤더는 배경색을 매우 연한 회색(#F9FAFB)으로 설정하고 텍스트는 굵게.
    - 셀 내부의 텍스트 정렬 및 여백(Padding)을 여유 있게 확보.

## 3. Pyecharts 시각화 원칙
차트는 streamlit-echarts를 사용하며, 다음 설정을 준수합니다.
- Theme: 'light' 테마를 기반으로 하되, 배경은 투명(backgroundColor: 'transparent')하게 설정.
- Color Palette: 또렷하고 세련된 파스텔 톤이나 모노톤 조합 사용.
- Interactivity: Tooltip과 DataZoom 기능을 활성화하여 동적인 경험 제공.

##4. 실행 체크리스트
1. 앱 실행 시 가장 먼저 st.set_page_config(layout="wide")를 호출했는가?
2. inject_custom_css()가 호출되어 상단 여백이 제거되었는가?
3. 모든 텍스트가 Pretendard/Inter 폰트로 출력되는가?
4. 표가 Streamlit 기본 형태가 아닌 커스텀 디자인인가?