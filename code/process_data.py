'''
处理原始文件
一：去掉重复的评论信息，保存在UNIQUE_COMMENT_FILE
二：对评论分词，保存到SEG_COMMENT_FILE，分词后文件去停用词保存到FINISH_COMMENT_FILE
(由于在情感分析，有一些标点符号等停用词可能对分类有作用，所以去停用词和不去停用词的预料都会进行训练测试)
ps: 初步观察不去停用词的效果好一些
三：将SEG_COMMENT_FILE，和FINISH_COMMENT_FILE分别写入DATAFRAME之中，保存到
'''

from helpers_comment import *
from time import time
import pandas as pd
import re
import jieba

class Dataprocess:                              # 数据处理的类
    def __init__(self):
        pass

    @staticmethod
    def unique_comments(raw_file, unique_file):  # 评论去重
        # 获得原始数据
        with open(raw_file, "r", encoding="utf-8") as file:
            raw_list = file.read().splitlines()  # 将原始数据的所有行储存在列表中，文件总量较小可以一次性读取
        print("原始数据一共有{}条".format(len(raw_list)))
        # 评论去重并写入文件
        unique_set = set(raw_list)               # 获取去重后的数据
        with open(unique_file, "w", encoding="utf-8") as file:
            for info in unique_set:
                file.writelines(info + "\n")
        print("去重后的数据一共有{}条".format(len(unique_set)))

    @staticmethod
    def seg_comments(unique_file, seg_file):                # 评论分词
        # 获取原始数据
        with open(unique_file, "r", encoding="utf-8") as file:
            unique_list = file.read().splitlines()          # 将去重后评论的所有行储存在列表中, 文件总量较小可以一次性读取
        # 评论分词后写入文件
        with open(seg_file, "w", encoding="utf-8") as file:
            print("正在进行分词操作》》》》"); st = time()
            for info in unique_list:
                score = info.split()[0]                     # 获取评分
                comment = info.replace(score, "")           # 获取评论
                comment = re.sub(r"\s", "", comment)        # 去掉空白符
                comment = " ".join(jieba.cut(comment))      # 获取分词后的评论
                file.writelines(score + " " + comment + "\n")
            print("已经对评论进行分词，用时：{:.3f}s!!!!".format(time()-st))

    @staticmethod
    def finish_comments(seg_file, stopwords_file, finish_file):              # 对分词后文件去掉停用词
        with open(seg_file, "r", encoding="utf-8") as file:
            seg_list = file.read().splitlines()             # 将分词后评论的所有行储存在列表中，文件总量较小可以一次性读取
        with open(stopwords_file, "r", encoding="utf-8") as file:
            stopwords_list = file.read().splitlines()       # 生成停用词列表
        with open(finish_file, "w", encoding="utf-8") as file:
            print("正在去停用词》》》》"); st = time()
            for info in seg_list:
                score = info.split()[0]                     # 获取评分
                comment = info.replace(score, "")           # 获取评论
                new_comment = ""                            # 初始化去完停用词后的评论
                for word in comment.split():                # 去停用词
                    if word not in stopwords_list:
                        new_comment += word + " "
                file.writelines(score + " " + new_comment + "\n")
            print("已经对分词后评论去停用词，用时：{:.3f}s!!!!".format(time() - st))

    @staticmethod
    def txt2csv(txt_file, csv_file):                                    # 使用txt文件构建DataFrame，然后写入csv
        # DataFrame的内容包括：labels(评论标签), lenths(评论的单词数), contents(评论内容)
        with open(txt_file, "r", encoding="utf-8") as file:
            info_list = file.read().splitlines()                        # 获得原始文件每一行信息组成的列表
            labels_list = []; lenths_list = []; contents_list = []      # 初始化labels(评论标签), lenths(评论的单词数), contents(评论内容)
            for info in info_list:
                label = info.split()[0]                                 # 获取标签
                content = info.replace(label, "").strip()               # 获取评论
                lenth = len(content.split())                            # 获取评论长度
                labels_list.append(label)
                lenths_list.append(lenth)
                contents_list.append(content)
        # 生成DataFrame，并写入csv文件
        df = pd.DataFrame({"labels":labels_list,"lenths":lenths_list,"contents":contents_list})
        df.to_csv(csv_file)
        print("已经生成{}文件!!!!".format(csv_file.split("/")[-1]))

    @staticmethod
    def statistics_csv(csv_file):                                        # 生成评论的统计信息
        df = pd.read_csv(csv_file)
        print("df.info如下：")
        print(df.info())
        print("df.describe如下：")
        print(df.describe())



if __name__ == '__main__':
    # 进行数据预处理
    # Dataprocess.unique_comments(RAW_DATA_FILE, UNIQUE_COMMENT_FILE)                         # 评论去重
    # Dataprocess.seg_comments(UNIQUE_COMMENT_FILE, SEG_COMMENT_FILE)                         # 产生分词后文件
    # Dataprocess.finish_comments(SEG_COMMENT_FILE, STOPWORDS_FILE, FINISH_COMMENT_FILE)      # 对分词后文件去停用词
    # 生成DataFrame并保存
    #Dataprocess.txt2csv(SEG_COMMENT_FILE, SEG_CSV)                                           # 分词文件对应的csv文件
    #Dataprocess.txt2csv(FINISH_COMMENT_FILE, FINISH_CSV)                                     # 去停用词文件的csv文件
    # 生成统计信息
    Dataprocess.statistics_csv(SEG_CSV)























