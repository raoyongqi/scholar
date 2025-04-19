import json
import os
import re
import csv
from urllib.parse import urlparse
import pandas as pd
import markdown
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# 获取所有 .md 文件
awesome_files = [f for f in os.listdir('awesome') if f.endswith('.html')]


awesome_hosts = set()

for html_file in awesome_files:
    html_file_path = os.path.join('awesome', html_file)
    
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    urls = [a['href'] for a in soup.find_all('a', href=True)]

    for url in urls:
        try:
            parsed_url = urlparse(url)
            host = parsed_url.netloc  # 提取URL中的host
            if host:  # 确保host存在
                awesome_hosts.add(host)
        except Exception as e:
            print(f"Error parsing URL {url} in file {html_file}: {e}")

error_set = set()

with open('error_urls.txt', 'r') as file:

    for line in file:

        error_set.add(line.strip())

overlap = awesome_hosts.intersection(error_set)


awesome_hosts -= awesome_hosts & error_set