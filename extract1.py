import json
import os
import re
import csv
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

# 读取 TXT 文件夹路径
url_path = 'url'  

url_result = set()  # 使用集合来去重

for filename in os.listdir(url_path):
    # 检查文件是否为 .txt 文件
    if filename.endswith('.txt'):
        file_path = os.path.join(url_path, filename)
        
        # 打开并读取 TXT 文件
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                line = line.strip()  # 去除每行的首尾空白符
                if line:  # 确保不是空行
                    url_result.add(line)  # 添加到集合中

# 读取 background.js 内容
with open('background.js','r', encoding='utf-8') as file:
    js_content = file.read()

# 使用正则表达式匹配 'const allowedUrls = [' 后的数组内容
match = re.search(r'const\s+allowedUrls\s*=\s*\[([^\]]*)\];', js_content)

if match:
    # 提取数组中的 URL 并按 URL 长度排序
    urls = re.findall(r'"([^"]+)"', match.group(1))
    sorted_urls = sorted(urls, key=len)
    
# 读取 CSV 文件并处理
csv_file = "url/alexa1m_dataset.csv"
domains = []  # 存储符合条件的域名

with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 1:  # 确保该行有至少两列
            domain = row[1].strip()  # 去除首尾空格
            # 只存储包含 "vue" 或 "react" 且不包含 "pron" 的域名
            if ("vue" in domain or "react" in domain) and "pron" not in domain:
                domains.append(domain)

# 合并所有结果，并去重
combined_hosts = list(set(hosts + sorted_urls + list(url_result) + domains))

# 生成新的 background.js 内容
js_content_new = f"""
const allowedUrls = {json.dumps(combined_hosts, ensure_ascii=False, indent=4)};
const blockedUrls = [
  "*://www.google.com/search*",
  ".*firefox.*",
  ".*firefox",
  "*://camo.githubusercontent.com/*" // 用于阻止包含“firefox”的 URL 的正则表达式
];

const onBeforeRequest = (details) => {{
  const url = new URL(details.url);
  const host = url.hostname;

  // 检查是否在被阻止的 URL 列表中
  const isBlocked = blockedUrls.some(pattern => {{
    const regex = new RegExp(pattern.replace(/\*/g, '.*'));
    return regex.test(details.url); // 检查整个 URL
  }});

  if (isBlocked) {{
    console.log(`Blocked URL: ${{details.url}}`);
    return {{ cancel: true }}; // 拦截请求
  }}

  // 检查是否在允许的 URL 列表中
  const isAllowed = allowedUrls.some(pattern => {{
    // 处理通配符
    if (pattern.startsWith("*.") && host.endsWith(pattern.slice(2))) {{
      return true;
    }}
    return host === pattern || host === 'www.' + pattern; // 检查主机名
  }});

  if (!isAllowed) {{
    console.log(`Blocked URL: ${{details.url}}`);
    return {{ cancel: true }}; // 拦截请求
  }}

  return {{ cancel: false }}; // 允许请求
}};

// 监听所有请求
browser.webRequest.onBeforeRequest.addListener(
  onBeforeRequest,
  {{ urls: ["<all_urls>"] }},
  ["blocking"]
);
"""

# 将生成的新内容写入到文件中
with open('newbackground.js', 'w', encoding='utf-8') as js_file:
    js_file.write(js_content_new)

print("Combined and de-duplicated hosts saved to newbackground.js")
