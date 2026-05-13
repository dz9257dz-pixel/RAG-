# 📚 RAG 知识库问答系统

RAG（检索增强生成）是一种结合向量检索与大模型生成的 AI 技术： 读取本地文档（PDF/Word/TXT 等），将文本向量化并存储到向量数据库 用户提出问题时，先从知识库中检索最相关的信息 将检索结果 + 用户问题输入大模型，生成精准、有据可依的答案 本项目是轻量级、可快速部署的 RAG 基础框架，适用于企业知识库、文档问答、学术资料检索等场景。

## 1️⃣ 项目介绍

### 这是什么？

RAG（检索增强生成）知识库问答系统是一个**结合了信息检索与大语言模型的智能问答平台**。

**核心流程：**
```
用户提问 → 检索知识库 → 找到相关资料 → 大模型生成回答 → 返回给用户
```

### 适用场景
- 📄 **企业知识库管理**：员工手册、产品文档、技术规范
- 🎓 **学习辅助工具**：课程资料、论文笔记
- 🏢 **内部培训系统**：FAQ 自动问答
- 📝 **文档检索平台**：快速定位文档中的关键信息

---

## 2️⃣ 主要功能

### 🌐 三种对话模式

| 模式 | 说明 | 适用场景 |
|------|------|----------|
| **🌐 混合模式（推荐）** | 优先用知识库回答，找不到则用大模型自身知识 | 日常使用 |
| **📖 仅知识库** | 严格基于知识库回答，找不到就说"未提及" | 严谨的企业场景 |
| **💬 自由对话** | 完全使用大模型自身能力，不检索知识库 | 普通聊天 |

### 📂 文档管理
- ✅ 支持 **Markdown（.md）** 文件上传
- ✅ 支持 **PDF（.pdf）** 文件上传
- ✅ 支持从网页**自动爬取**文档（crawler.py）
- ✅ 上传后自动解析、分块、建索引

### 🔍 智能检索
- ✅ **向量语义检索**：理解问题的深层含义
- ✅ **关键词检索**：精确匹配关键术语
- ✅ **RRF 融合排序**：综合两种检索结果
- ✅ 自动返回最相关的 Top-K 个文档片段

### 💬 智能回答
- ✅ 接入 **DeepSeek API** 生成回答
- ✅ 流式输出（打字机效果）
- ✅ 基于检索内容的精准回答
- ✅ 防止幻觉（Hallucination）

### 📊 评估体系
- ✅ 自动化召回率测试
- ✅ 可自定义测试用例
- ✅ 量化检索效果

### 🖥️ 双界面支持
- 🎨 **Streamlit 界面**（app/app.py）：美观的 Web 界面
- ⚡ **FastAPI 接口**（app/api.py）：RESTful API

---

## 3️⃣ 核心算法详解

### 3.1 文档分块（Chunking）

**代码位置：** `src/RAGflow.py` → `load_markdown_folder()`

```python
# 按 Markdown 标题层级（#、##、###）切分文档
# 保留语义完整性，每个块包含一个完整的主题
content.split("\n# ")  → 一级标题切分
content.split("\n## ") → 二级标题切分
```

**作用：** 将长文档切分成语义完整的短文本块，便于检索和匹配。

---

### 3.2 向量语义检索（Vector Search）

**代码位置：** `src/RAGflow.py` → `hybrid_search()` 中的向量部分

```python
# 使用 BGE 模型将文本转换为向量（768维）
query_vec = self.embed_model.encode([query])[0]

# 计算余弦相似度
vec_scores = np.dot(self.chunk_vectors, query_vec) / (
    np.linalg.norm(self.chunk_vectors, axis=1) * np.linalg.norm(query_vec)
)
```

**所用模型：** `BAAI/bge-small-zh-v1.5`（国产开源中英文向量模型）

**作用：** 理解问题的语义含义，找出语义上最相关的文档片段。即使问题用词与文档不完全一致，也能准确匹配。

---

### 3.3 BM25 关键词检索（Keyword Search）

**代码位置：** `src/RAGflow.py` → `hybrid_search()` 中的 BM25 部分

```python
# 使用 jieba 分词
tokenized_query = jieba.lcut(query)

# BM25 词频-逆文档频率打分
bm25_scores = self.bm25_model.get_scores(tokenized_query)
```

**作用：** 基于关键词匹配的经典信息检索算法。擅长精确匹配专业术语、代码片段等。与向量检索形成互补。

---

### 3.4 RRF 融合排序（Reciprocal Rank Fusion）

**代码位置：** `src/RAGflow.py` → `hybrid_search()` 中的 RRF 部分

```python
# RRF 融合公式：score = 1 / (k + rank)
k = 60
for rank, idx in enumerate(vec_ranks):
    rrf_scores[idx] += 1.0 / (k + rank + 1)
for rank, idx in enumerate(bm25_ranks):
    rrf_scores[idx] += 1.0 / (k + rank + 1)
```

**作用：** 将向量检索和 BM25 检索的结果进行融合排序，综合两种算法的优势，提升检索准确率。

---

### 3.5 大模型生成回答（LLM Generation）

**代码位置：** `src/RAGflow.py` → `generate_answer()`

```python
# 构建包含检索结果的 Prompt
prompt = f"""请严格根据【参考资料】回答。
【参考资料】：{context}
【用户问题】：{query}
"""

# 调用 DeepSeek API 生成回答
response = self.llm_client.chat.completions.create(
    model="deepseek-chat",
    temperature=0.1,  # 低温度，确保回答严谨
    stream=True       # 流式输出
)
```

**作用：** 将检索到的文档片段作为上下文，让大模型基于这些信息生成精准、自然的回答。通过设置低温度（0.1）减少模型自由发挥，防止幻觉。

---

### 3.6 混合检索流程总览

```
用户输入问题
     │
     ▼
┌─────────────────────┐
│  ① jieba 分词       │
└─────────┬───────────┘
          │
     ┌────┴────┐
     ▼         ▼
┌────────┐ ┌────────┐
│ 向量   │ │ BM25   │
│ 检索   │ │ 检索   │
└───┬────┘ └───┬────┘
    │         │
    └────┬────┘
         ▼
┌─────────────────┐
│ ② RRF 融合排序  │
└────────┬────────┘
         ▼
┌─────────────────┐
│ ③ 返回 Top-K   │
│    个片段       │
└────────┬────────┘
         ▼
┌─────────────────┐
│ ④ 拼接 Context  │
│    + Prompt      │
└────────┬────────┘
         ▼
┌─────────────────┐
│ ⑤ DeepSeek      │
│   生成回答       │
└────────┬────────┘
         ▼
┌─────────────────┐
│ ⑥ 流式输出      │
│   返回给用户     │
└─────────────────┘
```

---

## 4️⃣ 快速开始

### 环境要求
- Python 3.8+
- 8GB+ RAM（推荐）

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行（二选一）

**Streamlit 界面（推荐）：**
```bash
python -m streamlit run app/app.py
```
然后浏览器访问显示的地址（默认 `http://localhost:8501`）

**FastAPI 接口：**
```bash
python app/api.py
```
然后浏览器访问 `http://localhost:8000`

### 爬取知识库数据
```bash
python src/crawler.py
```

### 评估召回率
```bash
python src/evaluate.py
```

---

## 5️⃣ 项目结构

```
GS/
├── README.md                  # 项目说明
├── requirements.txt           # 依赖包列表
├── .gitignore                 # Git 忽略文件
│
├── src/                       # 核心代码
│   ├── __init__.py
│   ├── RAGflow.py             # RAG 引擎（核心算法）
│   ├── crawler.py             # 网页爬虫
│   └── evaluate.py            # 召回率评估
│
├── app/                       # 应用界面
│   ├── __init__.py
│   ├── api.py                 # FastAPI 后端
│   ├── app.py                 # Streamlit 界面
│   └── chat.html              # 聊天前端
│
└── data/                      # 知识库数据（.md 文件）
    ├── fastapi_first_steps.md
    ├── fastapi_path_params.md
    ├── fastapi_query_params.md
    ├── fastapi_request_body.md
    └── fastapi_query_validations.md
```

---

## 6️⃣ 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| 🧠 **向量模型** | `BAAI/bge-small-zh-v1.5` | 中文语义向量模型 |
| 🔍 **关键词检索** | `BM25` + `jieba` | 经典信息检索 |
| 🔗 **融合算法** | `RRF`（倒数排序融合） | 多结果融合 |
| 🤖 **大语言模型** | `DeepSeek API` | 回答生成 |
| 🌐 **Web 框架** | `FastAPI` | RESTful API |
| 🎨 **前端界面** | `Streamlit` | 交互式网页 |
| 📦 **文档解析** | `PyMuPDF` / `markdownify` | PDF & HTML 解析 |

---
