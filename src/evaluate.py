from RAGflow import MiniRAGFlow

def run_evaluation():
    rag = MiniRAGFlow()
    rag.load_markdown_folder("data")
    rag.build_index()
    
    # 构建测试集：使用数据中实际存在的关键词
    test_set = [
        {"query": "FastAPI 是基于什么标准的？", "expected_keyword": "OpenAPI"},
        {"query": "怎么定义路径参数？", "expected_keyword": "{item_id}"},
        {"query": "FastAPI 怎么启动服务？", "expected_keyword": "fastapi dev"},
        {"query": "路径参数怎么声明类型？", "expected_keyword": "int"},
        {"query": "查询参数怎么设置默认值？", "expected_keyword": "默认值"},
        {"query": "Pydantic 模型怎么定义？", "expected_keyword": "BaseModel"},
    ]
    
    hits = 0
    total = len(test_set)
    
    print("开始自动化测试 RAG 召回率...\n")
    for item in test_set:
        query = item["query"]
        expected = item["expected_keyword"]
        
        results = rag.hybrid_search(query, top_k=3)
        
        hit = any(expected in doc for doc in results)
        if hit:
            hits += 1
            print(f"✅ 命中 | 问题: {query}")
        else:
            print(f"❌ 丢失 | 问题: {query}")
            # 显示实际检索到的内容，方便调试
            print(f"   检索到的片段: {results[0][:100]}...")
            
    recall_rate = (hits / total) * 100
    print(f"\n📊 测试完成！Top-3 召回率 (Hit Rate): {recall_rate:.1f}%")

if __name__ == "__main__":
    run_evaluation()
