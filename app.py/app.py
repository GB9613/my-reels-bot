import streamlit as st
import google.generativeai as genai

# --- 1. 初始化與設定 ---
# 請在此處填入你的 API Key，或設定為環境變數
API_KEY = "你的_GEMINI_API_KEY"
genai.configure(api_key=API_KEY)

# 設定網頁標題與圖示
st.set_page_config(page_title="五泰房屋短影音生成器", page_icon="🎬")

# --- 2. 側邊欄：進階參數設定 ---
with st.sidebar:
    st.title("⚙️ 設定參數")
    model_choice = st.selectbox("選擇模型", ["gemini-1.5-flash", "gemini-1.5-pro"])
    tone = st.radio("語氣風格", ["活潑幽默", "專業權威", "親切鄰家", "阿泰/小五專屬口吻"])
    platform = st.multiselect("目標平台", ["Reels", "TikTok", "YT Shorts"], default=["Reels"])
    
    st.divider()
    st.info("這是一個專為五泰房屋設計的自動化文案工具。")

# --- 3. 主界面：輸入區域 ---
st.title("🎬 短影音標題與文案生成器")
st.subheader("填寫下方資訊，一鍵產出爆款內容")

col1, col2 = st.columns(2)
with col1:
    topic = st.text_input("影片核心主題", placeholder="例如：新北社宅申請攻略")
    target_audience = st.text_input("目標受眾", placeholder="例如：在五股找房的年輕租屋族")

with col2:
    key_points = st.text_area("必看亮點 (每行一個)", placeholder="免仲介費\n政府補助最高5000\n專業代管")

# --- 4. 邏輯核心：Prompt 工程 ---
def generate_copy(topic, audience, points, tone, platforms):
    model = genai.GenerativeModel(model_choice)
    
    # 建立強大的指令
    prompt = f"""
    你現在是一位資深的社群媒體經營專家，擅長製作 Instagram Reels, TikTok 與 YouTube Shorts 的爆款文案。
    
    請針對以下資訊生成文案：
    - 主題：{topic}
    - 受眾：{audience}
    - 關鍵重點：{points}
    - 語氣：{tone}
    - 平台：{', '.join(platforms)}

    輸出格式要求：
    1. 【5 個吸睛標題】：包含懸念型、利益型、恐懼型。
    2. 【文案正文】：
       - 前 3 秒的 Hook（黃金鉤子）
       - 內容重點摘要（使用 Emoji 列表）
       - 行動呼籲 (CTA)
    3. 【Hashtags】：提供 10 個與房地產、租屋、新北區域相關的標籤。
    
    若語氣選擇「阿泰/小五專屬口吻」，請融入五泰房屋吉祥物的特色。
    """
    
    response = model.generate_content(prompt)
    return response.text

# --- 5. 執行與呈現 ---
if st.button("🚀 開始生成文案", type="primary"):
    if not topic:
        st.warning("請至少填寫影片主題喔！")
    else:
        with st.spinner('AI 正在腦力激盪中...'):
            try:
                result = generate_copy(topic, target_audience, key_points, tone, platform)
                
                st.success("✨ 生成完成！")
                st.markdown("---")
                st.markdown(result)
                
                # 下載按鈕 (方便複製)
                st.download_button("💾 下載文案", result, file_name=f"{topic}_文案.txt")
                
            except Exception as e:
                st.error(f"發生錯誤：{e}")

# --- 6. 頁尾資訊 ---
st.caption("© 2026 住商不動產五泰房屋 - 內部自動化工具")