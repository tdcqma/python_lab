import os,sys
from core import src

# 项目根目录
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 将根目录加入环境变量
sys.path.append(BASE_DIR)

if __name__ == '__main__':
    src.run()