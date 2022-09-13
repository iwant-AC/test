# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import os
import pandas as pd
import collections
import jieba
jieba.setLogLevel(jieba.logging.INFO)
import numpy as np
import wordcloud
import matplotlib.pyplot as plt

#读入弹幕文件和停用词
data = pd.read_csv("E:\作业\程设\第1周\danmuku.csv", encoding='utf-8', usecols=['content'])
data = data.loc[:,'content']
data = data.tolist()
stop = open('E:\作业\程设\第1周\stopwords_list.txt', 'r', encoding='utf-8')
stopWord = stop.read().split("\n")
jieba.load_userdict('E:\作业\程设\第1周\stopwords_list.txt')

#弹幕分词并统计词频
wlists = []
unsorted_d={}
for row in data:
    ls = jieba.cut(row, cut_all=False)
    for key in ls:
        if not (key in stopWord) and key !='️' and key !='∀':
            if key in unsorted_d:
                unsorted_d[key] += 1
            else:
                unsorted_d[key] = 1
    wlists.append(ls)

#词频排序并删除低频次
sorted_d = collections.OrderedDict(sorted(unsorted_d.items(), key=lambda dc:dc[1], reverse = True))
for key in list(sorted_d):
    if sorted_d[key]<=5 :
        del sorted_d[key]

#将词频输出为txt文件
s = str(sorted_d)
f1 = open('E:\作业\程设\第1周\词频.txt','w',encoding='utf-8')
sorted_d.encoding='utf-8'
f1.writelines(s)
f1.close()

#绘制词云图
w = wordcloud.WordCloud(font_path='./fonts/simhei.ttf')
picture = {}
for i, (k, v) in enumerate(sorted_d.items()):
    if i in range(0, 50):
        picture[k] = v
w = wordcloud.WordCloud(font_path='simhei.ttf',background_color="white",width =4000,height= 2000,margin= 10 ).fit_words(picture)
plt.imshow(w)
w.to_file('E:\作业\程设\第1周\词云图.png')
plt.show()

