# coding:utf-8

from os import path
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

if __name__ == '__main__':
    # 读取 CSV 文件
    df = pd.read_csv('url/alexa1m_dataset.csv')

    # 提取第二列（索引为 1 的列）
    second_column_data = df.iloc[:, 1]

    # 合并所有 URL 到一个大字符串
    text_data = " ".join(second_column_data.astype(str))

    # 生成词云（直接使用 WordCloud 的 generate 方法）
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        max_words=100,  # 可以根据需求调整最大词数
        colormap='viridis'  # 词云的颜色
    ).generate(text_data)  # 直接传入清理过的文本数据

    # 显示词云
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")  # 不显示坐标轴
    plt.show()

    # 保存词云图
    wordcloud.to_file("url_wordcloud.png")

    # 获取词云的词频字典
    word_frequencies = wordcloud.words_

    # 排序词频字典
    sorted_words = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

    # 打印词频
    for word, freq in sorted_words:
        print(f"{word}: {freq}")

    # 保存词频字典到文本文件
    with open("word_frequency.txt", "w", encoding="utf-8") as f:
        for word, freq in sorted_words:
            f.write(f"{word}: {freq}\n")

    print("\n词云图已生成并保存为 'url_wordcloud.png'，词频已保存到 'word_frequency.txt'。")
