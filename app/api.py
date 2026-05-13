from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from RAGflow import MiniRAGFlow

# 1. 初始化 FastAPI 应用
app = FastAPI(title="企业级 RAG 知识库引擎 API")

# 2. 全局加载 RAG 引擎
rag_engine = MiniRAGFlow()
rag_engine.load_markdown_folder("data")
rag_engine.build_index()

# 如果你有 DeepSeek API Key，在这里取消注释并填入你的 Key
# rag_engine.init_llm("sk-你的真实API-KEY")

class ChatRequest(BaseModel):
    query: str
    top_k: int = 3
    use_llm: bool = False  # 新增：是否使用大模型生成回答

class ChatResponse(BaseModel):
    code: int
    query: str
    answer: str = ""
    retrieved_contexts: list = []
    message: str = ""

@app.get("/", response_class=HTMLResponse)
async def index():
    with open("chat.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.post("/v1/chat")
async def chat_endpoint(request: ChatRequest):
    try:
        # 第一步：混合检索找资料
        retrieved_docs = rag_engine.hybrid_search(request.query, top_k=request.top_k)
        
        # 第二步：如果配置了大模型且 use_llm=True，就生成回答
        answer = ""
        if request.use_llm and rag_engine.llm_client:
            raw_answer = rag_engine.generate_answer(request.query, retrieved_docs)
            if isinstance(raw_answer, str):
                answer = raw_answer
            else:
                # 流式响应 -> 直接拼接
                full = ""
                for chunk in raw_answer:
                    if chunk.choices[0].delta.content:
                        full += chunk.choices[0].delta.content
                answer = full
        else:
            # 不启用大模型时，简单拼接检索结果
            answer = "根据检索到的资料：\n\n"
            for i, doc in enumerate(retrieved_docs):
                answer += f"**片段 {i+1}：**\n{doc}\n\n"
        
        return {
            "code": 200,
            "query": request.query,
            "answer": answer,
            "retrieved_contexts": retrieved_docs,
            "message": "检索成功"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
