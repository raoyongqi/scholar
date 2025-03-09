import re
import os
import json
import ast

# 设置文件路径
js_file_path = "background.js"  # 原 JS 文件路径
folder_path = 'url'  # 需要读取的 TXT 文件夹路径

output_js_file_path = "google1.txt"  # 处理后的新文件路径
output_path = 'google1.txt'  # 合并后的结果输出文件路径

# 读取 JS 文件并提取 allowedUrls 数组
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
        allowed_urls = ast.literal_eval(allowed_urls_str)
    except Exception as e:
        print(f"解析数组时出错: {e}")
        allowed_urls = []

    # 从列表中移除包含 google.com 的 URL
    allowed_urls = [url for url in allowed_urls if 'google' not in url]

    formatted_urls = [f'"{url}",' for url in allowed_urls]


# 用于保存合并后的结果
merged_result = []

# 遍历文件夹中的所有 TXT 文件
for filename in os.listdir(folder_path):
    # 检查文件是否为 .txt 文件
    if filename.endswith('.txt'):
        file_path = os.path.join(folder_path, filename)
        
        # 打开并读取 TXT 文件
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 处理每一行
        for i, line in enumerate(lines):
            line = line.strip()  # 去除每行的首尾空白符
            quoted_line = f'"{line}"'  # 给每行加上引号

            # 如果不是最后一行，添加逗号
            if i != len(lines) - 1:
                quoted_line += ','

            merged_result.append(quoted_line)

# 合并处理后的内容
merged_text = '\n'.join(merged_result+formatted_urls)


# 如果需要保存到新的文件
with open(output_path, 'w', encoding='utf-8') as output_file:
    output_file.write(merged_text)

print(f"合并后的结果已保存到 {output_path}")
