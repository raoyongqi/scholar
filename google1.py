import re
import json

# 读取原始的 JavaScript 文件内容
js_file_path = "background.js"  # 原 JS 文件路径
output_js_file_path = "google1.js"  # 处理后的新 JS 文件路径

# 读取 JS 文件
with open(js_file_path, "r", encoding="utf-8") as f:
    js_content = f.read()

# 使用正则表达式提取 allowedUrls 数组
match = re.search(r'const allowedUrls = (\[.*?\]);', js_content, re.DOTALL)
if match:
    # 提取数组字符串并处理
    allowed_urls_str = match.group(1)
    
    # 去掉数组中每个 URL 的星号（*）
    allowed_urls_str = re.sub(r'\*', '', allowed_urls_str)
    
    # 将处理后的字符串转换为 Python 列表
    allowed_urls = json.loads(allowed_urls_str)

    # 从列表中移除 google.com
    print(allowed_urls)
    allowed_urls = [url for url in allowed_urls if 'google' not in url]

    # 将处理后的数组写回新的 JS 文件
    new_js_content = re.sub(r'const allowedUrls = \[.*?\];', f'const allowedUrls = {json.dumps(allowed_urls, indent=2)};', js_content, flags=re.DOTALL)

    # 保存处理后的内容到新的 JS 文件
    with open(output_js_file_path, "w", encoding="utf-8") as f:
        f.write(new_js_content)

    print(f"处理后的 JavaScript 文件已保存为 {output_js_file_path}")
else:
    print("未找到 allowedUrls 数组")
