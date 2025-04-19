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

scholar_hosts_set= scholar_hosts_set - overlap 



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

org_or_edu_urls = set()  # 使用集合来去重

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
                    org_or_edu_urls.add(line)  # 添加到集合中


overlap = org_or_edu_urls.intersection(error_set)

if overlap:
    print("重叠元素:", overlap)
else:
    print("没有重叠元素")

org_or_edu_urls = org_or_edu_urls-overlap 

org_or_edu_urls -= org_or_edu_urls & error_set

#################
# 读取原始js内容
############################
# 读取 background.js 内容
def extract_and_sort_urls(js_content, variable_name):
    """
    提取并过滤特定 JS 内容中的 URL 列表。
    
    :param js_content: JS 内容的字符串
    :param variable_name: 变量名（如 'beginWithStar' 或 'beginWithoutStar'
    :return: 排序并过滤后的 URL 列表
    """
    match = re.search(rf'const\s+{variable_name}\s*=\s*\[([^\]]*)\];', js_content)
    
    if match:
        urls = re.findall(r'"([^"]+)"', match.group(1))
        sorted_urls = sorted(urls, key=len)
        filtered_urls = [url for url in sorted_urls if url not in ['ws', 'www',"localhost","127.0.0.1"]]
        return filtered_urls
    return []

with open('background.js', 'r', encoding='utf-8') as file:
    js_content = file.read()

begin_with_star_urls = extract_and_sort_urls(js_content, 'beginWithStar')
begin_without_star_urls = extract_and_sort_urls(js_content, 'beginWithoutStar')


#################
# 读取weekly-md内容，会存在无法访问情况
############################


# 获取所有 .md 文件
weekly_files = [f for f in os.listdir('weekly-master/docs') if f.endswith('.md')]

weekly_hosts = set()

# 遍历所有 .md 文件
for md_file in weekly_files:
    md_file_path = os.path.join('weekly-master/docs', md_file)
    
    with open(md_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    html = markdown.markdown(content)

    soup = BeautifulSoup(html, 'html.parser')

    # 提取所有链接
    urls = [a['href'] for a in soup.find_all('a', href=True)]

    for url in urls:
        try:
            parsed_url = urlparse(url)
            host = parsed_url.netloc  
            if host: 
                weekly_hosts.add(host)
        except Exception as e:
            print(f"Error parsing URL {url} in file {md_file}: {e}")

weekly_hosts -= weekly_hosts & error_set

####
#读取awesome
######

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

awesome_hosts -= awesome_hosts & error_set

#################
##读取求职内容
######################


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
####

#github上一些其他的*.md

###
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


########################
#这个是deepl翻译用的上的网址
########################
import re
from urllib.parse import urlparse

# 读取背景文件内容
with open('md/background.js', 'r', encoding='utf-8') as file:
    content = file.read()

# 正则表达式匹配所有以 https:// 开头的链接，直到域名部分
urls = re.findall(r'https://[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,3}', content)


deepl = [urlparse(url).netloc for url in urls]
########################
#数据包括谷歌学术+alexa1m_set+org_or_edu_urls+原本的origin_urls
########################


combined_hosts = list(set().union(
    scholar_hosts, alexa1m_set, org_or_edu_urls, begin_without_star_urls ,
    weekly_hosts, awesome_hosts, career_hosts, md_hosts,deepl
))

js_content_new = f"""
const beginWithStar = {json.dumps(begin_with_star_urls, ensure_ascii=False, indent=4)};
const beginWithoutStar = {json.dumps(combined_hosts, ensure_ascii=False, indent=4)};

const allowedUrls = beginWithStar.concat(beginWithoutStar);  // concat 方法 gpt认为效率更高
const blockedUrls = [
    "*://www.google.com/search*",
    ".*firefox.*",
    ".*firefox",
    "*://camo.githubusercontent.com/*" // 用于阻止包含“firefox”的 URL 的正则表达式
];

let sets = {{}};

browser.webRequest.onBeforeRequest.addListener((details) => {{
    browser.tabs.query({{ currentWindow: true, active: true }}).then(tabs => {{
        if (tabs[0]?.url) {{
            const tabUrl = tabs[0].url;
            const domain = new URL(details.url).host;
            if (domain.includes('127.0.0.1') || domain.includes('localhost')) {{
                return;
            }}

            sets[tabUrl] = sets[tabUrl] || new Set();
            sets[tabUrl].add(domain);

            async function isDomainInStoredList(tabUrl, domain) {{
                const result = await browser.storage.local.get();
                const keys = Object.keys(result).filter(key => !key.startsWith("about:"));

                for (const key of keys) {{
                    try {{
                        const keyHost = new URL(key).host;
                        if (keyHost === new URL(tabUrl).host && result[key]?.includes(domain)) {{
                            return true;
                        }}
                    }} catch (e) {{}} 
                }}

                return false;
            }}

            isDomainInStoredList(tabUrl, domain).then(isInList => {{
                if (!isInList) {{
                    browser.storage.local.get([tabUrl]).then(result => {{
                        const storedSet = new Set(result[tabUrl] || []);
                        storedSet.add(domain);
                        browser.storage.local.set({{ [tabUrl]: Array.from(storedSet) }});
                    }});
                }}
            }});
        }}
    }});
    const url = new URL(details.url);
    const host = url.hostname;

    const isBlocked = blockedUrls.some(pattern => {{
        const regex = new RegExp(pattern.replace(/\*/g, '.*'));
        return regex.test(details.url);
    }});

    if (isBlocked) {{
        console.log(`Blocked URL: {{details.url}}`);
        return {{ cancel: true }};
    }}

    const isAllowed = allowedUrls.some(pattern => {{
        if (pattern.startsWith("*.") && host.endsWith(pattern.slice(2))) {{
            return true;
        }}
        return host === pattern || host === 'www.' + pattern;
    }});

    if (!isAllowed) {{
        console.log(`Blocked URL: {{details.url}}`);
        return {{ cancel: true }};
    }}

    return {{ cancel: false }};
}},
{{ urls: ["*://*/*"] }},
["blocking"]
);

browser.runtime.onMessage.addListener((message, sender, sendResponse) => {{
    if (message === "LIST") {{
        sendResponse(sets);
    }}
}});

browser.runtime.onUninstall.addListener(() => {{
    console.log('扩展已卸载，正在清理数据...');
    browser.storage.local.clear()
        .then(() => console.log('数据已清空'))
        .catch((error) => console.error('清空数据时出错:', error));
}});
"""
# 将生成的新内容写入到文件中
with open('background1.js', 'w', encoding='utf-8') as js_file:
    js_file.write(js_content_new)

print("Combined and de-duplicated hosts saved to newbackground1.js")
