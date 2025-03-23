import os
import markdown
from bs4 import BeautifulSoup
from urllib.parse import urlparse

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

# 保存不重复的host到txt文件
with open('unique_hosts.txt', 'w', encoding='utf-8') as f:
    for host in hosts:
        f.write(host + '\n')

print("Unique hosts have been saved to 'unique_hosts.txt'.")
