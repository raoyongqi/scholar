import re
import json

# 读取原始的 JavaScript 文件内容
js_file_path = "background.js"  # 原 JS 文件路径
output_js_file_path = "google1.txt"  # 处理后的新文件路径

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
    try:
        import ast
        allowed_urls = ast.literal_eval(allowed_urls_str)
    except Exception as e:
        print(f"解析数组时出错: {e}")
        allowed_urls = []

    # 从列表中移除 google.com
    allowed_urls = [url for url in allowed_urls if 'google' not in url]

    # 格式化为每个 URL 保留引号和逗号
    formatted_urls = [f'"{url}",' for url in allowed_urls]

    # 将格式化后的 URL 按行写入新的文本文件
    with open(output_js_file_path, "w", encoding="utf-8") as f:
        for url in formatted_urls:
            f.write(f"{url}\n")

    print(f"处理后的 URL 已按行写入到 {output_js_file_path}")
else:
    print("未找到 allowedUrls 数组")
