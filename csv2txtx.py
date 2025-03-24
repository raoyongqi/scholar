import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('url/alexa1m_dataset.csv')

# 提取第二列（索引为 1 的列），并将其转换为集合（去除重复的元素）
second_column_set = set(df.iloc[:, 1])

# 过滤包含 "react"、"vue"、".ai" 或 "journey" 的元素
# 过滤包含 "react"、"vue"、".ai" 或 "journey" 的元素，并确保特定域名在字符串结尾
filtered_set = {item for item in second_column_set if 
                'react' in str(item).lower() or
                'vue' in str(item).lower() or
                '.ai' in str(item).lower() and str(item).lower().endswith('.ai') or
                'journey' in str(item).lower() or
                'github.io' in str(item).lower() and str(item).lower().endswith('github.io') or
                'blogspot.com' in str(item).lower() and str(item).lower().endswith('blogspot.com') or
                'myshopify.com' in str(item).lower() and str(item).lower().endswith('myshopify.com') or
                'wordpress.com' in str(item).lower() and str(item).lower().endswith('wordpress.com') or
                'livejournal.com' in str(item).lower() and str(item).lower().endswith('livejournal.com')}


# 将过滤后的集合保存为 txt 文件
with open('filtered_second_column_set.txt', 'w') as file:
    # 将过滤后的集合的每个元素逐行写入文件
    for item in filtered_set:
        file.write(str(item) + '\n')

print("过滤后的第二列集合数据已保存为 filtered_second_column_set.txt")
