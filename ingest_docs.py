import os
from pathlib import Path
import markdown
from bs4 import BeautifulSoup

def md_to_text(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        md_content = f.read()
        html = markdown.markdown(md_content)
        soup = BeautifulSoup(html, 'html.parser')
        return soup.get_text()

def collect_docs(docs_dir):
    all_docs = []
    for md_file in Path(docs_dir).rglob("*.md"):
        text = md_to_text(md_file)
        all_docs.append({
            "path": str(md_file),
            "text": text
        })
    return all_docs

if __name__ == "__main__":
    docs_path = "data/langgraph-docs"
    documents = collect_docs(docs_path)
    print(f"✅ Loaded {len(documents)} documentation files.")
    
    # Save all the text into one file
    with open("all_docs.txt", "w", encoding="utf-8") as f:
        for doc in documents:
            f.write(f"### {doc['path']}\n{doc['text']}\n\n")
