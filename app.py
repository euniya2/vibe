import streamlit as st
from openai import OpenAI

# 페이지 설정
st.set_page_config(page_title="AI 수업 설계 도우미", layout="wide")

st.title("🎓 AI 수업 설계 도우미")
st.subheader("과목과 단원만 입력하면 수업의 뼈대를 잡아줍니다.")

# 사이드바에서 API 키 입력 받기 (보안을 위해)
with st.sidebar:
    st.title("⚙️ 설정")
    api_key = st.text_input("OpenAI API Key를 입력하세요", type="password")
    st.info("API Key가 없으면 동작하지 않습니다.")

# 메인 입력창
col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("과목명", placeholder="예: 정보, 국어, 과학")
with col2:
    topic = st.text_input("단원명 또는 주제", placeholder="예: 파이썬 조건문, 시의 함축적 의미")

if st.button("수업 설계안 생성하기"):
    if not api_key:
        st.error("먼저 사이드바에 API Key를 입력해 주세요!")
    elif not subject or not topic:
        st.warning("과목명과 주제를 모두 입력해 주세요.")
    else:
        try:
            client = OpenAI(api_key=api_key)
            
            with st.spinner('AI가 수업을 설계 중입니다...'):
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": "너는 전문적인 수업 설계자야. 교사들을 위해 창의적이고 체계적인 수업 지도안을 작성해줘."},
                        {"role": "user", "content": f"{subject} 과목의 '{topic}' 주제로 수업 목표 3가지와 '도입-전개-정리' 단계별 활동을 표 형식으로 작성해줘."}
                    ]
                )
                
                result = response.choices[0].message.content
                st.markdown("### 📝 완성된 수업 설계안")
                st.write(result)
                
        except Exception as e:
            st.error(f"오류가 발생했습니다: {str(e)}")

st.divider()
st.caption("Jenius의 바이브 코딩 실습 프로젝트 1")
