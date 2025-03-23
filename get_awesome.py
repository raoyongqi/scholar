import os
import re
import requests
import markdown
from bs4 import BeautifulSoup
from urllib.parse import urlparse

# 创建 awesome 文件夹，如果不存在的话
if not os.path.exists('awesome'):
    os.makedirs('awesome')

# 读取Markdown文件内容
with open('readme.md', 'r', encoding='utf-8') as f:
    content = f.read()

# 将Markdown转换为HTML
html = markdown.markdown(content)

# 使用BeautifulSoup解析HTML并提取所有的URL
soup = BeautifulSoup(html, 'html.parser')
urls = [a['href'] for a in soup.find_all('a', href=True)]

# 遍历每个URL并下载页面内容
for url in urls:
    try:
        # 使用urlparse解析URL
        parsed_url = urlparse(url)
        
        # 提取路径部分，作为文件名的一部分
        path = parsed_url.path.lstrip('/')
        
        # 将路径中的斜杠（/）替换为破折号（-），以确保文件名有效
        file_name = path.replace('/', '-') + '.html'
        
        # 特殊处理 #，因为它不能用于文件名
        file_name = file_name.replace('#', '-')
        
        # 创建下载文件的完整路径（保存在 awesome 文件夹中）
        file_path = os.path.join('awesome', file_name)
        
        # 发送GET请求以获取URL的HTML内容
        response = requests.get(url)
        
        # 检查请求是否成功
        if response.status_code == 200:
            # 将网页内容保存到文件
            with open(file_path, 'w', encoding='utf-8') as f_out:
                f_out.write(response.text)
            print(f"Page '{url}' has been downloaded and saved as '{file_path}'.")
        else:
            print(f"Failed to retrieve the page '{url}'. Status code: {response.status_code}")
    
    except Exception as e:
        print(f"Error processing URL '{url}': {e}")
