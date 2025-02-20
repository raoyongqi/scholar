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
# 读取已有的 JS 文件
# 读取 .js 文件
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
    print(sorted_urls)


# 提取已有 allowedUrls 列表



if any(item == '' for item in sorted_urls):
    print("列表中有空字符串")
else:
    print("列表中没有空字符串")
# 合并新的 hosts 和已有的 allowedUrls
combined_hosts = list(set(hosts + sorted_urls))  # 合并并去重


# 保存为新的 JS 文件
js_content_new = f"const allowedUrls = {json.dumps(combined_hosts, ensure_ascii=False, indent=4)};"

with open('newbackground.js', 'w', encoding='utf-8') as js_file:
    js_file.write(js_content_new)

print("Combined and de-duplicated hosts saved to newAllowedUrls.js")
