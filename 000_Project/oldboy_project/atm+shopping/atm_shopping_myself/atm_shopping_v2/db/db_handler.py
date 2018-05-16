import os
from conf import setting
import json

def select(username):
    path = os.path.join(setting.BASE_DB,'%s.json' % username )
    if os.path.exists(path):
        with open(path,'r',encoding='utf-8') as f:
            return json.load(f)
    else:
        return

def save(user_dic):
    path = os.path.join(setting.BASE_DB,'%s.json' % user_dic['username'])
    with open(path,'w',encoding='utf-8') as f:
        json.dump(user_dic,f)
        f.flush()   # 刷新缓存，立刻写入文件