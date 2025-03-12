import json
from urllib.parse import urlparse

import os
import json
from urllib.parse import urlparse

# 设置文件夹路径
folder_path = 'folder'

# 获取文件夹中所有 .json 文件
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# 存储所有 eprint_url 的主机部分
hosts = []

# 遍历所有 JSON 文件
for json_file in json_files:
    json_path = os.path.join(folder_path, json_file)
    
    # 读取 JSON 文件
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 提取 "eprint_url" 的主机部分
    eprint_urls = [entry.get('href', '') for entry in data]
    for url in eprint_urls:
        if url:
            host = urlparse(url).hostname
            # 去掉 www.
            host = host.replace('www.', '')
            hosts.append(host)

# 去重并排序
hosts = list(dict.fromkeys(hosts))  # 去除重复项
hosts.sort()  # 可选：按字母顺序排序


url_path = 'url'  # 需要读取的 TXT 文件夹路径

url_result = set() # 使用集合来去重

for filename in os.listdir(url_path):
    # 检查文件是否为 .txt 文件
    if filename.endswith('.txt'):
        file_path = os.path.join(url_path, filename)
        
        # 打开并读取 TXT 文件
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines):
                line = line.strip()  # 去除每行的首尾空白符
                url_result.add(line)  # 添加到集合中

# print(url_result)
with open('background.js','r', encoding='utf-8') as file:
    js_content = file.read()


import re
# 使用正则表达式匹配 'const allowedUrls = [' 后的数组内容
match = re.search(r'const\s+allowedUrls\s*=\s*\[([^\]]*)\];', js_content)

if match:
    # 提取数组中的 URL 并按 URL 长度排序
    urls = re.findall(r'"([^"]+)"', match.group(1))
    sorted_urls = sorted(urls, key=len)
    
    # 输出排序后的结果
    # print(sorted_urls)
import csv
import json

# 读取 CSV 文件
csv_file = "url/alexa1m_dataset.csv"
js_file = "output.js"

domains = []  # 存储符合条件的域名

with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 1:  # 确保该行有至少两列
            domain = row[1].strip()  # 去除首尾空格
            if ".org" in domain or ".edu" in domain:  # 只存储包含 .org 或 .edu 的域名
                domains.append(domain)


combined_hosts = list(set(list(hosts) + list(sorted_urls) + list(url_result)+domains))

js_content_new = f"const allowedUrls = {json.dumps(combined_hosts, ensure_ascii=False, indent=4)};"

with open('newbackground.js', 'w', encoding='utf-8') as js_file:

    js_file.write(js_content_new)

print("Combined and de-duplicated hosts saved to newbackground.js")
