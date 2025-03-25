import json
import os
import re
import csv
from urllib.parse import urlparse
import pandas as pd
import markdown
from bs4 import BeautifulSoup
from urllib.parse import urlparse
###
# 来自谷歌学术的url会存在不能访问的情况

##
folder_path = 'folder'

json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

scholar_hosts = []

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
            scholar_hosts.append(host)


scholar_hosts_set = set(scholar_hosts)
# 定义一个空集合
error_set = set()
with open('error_urls.txt', 'r') as file:
    for line in file:
        # 去掉行末的换行符并将每行添加到集合中
        error_set.add(line.strip())

overlap = scholar_hosts_set.intersection(error_set)
scholar_hosts_set= scholar_hosts_set-overlap 



#####
#alexa1m_dataset 基本不存在不能访问的url ，暂时省去取差集的步骤
######
# 读取 CSV 文件
df = pd.read_csv('url/alexa1m_dataset.csv')

# 提取第二列（索引为 1 的列），并将其转换为集合（去除重复的元素）
alexa1m_column_set = set(df.iloc[:, 1])

# 过滤包含 "react"、"vue"、".ai" 或 "journey" 的元素
alexa1m_set = set({item for item in alexa1m_column_set if 
                'react' in str(item).lower() or
                'vue' in str(item).lower() or
                '.ai' in str(item).lower() and str(item).lower().endswith('.ai') or
                'journey' in str(item).lower() or
                'github.io' in str(item).lower() and str(item).lower().endswith('github.io') or
                'blogspot.com' in str(item).lower() and str(item).lower().endswith('blogspot.com') or
                'myshopify.com' in str(item).lower() and str(item).lower().endswith('myshopify.com') or
                'wordpress.com' in str(item).lower() and str(item).lower().endswith('wordpress.com') or
                'livejournal.com' in str(item).lower() and str(item).lower().endswith('livejournal.com') or
                'readthedocs.io' in str(item).lower() and str(item).lower().endswith('readthedocs.io')}
)



#################
# 处理 org_or_edu_urls.txt
############################

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

# 定义一个空集合
error_set = set()
with open('error_urls.txt', 'r') as file:
    for line in file:
        # 去掉行末的换行符并将每行添加到集合中
        error_set.add(line.strip())

overlap = url_result.intersection(error_set)

if overlap:
    print("重叠元素:", overlap)
else:
    print("没有重叠元素")

url_result = url_result-overlap 
#################
# 处理 org_or_edu_urls.txt
############################
# 读取 background.js 内容
with open('background.js','r', encoding='utf-8') as file:
    js_content = file.read()

# 使用正则表达式匹配 'const allowedUrls = [' 后的数组内容
match = re.search(r'const\s+allowedUrls\s*=\s*\[([^\]]*)\];', js_content)

if match:
    # 提取数组中的 URL 并按 URL 长度排序
    
    origin_urls = re.findall(r'"([^"]+)"', match.group(1))
    
# 读取 CSV 文件并处理
csv_file = "url/alexa1m_dataset.csv"
domains = []  # 存储符合条件的域名

with open(csv_file, "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) > 1:  # 确保该行有至少两列
            domain = row[1].strip()  # 去除首尾空格
            # 只存储包含 "vue" 或 "react" 且不包含 "pron" 的域名
            if ("vue" in domain or "react" in domain or "spark" in domain or "analyse" in domain) and "pron" not in domain:
                domains.append(domain)


# 获取所有 .md 文件
weekly_files = [f for f in os.listdir('weekly-master/docs') if f.endswith('.md')]

# 创建一个集合来存储不重复的主机
weekly_hosts = set()

# 遍历所有 .md 文件
for md_file in weekly_files:
    md_file_path = os.path.join('weekly-master/docs', md_file)
    
    # 读取每个Markdown文件内容
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 将Markdown转换为HTML
    html = markdown.markdown(content)

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(html, 'html.parser')

    # 提取所有链接
    urls = [a['href'] for a in soup.find_all('a', href=True)]

    # 提取每个URL的host并添加到集合
    for url in urls:
        try:
            parsed_url = urlparse(url)
            host = parsed_url.netloc  # 提取URL中的host
            if host:  # 确保host存在
                weekly_hosts.add(host)
        except Exception as e:
            print(f"Error parsing URL {url} in file {md_file}: {e}")
awesome_files = [f for f in os.listdir('awesome') if f.endswith('.html')]

# 创建一个集合来存储不重复的主机

awesome_hosts = set()

# 遍历所有 .html 文件
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

career_files = [f for f in os.listdir('career') if f.endswith('.md')]

career_hosts = set()

for md_file in career_files:
    md_file_path = os.path.join('career', md_file)
    
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
                career_hosts.add(host)
        except Exception as e:
            print(f"Error parsing URL {url} in file {md_file}: {e}")


########################
#数据包括谷歌学术+原本的url
########################
combined_hosts = list(set(scholar_hosts + sorted_urls + list(url_result) + domains+list(weekly_hosts)+list(awesome_hosts)+list(career_hosts)))

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
