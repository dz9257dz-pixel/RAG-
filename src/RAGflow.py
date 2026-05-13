# ✅ 关键修复：必须在 所有 import 之前 设置 Hugging Face 国内镜像
import os
os.environ["HF_ENDPOINT"] = "https://hf-mirror.com"

# 下方是你原有的所有代码，完全不变
import fitz  # PyMuPDF
import jieba
import numpy as np
from rank_bm25 import BM25Okapi
from sentence_transformers import SentenceTransformer
from openai import OpenAI

class MiniRAGFlow:
    def __init__(self):
        # 1. 向量模型初始化
        model_path = './bge-model'
        if not os.path.exists(model_path):
            model_path = 'BAAI/bge-small-zh-v1.5'
            
        self.embed_model = SentenceTransformer(model_path)
        self.chunks = []
        self.chunk_vectors = []
        self.bm25_model = None
        
        # 2. 大模型客户端初始化 (默认先不填 key，在网页端动态传入)
        self.llm_client = None 

    def init_llm(self, api_key):
        """动态初始化 DeepSeek 大模型"""
        self.llm_client = OpenAI(
            api_key=api_key, 
            base_url="https://api.deepseek.com"
        )

    def parse_pdf_by_layout(self, pdf_path):
        doc = fitz.open(pdf_path)
        parsed_chunks = []
        for page in doc:
            blocks = page.get_text("blocks")
            for b in blocks:
                text = b[4].strip()
                if b[6] == 0 and len(text) > 10:
                    parsed_chunks.append(text.replace('\n', ' '))
        self.chunks = parsed_chunks

    def build_index(self):
        if not self.chunks: return
        self.chunk_vectors = self.embed_model.encode(self.chunks)
        tokenized_chunks = [jieba.lcut(c) for c in self.chunks]
        self.bm25_model = BM25Okapi(tokenized_chunks)

    def hybrid_search(self, query, top_k=3):
        # 向量检索
        query_vec = self.embed_model.encode([query])[0]
        vec_scores = np.dot(self.chunk_vectors, query_vec) / (
            np.linalg.norm(self.chunk_vectors, axis=1) * np.linalg.norm(query_vec)
        )
        vec_ranks = np.argsort(vec_scores)[::-1]

        # BM25 检索
        tokenized_query = jieba.lcut(query)
        bm25_scores = self.bm25_model.get_scores(tokenized_query)
        bm25_ranks = np.argsort(bm25_scores)[::-1]

        # RRF 融合
        rrf_scores = {i: 0 for i in range(len(self.chunks))}
        k = 60
        for rank, idx in enumerate(vec_ranks): rrf_scores[idx] += 1.0 / (k + rank + 1)
        for rank, idx in enumerate(bm25_ranks): rrf_scores[idx] += 1.0 / (k + rank + 1)

        final_indices = sorted(rrf_scores, key=rrf_scores.get, reverse=True)
        return [self.chunks[i] for i in final_indices[:top_k]]
    
    def load_markdown_folder(self, folder_path="data"):
        """读取 data 文件夹下的所有 Markdown 文件并分块（优化版）"""
        import glob
        parsed_chunks = []
        md_files = glob.glob(f"{folder_path}/*.md")
        
        for file in md_files:
            with open(file, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # 同时按 ## 和 ### 以及 # 标题切分，保留更多语义
            # 先按一级标题切
            parts = content.split('\n# ')
            for part in parts:
                # 再按二级标题切
                subparts = part.split('\n## ')
                for subpart in subparts:
                    if len(subpart.strip()) > 30:
                        parsed_chunks.append(subpart.strip())
                    elif len(subpart.strip()) > 5 and len(parsed_chunks) > 0:
                        # 太短的段落追加到上一个区块
                        parsed_chunks[-1] += "\n" + subpart.strip()
                        
        self.chunks = parsed_chunks
        print(f"✅ 从 Markdown 文件夹中加载了 {len(self.chunks)} 个语义区块。")

    def generate_answer(self, query, retrieved_docs):
        if not self.llm_client:
            return "⚠️ 请先在左侧边栏配置 API Key！"
            
        context = "\n\n---\n\n".join(retrieved_docs)
        
        prompt = f"""你是一个专业的企业知识库 AI 助手。
请严格根据以下【参考资料】来回答用户的【问题】。
要求：
1. 如果【参考资料】中没有相关信息，请诚实地回答"抱歉，资料中未提及相关信息"，绝不允许自己编造。
2. 回答要条理清晰，重点内容可以使用 Markdown 加粗。

【参考资料】：
{context}

【用户问题】：
{query}
"""
        try:
            response = self.llm_client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "你是一个严谨的助手，你的回答必须基于提供的文档。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.1,
                stream=True
            )
            return response
        except Exception as e:
            return f"大模型调用出错: {str(e)}"
