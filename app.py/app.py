import streamlit as st
import google.generativeai as genai

# 直接設定 API Key (跳過 Secrets 步驟)
API_KEY = "AIzaSyDz5AmxSMYFkmUV9XARr_lnbxBZrOWsglw"
genai.configure(api_key=API_KEY)

st.set_page_config(page_title="五泰房屋 AI 文案產生器", page_icon="🎬")

st.title("🎬 短影音文案產生器")
st.info("專為 Reels / TikTok / YT Shorts 設計")

topic = st.text_input("1. 影片主題", placeholder="例如：1580萬入主大三房")
points = st.text_area("2. 影片重點", placeholder="走路就上學、生活機能好")
tone = st.selectbox("3. 選擇語氣", ["活潑有趣", "專業權威", "親切鄰家"])

if st.button("🚀 產生文案"):
    if topic:
        with st.spinner('正在生成中...'):
            try:
                # 這次我們用最保險的模型名稱
                model = genai.GenerativeModel('gemini-1.5-flash')
                prompt = f"你是一位房地產社群專家，請針對主題『{topic}』與重點『{points}』，以『{tone}』的語氣，寫出 3 個吸睛標題、前3秒鉤子文案與一段短影音說明，包含適當的 Emoji。"
                response = model.generate_content(prompt)
                st.success("✨ 生成成功！")
                st.markdown(response.text)
            except Exception as e:
                st.error(f"連線還是有問題，請檢查 API Key。錯誤訊息：{e}")
    else:
        st.warning("請輸入主題喔！")

st.caption("© 2026 住商不動產五泰房屋")
