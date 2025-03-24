import os


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

# 打开文件并逐行读取
overlap = url_result.intersection(error_set)

if overlap:
    print("重叠元素:", overlap)
else:
    print("没有重叠元素")

url_result= url_result-overlap 