import pandas as pd

# 读取 CSV 文件
df = pd.read_csv('url/alexa1m_dataset.csv')

# 提取第二列（索引为 1 的列），并将其转换为集合（去除重复的元素）
second_column_set = set(df.iloc[:, 1])
alexa1m_set = {
    item for item in second_column_set if (
        "react" in str(item).lower() or
        "vue" in str(item).lower() or
        (".ai" in str(item).lower() and str(item).lower().endswith(".ai")) or
        "journey" in str(item).lower() or
        ("github.io" in str(item).lower() and str(item).lower().endswith("github.io")) or
        ("blogspot.com" in str(item).lower() and str(item).lower().endswith("blogspot.com")) or
        ("myshopify.com" in str(item).lower() and str(item).lower().endswith("myshopify.com")) or
        ("wordpress.com" in str(item).lower() and str(item).lower().endswith("wordpress.com")) or
        ("livejournal.com" in str(item).lower() and str(item).lower().endswith("livejournal.com")) or
        ("readthedocs.io" in str(item).lower() and str(item).lower().endswith("readthedocs.io"))
    )
}

alexa1m_list = [domain for domain in alexa1m_set if "pron" not in domain]


# 定义一个空集合
error_set = set()
with open('error_urls.txt', 'r') as file:
    for line in file:
        # 去掉行末的换行符并将每行添加到集合中
        error_set.add(line.strip())

overlap = alexa1m_set.intersection(error_set)

if overlap:
    print("重叠元素:", overlap)
else:
    print("没有重叠元素")

print("过滤后的第二列集合数据已保存为 filtered_second_column_set.txt")
