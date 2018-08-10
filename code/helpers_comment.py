# 保存文件路径，参数及常用函数
import os
BASE_DIR = os.path.dirname(os.getcwd())                       # 文件基础路径
# data文件夹下，保存了停用词文件
STOPWORDS_FILE = os.path.join(BASE_DIR, "data", "stopwords.txt")
# data/raw_data文件夹，储存原始文件
RAW_DATA_FILE = os.path.join(BASE_DIR, "data/raw_data", "raw_data.txt")
# data/process_data文件夹，储存处理过后的文件夹
UNIQUE_COMMENT_FILE = os.path.join(BASE_DIR, "data/process_data", "unique_comment.txt")    # 去重后的文件
SEG_COMMENT_FILE = os.path.join(BASE_DIR, "data/process_data", "seg_comment.txt")          # 分完词的文件
FINISH_COMMENT_FILE = os.path.join(BASE_DIR, "data/process_data", "finish_comment.txt")    # 分完词并去除停用词的文件
SEG_CSV = os.path.join(BASE_DIR, "data/process_data", "seg.csv")          # 分完词的CSV文件
FINISH_CSV = os.path.join(BASE_DIR, "data/process_data", "finish.csv")    # 分完词并去除停用词的CSV文件

