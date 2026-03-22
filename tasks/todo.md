- [x] 기존 `app.py` 구조와 삽입 위치 확인
- [x] Streamlit Cloud keep-alive fragment 추가
- [x] 정적 검증 수행
- [x] 변경사항 리뷰 및 Git 절차 수행

## Review
- `app.py` 상단에 `timedelta` import와 30초 주기의 `@st.fragment` keep-alive 함수를 추가해 Streamlit Cloud 세션 리디렉션 완화를 위한 주기적 재실행 지점을 만들었음
- 기존 레이아웃, CSS, 카드 렌더링 흐름은 건드리지 않고 초기 설정 직후에만 fragment를 호출하도록 최소 수정으로 반영함
- 검증: `python3 -m py_compile /Users/hyunsikhwang/valuehorizon/app.py` (pass)

- [x] 현재 UI 구조 및 CSS 테마 포인트 확인
- [x] `app.py`를 라이트 모드 팔레트로 전환
- [x] 실행 또는 정적 검토로 결과 검증
- [ ] 변경사항 리뷰 및 Git 절차 수행

## Review
- 기존 레이아웃, 카드 마크업, 링크 동작은 유지하고 CSS 색상 체계만 라이트 모드 기준으로 재정의함
- `app.py` 상단 CSS에 색상 토큰을 추가해 배경, 카드, 텍스트, 그림자 톤을 일관되게 관리하도록 정리함
- 검증: `python3 -m py_compile /Users/hyunsikhwang/valuehorizon/app.py` (pass)
- 검증: `python3 -m streamlit run app.py --server.headless true --server.port 8505` (fail: No module named streamlit)
