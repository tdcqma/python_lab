import os
from conf import setting
import json

def select(name):
    path =os.path.join(setting.base_db,'%s.json'%name)
    if os.path.exists(path):
        with open(path,'r',encoding='utf-8') as f:
            return json.load(f)

    else:
        return


def save(user_dic):
    path =os.path.join(setting.base_db,'%s.json'%user_dic['name'])

    with open(path,'w',encoding='utf-8') as f:
         json.dump(user_dic,f)
         f.flush()

