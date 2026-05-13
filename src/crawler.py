import os
import requests
from markdownify import markdownify as md
import re

def clean_markdown(text):
    """清理 Markdown 中的脏数据"""
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r'.*?跳转至\s*', '', text)
    text = re.sub(r'# 🌐 由 AI.*?(?=\n|$)', '', text)
    text = re.sub(r'本翻译由.*?(?=\n|$)', '', text)
    text = re.sub(r'回到页面顶部.*', '', text)
    return text.strip()

def fetch_doc_to_markdown(url, save_filename):
    print(f"正在抓取: {url}")
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
        response = requests.get(url, headers=headers, timeout=15)
        if response.status_code == 200:
            os.makedirs("data", exist_ok=True)
            markdown_content = md(response.text, heading_style="ATX")
            markdown_content = clean_markdown(markdown_content)
            filepath = os.path.join("data", save_filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(markdown_content)
            print(f"✅ 成功保存至: {filepath} ({len(markdown_content)} 字符)")
        else:
            print(f"❌ 抓取失败，状态码: {response.status_code}")
    except Exception as e:
        print(f"❌ 错误: {e}")

if __name__ == "__main__":
    urls_to_crawl = [
        ("https://fastapi.tiangolo.com/zh/tutorial/first-steps/", "fastapi_first_steps.md"),
        ("https://fastapi.tiangolo.com/zh/tutorial/path-params/", "fastapi_path_params.md"),
        ("https://fastapi.tiangolo.com/zh/tutorial/query-params/", "fastapi_query_params.md"),
        ("https://fastapi.tiangolo.com/zh/tutorial/body/", "fastapi_request_body.md"),
        ("https://fastapi.tiangolo.com/zh/tutorial/query-params-str-validations/", "fastapi_query_validations.md")
    ]
    for url, filename in urls_to_crawl:
        fetch_doc_to_markdown(url, filename)
