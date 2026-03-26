import streamlit as st
import google.generativeai as genai

# 1. 核心設定：直接鎖定你能用的模型
API_KEY = "AIzaSyDz5AmxSMYFkmUV9XARr_lnbxBZrOWsglw"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="五泰房屋文案大師", page_icon="🏠")

# 2. 介面設計
st.title("🎬 五泰房屋短影音生成器")
st.write("目前狀態：🟢 連線準備就緒")

topic = st.text_input("影片主題", placeholder="例如：1580萬入主大三房")
points = st.text_area("影片重點", placeholder="走路就上學、通風採光好")
tone = st.selectbox("語氣風格", ["活潑有趣", "專業誠懇", "溫馨動人"])

# 3. 生成邏輯
if st.button("🚀 立即產出爆款文案"):
    if topic:
        with st.spinner('正在與五泰房屋 AI 腦力激盪中...'):
            try:
                # 重點：改成 gemini-pro，這絕對是你的 Key 能開的門
                model = genai.GenerativeModel('gemini-pro')
                prompt = f"你是一位房地產專家，請針對主題『{topic}』與重點『{points}』，以『{tone}』的語氣，寫出3個吸睛標題、一段短影音文案，並加入適合的 Emoji。"
                
                response = model.generate_content(prompt)
                
                st.balloons() # 成功噴氣球
                st.success("✨ 文案生成成功！")
                st.markdown("---")
                st.markdown(response.text)
                
            except Exception as e:
                st.error("連線微調中，請再試一次")
                st.code(str(e))
    else:
        st.warning("請填寫主題喔！")

st.caption("© 2026 住商不動產五泰房屋")
