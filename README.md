# 📚 GS - RAG 知识库问答系统

一个基于 FastAPI + Streamlit 的 RAG（检索增强生成）知识库系统。

## 功能特点
- ✅ 支持 Markdown/PDF 文档上传
- ✅ 混合检索（向量 + BM25）
- ✅ 三种对话模式：混合/仅知识库/自由对话
- ✅ Streamlit 和 FastAPI 双界面

## 快速开始

### 安装依赖
```bash
pip install -r requirements.txt
```

### 运行（二选一）

**Streamlit 界面：**
```bash
python -m streamlit run app/app.py
```

**FastAPI 界面：**
```bash
python app/api.py
```

### 爬取数据
```bash
python src/crawler.py
```

### 评估召回率
```bash
python src/evaluate.py
```

## 项目结构
```
GS/
├── README.md
├── requirements.txt
├── src/              # 核心代码
│   ├── RAGflow.py    # RAG 引擎
│   ├── crawler.py    # 爬虫
│   └── evaluate.py   # 评估
├── app/              # 应用界面
│   ├── api.py        # FastAPI
│   ├── app.py        # Streamlit
│   └── chat.html     # 前端
└── data/             # 知识库
```

## 技术栈
- **Embedding**: BAAI/bge-small-zh-v1.5
- **检索**: 向量检索 + BM25 + RRF 融合
- **LLM**: DeepSeek API
- **框架**: FastAPI, Streamlit
