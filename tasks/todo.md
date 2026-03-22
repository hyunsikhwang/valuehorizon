- [x] 모바일 Chrome 재진입 오류 원인 후보 확인
- [x] `app.py`의 keep-alive 재실행 코드 제거
- [x] 정적 검증 수행
- [x] 변경사항 리뷰 및 Git 절차 수행

## Review
- 정적 포털 앱에서 불필요하게 30초마다 돌던 `@st.fragment` keep-alive 로직을 제거해, 모바일 Chrome이 오래 백그라운드에 있던 탭을 복구할 때 Streamlit Cloud 세션 리다이렉트 루프가 겹치지 않도록 정리함
- 페이지 설정, CSS, 카드 렌더링 및 외부 앱 링크 동작은 유지하고 상단의 세션 재실행 코드만 제거하는 최소 수정으로 반영함
- 검증: `python3 -m py_compile /Users/hyunsikhwang/valuehorizon/app.py` (pass)
