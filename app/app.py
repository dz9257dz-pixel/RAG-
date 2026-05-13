import streamlit as st
import os
from RAGflow import MiniRAGFlow

st.set_page_config(page_title="企业知识库 RAGFlow-Mini", page_icon="📚", layout="wide")
st.title("📚 企业知识库 RAG 系统 (Mini 版)")

@st.cache_resource
def load_rag_engine():
    os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"
    engine = MiniRAGFlow()
    # 自动加载爬取的 Markdown 数据
    if os.path.exists("data") and any(f.endswith(".md") for f in os.listdir("data")):
        engine.load_markdown_folder("data")
        engine.build_index()
    return engine

rag_engine = load_rag_engine()

with st.sidebar:
    st.header("⚙️ 系统配置")
    api_key = st.text_input("请输入 DeepSeek API Key:", type="password")
    if api_key:
        rag_engine.init_llm(api_key)
        st.success("API Key 已加载！")
    else:
        st.warning("⚠️ 请输入 API Key 以启用大模型对话功能。")
    
    st.markdown("---")
    
    # ---------- 上传功能 ----------
    st.header("📂 知识库管理")
    st.info(f"当前知识库: {len(rag_engine.chunks)} 个语义片段")
    
    uploaded_file = st.file_uploader("上传 PDF 或 Markdown 文档", type=["pdf", "md"])
    
    if st.button("解析并加入知识库"):
        if uploaded_file is not None:
            with st.spinner("正在解析文档..."):
                # 保存临时文件
                temp_path = f"temp_{uploaded_file.name}"
                with open(temp_path, "wb") as f:
                    f.write(uploaded_file.getvalue())
                
                if uploaded_file.name.endswith(".pdf"):
                    rag_engine.parse_pdf_by_layout(temp_path)
                elif uploaded_file.name.endswith(".md"):
                    # 直接把 markdown 内容加入知识库
                    with open(temp_path, "r", encoding="utf-8") as f:
                        content = f.read()
                    # 按标题切分
                    paragraphs = content.split("\n## ")
                    for p in paragraphs:
                        if len(p.strip()) > 30:
                            rag_engine.chunks.append(p.strip())
                
                rag_engine.build_index()
                st.success(f"解析成功！当前知识库共 {len(rag_engine.chunks)} 个语义区块。")
                os.remove(temp_path)
        else:
            st.warning("请先选择文件！")
    
    st.markdown("---")
    
    # ---------- 模式选择 ----------
    mode = st.radio(
        "对话模式",
        ["🌐 混合模式（推荐）", "📖 仅知识库", "💬 自由对话"],
        help="混合模式：有资料用资料，没资料自由回答"
    )

st.subheader("💬 智能问答")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_query = st.chat_input("请输入你的问题...")

if user_query:
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.messages.append({"role": "user", "content": user_query})
    
    with st.chat_message("assistant"):
        if not api_key:
            st.error("请先在左侧输入 API Key！")
        else:
            with st.status("思考中...", expanded=True) as status:
                # 1. 检索知识库
                if rag_engine.chunks:
                    st.write("🔍 检索知识库...")
                    retrieved_docs = rag_engine.hybrid_search(user_query, top_k=3)
                    context = "\n\n---\n\n".join(retrieved_docs)
                else:
                    context = ""
                    retrieved_docs = []
                
                # 2. 根据模式生成 prompt
                if mode == "💬 自由对话":
                    instruction = "你是一个友好的 AI 助手，请根据你的知识回答用户的问题。"
                    context = ""  # 不用知识库
                elif mode == "📖 仅知识库":
                    instruction = """你是一个专业的企业知识库 AI 助手。
请严格根据以下【参考资料】来回答用户的【问题】。
要求：
1. 如果【参考资料】中没有相关信息，请诚实地回答"抱歉，资料中未提及相关信息"，绝不允许自己编造。
2. 回答要条理清晰，重点内容可以使用 Markdown 加粗。"""
                else:  # 混合模式
                    if retrieved_docs:
                        instruction = """你是一个 AI 助手。请优先根据【参考资料】回答。
如果参考资料中有相关信息，请基于资料回答。
如果参考资料中没有相关信息，你可以根据自己的知识正常回答，但请注明"以下回答基于我的一般知识"。"""
                    else:
                        instruction = "你是一个友好的 AI 助手，请根据你的知识回答用户的问题。"
                        context = ""
                
                prompt = f"""{instruction}

【参考资料】：
{context}

【用户问题】：
{user_query}
"""
                status.update(label="正在生成回答...", state="running")
            
            # 3. 调用大模型
            try:
                response_stream = rag_engine.llm_client.chat.completions.create(
                    model="deepseek-chat",
                    messages=[
                        {"role": "system", "content": "你是一个友好的 AI 助手。"},
                        {"role": "user", "content": prompt}
                    ],
                    temperature=0.7,
                    stream=True
                )
                
                message_placeholder = st.empty()
                full_response = ""
                
                for chunk in response_stream:
                    if chunk.choices[0].delta.content is not None:
                        full_response += chunk.choices[0].delta.content
                        message_placeholder.markdown(full_response + "▌")
                
                message_placeholder.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
                
            except Exception as e:
                st.error(f"调用大模型出错: {str(e)}")
