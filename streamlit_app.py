# streamlit_app.py

import streamlit as st
import random

# 앱의 제목 설정
st.title("🥠 행운의 포츈쿠키")

# 미리 준비된 운세 메시지 리스트
fortune_messages = [
    "새로운 기회가 당신을 찾아올 것입니다.",
    "작은 변화가 큰 성공으로 이어질 것입니다.",
    "오늘은 당신의 날입니다! 모든 일이 잘 풀릴 거예요.",
    "주변 사람들에게 친절을 베풀면 더 큰 복이 돌아옵니다.",
    "꾸준함이 결국 당신을 정상으로 이끌 것입니다.",
    "생각지도 못한 곳에서 행운이 찾아옵니다.",
    "잠시 쉬어가세요. 휴식은 다음 도약을 위한 준비입니다.",
    "당신의 재능이 곧 빛을 발하게 될 것입니다.",
    "긍정적인 생각은 긍정적인 결과를 낳습니다.",
    "오늘은 새로운 것을 배우기에 완벽한 날입니다."
]

# st.session_state를 사용하여 상태 유지
# 'fortune' 이라는 키가 세션 상태에 없으면 초기 메시지로 설정
if 'fortune' not in st.session_state:
    st.session_state.fortune = "아래 버튼을 눌러 오늘의 운세를 확인하세요!"

# '오늘의 운세 확인하기' 버튼 생성
if st.button("오늘의 운세 확인하기"):
    # 버튼이 클릭되면, 운세 리스트에서 메시지를 랜덤으로 선택
    selected_fortune = random.choice(fortune_messages)
    # 선택된 메시지를 세션 상태에 저장하여 화면이 갱신되어도 유지되도록 함
    st.session_state.fortune = selected_fortune

# 운세 메시지를 화면에 보기 좋게 출력
st.success(f"**{st.session_state.fortune}**")

# 간단한 설명 추가
st.markdown("---")
st.info("버튼을 누를 때마다 새로운 운세 메시지가 나타납니다.")