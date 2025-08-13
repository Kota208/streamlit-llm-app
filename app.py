
import os
from dotenv import load_dotenv
import streamlit as st
from langchain.llms import OpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Webアプリの概要
st.title("専門家LLM相談アプリ")
st.write("""
このアプリは、あなたの質問に対してLLM（大規模言語モデル）が専門家として回答します。
下記のフォームに質問を入力し、専門家の種類を選択して送信してください。
""")

# 専門家の種類
experts = {
	"医療専門家": "あなたは医療分野の専門家です。専門的かつ分かりやすく回答してください。",
	"ITコンサルタント": "あなたはIT分野のコンサルタントです。技術的な観点からアドバイスしてください。",
	"英語教師": "あなたは英語教育の専門家です。英語学習者に分かりやすく説明してください。"
}

# 入力フォーム
user_input = st.text_area("質問を入力してください：")
expert_type = st.radio("専門家の種類を選択：", list(experts.keys()))

# LLMに問い合わせる関数
def get_llm_response(text, expert):
	system_message = experts[expert]
	llm = OpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7)
	prompt = f"{system_message}\n質問: {text}"
	return llm(prompt)

if st.button("送信"):
	if user_input.strip():
		with st.spinner("LLMが回答中..."):
			response = get_llm_response(user_input, expert_type)
		st.markdown("### 回答")
		st.write(response)
	else:
		st.warning("質問を入力してください。")

