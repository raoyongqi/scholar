import os
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# 获取所有 .html 文件
html_files = [f for f in os.listdir('awesome') if f.endswith('.html')]

# 创建一个集合来存储不重复的主机
awesome_hosts = set()

# 遍历所有 .html 文件
for html_file in html_files:
    html_file_path = os.path.join('awesome', html_file)
    
    # 读取每个HTML文件内容
    with open(html_file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 使用BeautifulSoup解析HTML
    soup = BeautifulSoup(content, 'html.parser')

    # 提取所有链接
    urls = [a['href'] for a in soup.find_all('a', href=True)]

    # 提取每个URL的host并添加到集合
    for url in urls:
        try:
            parsed_url = urlparse(url)
            host = parsed_url.netloc  # 提取URL中的host
            if host:  # 确保host存在
                awesome_hosts.add(host)
        except Exception as e:
            print(f"Error parsing URL {url} in file {html_file}: {e}")

# 保存不重复的host到txt文件
with open('unique_hosts1.txt', 'w', encoding='utf-8') as f:
    for host in awesome_hosts:
        f.write(host + '\n')

print("Unique hosts have been saved to 'unique_hosts.txt'.")
