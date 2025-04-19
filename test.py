
import json
import os
import re
import csv
from urllib.parse import urlparse
import pandas as pd
import markdown
from bs4 import BeautifulSoup
from urllib.parse import urlparse


md_files = [f for f in os.listdir('md') if f.endswith('.md')]

md_hosts = set()

for md_file in md_files:

    md_file_path = os.path.join('md', md_file)
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    html = markdown.markdown(content)

    soup = BeautifulSoup(html, 'html.parser')

    # 提取所有链接
    urls = [a['href'] for a in soup.find_all('a', href=True)]

    # 提取每个URL的host并添加到集合
    for url in urls:
        try:
            parsed_url = urlparse(url)
            host = parsed_url.netloc  # 提取URL中的host
            if host:  # 确保host存在
                md_hosts.add(host)
        except Exception as e:
            print(f"Error parsing URL {url} in file {md_file}: {e}")
print(md_hosts)