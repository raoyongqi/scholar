import json
import os
import re
import csv
from urllib.parse import urlparse
folder_path = 'folder'

json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

folder_hosts = []

for json_file in json_files:
    json_path = os.path.join(folder_path, json_file)
    
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    # 提取 "eprint_url" 的主机部分
    eprint_urls = [entry.get('href', '') for entry in data]
    for url in eprint_urls:
        if url:
            host = urlparse(url).hostname
            # 去掉 www.
            host = host.replace('www.', '')
            folder_hosts.append(host)


folder_hosts_set = set(folder_hosts)
# 定义一个空集合
error_set = set()
with open('error_urls.txt', 'r') as file:
    for line in file:
        # 去掉行末的换行符并将每行添加到集合中
        error_set.add(line.strip())

overlap = folder_hosts_set.intersection(error_set)
folder_hosts_set= folder_hosts_set-overlap 
if overlap:
    print("重叠元素:", overlap)
else:
    print("没有重叠元素")

print("过滤后的第二列集合数据已保存为 filtered_second_column_set.txt")
