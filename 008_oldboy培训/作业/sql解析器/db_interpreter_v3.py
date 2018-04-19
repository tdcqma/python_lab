import re
import datetime
import os

"""
           >>>以下代码在未参考任何资料的情况下独自成，硬编码部分巨多...<<<
v2:
180419：增加退出功能
        将函数体部分放置到while循环外
        修复删除与增加记录后数据库多出空行的bug
        添加简单的异常捕捉及输错信息提示
        增加'q'退出的退出功能

v1:
180418：添加while，保持命令可持续输入
        部分功能修复

v0：
180417：基本框架完成

已测试SQL查询语句：
select name,age from staff_table where age > 2(支持任意年龄)
select name,age,phone,enroll_date from staff_table where age > 2
select * from staff_table where dept="IT"
select * from staff_table where dept="hr"
select * from staff_table where dept="sales"
select * from staff_table where enroll_date like "2013"
select * from staff_table where enroll_date like "2018"
insert into staff_table(name,age,phone,dept) values('wxx001',73,13188888889,'hr')
insert into staff_table(name,age,phone,dept) values('洪七公',84,18200000000,'sales')
delete from staff_table where staff_id = '3'
UPDATE staff_table SET dept="Market" WHERE dept = "IT"
UPDATE staff_table SET dept="IT" WHERE dept = "Market"
UPDATE staff_table SET dept="TEC" WHERE dept = "sales"

"""

# 将用户输入的任意指定字段转为数据表中列表的索引
def userCol_to_dbCol(list):
    db_column_dic = {'db_staff_id': 0, 'db_name': 1, 'db_age': 2, 'db_phone': 3, 'db_dept': 4, 'db_enroll_date': 5}
    col_list = []
    for line in list:
        for k, v in db_column_dic.items():
            if line in k:
                key = v
                col_list.append(key)
            else:
                pass
    return col_list


# 从文件中读取员工信息内容到staff_table列表里
emp_list_1 = []
with open(r'employee_db.txt', mode='r', encoding='utf-8') as f:
    for line in f:
        emp_list_1.append(line.strip('\n'))
# 将str类型的员工信息emp_list_1转换添加到emp_list_2中，类型为双层列表
staff_table = []
for line in emp_list_1:
    staff_table.append(line.split(','))

# 定义年龄筛选函数
def age(list, age):
    age_list = []
    for line in list:
        if int(line[2]) > age:
            age_list.append(line)
    return age_list

def dep_find(list, dep):
    it_dep_list = []
    hr_dep_list = []
    sales_dep_list = []
    market_dep_list = []
    for line in list:
        if line[4] == 'IT':
            it_dep_list.append(line)
        elif line[4] == 'HR':
            hr_dep_list.append(line)
        elif line[4].capitalize() == 'Sales':
            sales_dep_list.append(line)
        elif line[4].upper() == 'MARKET':
            market_dep_list.append(line)

    if dep.upper() == 'IT':
        return it_dep_list
    elif dep.upper() == 'HR':
        return hr_dep_list
    elif dep.upper() == 'SALES':
        return sales_dep_list
    elif dep.upper() == 'MARKET':
        return market_dep_list


# 定义enroll_date模糊筛选函数
def enroll_find(list, enr_date):
    enroll_date_list = []
    for line in list:
        if enr_date in line[5]:
            enroll_date_list.append(line)
    return enroll_date_list

while True:
    user_input = input('>>SQL: ').strip()
    # 简单的用户输入确认
    if user_input == 'q':
        print('欢迎再次使用。')
        exit()

    try:
        sql_info = user_input.split()
        sql_action = sql_info[0]
        sql_column = sql_info[1]
        sql_table = sql_info[3]
        sql_limit = sql_info[4:]
    except IndexError as err:
        print('sql语句不合法，请重新输入。\n报错信息：%s\n' % err)
        continue

    if sql_action.upper() not in ['SELECT','INSERT','DELETE','UPDATE']:
        print('sql语句不合法，请重新输入。\n')

    # 解析SELECT数据语句
    if sql_action.upper() == 'SELECT':
        if sql_column == '*':  #搜索所有字段的情况下
            for line in sql_limit:
                if '=' in line: # 判断条件符号是否包由"="组成
                    sql_res = []
                    s = re.findall(r'[^=]+', user_input)
                    dept_select_colu = s[1].strip().strip('\',\"')

                    if dept_select_colu.upper() == 'IT':
                        sql_res = dep_find(staff_table,dept_select_colu)
                    elif dept_select_colu.upper() == 'HR':
                        sql_res = dep_find(staff_table,dept_select_colu)
                    elif dept_select_colu.upper() == 'SALES':
                        sql_res = dep_find(staff_table,dept_select_colu)
                    elif dept_select_colu.upper() == 'MARKET':
                        sql_res = dep_find(staff_table,dept_select_colu)

                    res = ''
                    for line in sql_res:
                        for x in line:
                            res += (x + '\t')
                        res += '\n'
                    print(res.strip('\n'),'\ncount:%s\n' % res.count('\n'))

                elif 'like' in line:
                    enroll_select_colu = sql_limit[3].strip("\",\'")  # 得到where后想要查询的年龄字段
                    enroll_date_ok = enroll_find(staff_table,enroll_select_colu)
                    res = ''
                    for line in enroll_date_ok:
                        for num in line:
                            res += (num + '\t')
                        res += '\n'
                    print(res.strip('\n'), '\ncount:%s\n' % res.count('\n'))

        else:   # 搜部分字段的情况下
            column_list = sql_column.split(',')
            column_list_ok = userCol_to_dbCol(column_list)
            age_select_colu = sql_limit[3].strip("\",\'")  # 得到where后想要查询的age字段
            age_ok = age(staff_table,int(age_select_colu))
            res = ''
            for line in age_ok:
                for num in column_list_ok:
                    res += (line[num] + '\t\t')
                res += '\n'
            print(res,'\n>count:%s' % res.count('\n'))

    # 解析INSERT数据语句
    elif sql_action.upper() == 'INSERT':
        insert_value = re.findall(r'[^()]+', user_input)[3] # 使用正则匹配用户输入的value部分
        new_user_list = insert_value.split(',')
        staff_id = ''
        with open(r'employee_db.txt',mode='r',encoding='utf-8') as f_read:
            data = f_read.read()
            a = data.split('\n')
            l = []
            for x in a:
                l.append(x.split(',')[0])
            staff_id = str((int(max(l)) + 1))

            if new_user_list[2] not in data:    # 判断pyhone是否为唯一键
                with open(r'employee_db.txt',mode='a',encoding='utf-8') as f_write:
                    data = '\n'+staff_id+','
                    today = datetime.date.today()
                    for line in new_user_list:
                        data += (line.strip('\',\"')+',')
                    data += str(today)
                    f_write.writelines(data)
                    print('用户添加成功！\n')
                    continue
            else:
                print('用户已存在，请重新添加。\n')

    # 解析DELETE数据语句
    elif sql_action.upper() == 'DELETE':

        s = re.findall(r'[^=]+', user_input)
        delete_staff_id = s[1].strip().strip('\',\"')
        with open(r'employee_db.txt',mode='r',encoding='utf-8') as f,open(r'employee_db.txt.swap',mode='w',encoding='utf-8') as f_new:
            data = f.read()
            db_list = data.split('\n')

            user_id_exist = []
            for line in db_list:
                user_id_exist.append(line.split(',')[0])

            if delete_staff_id not in user_id_exist:
                print('用户不存在或已被删除。\n')
                continue
            else:
                delete_info = ''
                all_line = ''
                for line in db_list:
                    use_info_list = line.split(',')
                    if delete_staff_id == use_info_list[0]:
                        delete_info = line
                        print('用户[%s]已被删除。\n' % delete_info)
                        continue
                    all_line += (line+'\n')
                f_new.write(all_line.strip('\n'))

            os.remove('employee_db.txt')
            os.rename('employee_db.txt.swap','employee_db.txt')

    # 解析UPDATE数据语句
    elif sql_action.upper() == 'UPDATE':
        s1 = re.findall(r'[^=]+', user_input)
        user_old_update_dep = s1[2].strip().strip('\',\"')    # 被更改的部分名称
        s2 = re.findall(r'[^=]+', user_input)
        user_new_update_dep = re.findall(r'[^\'|^\"]+', s2[1].strip())[0]
        with open(r'employee_db.txt',mode='r',encoding='utf-8') as f_read,open(r'employee_db.txt.swap',mode='w',encoding='utf-8') as f_write:
            data = f_read.read()
            data = data.strip().strip('\n')
            update_dep_list = data.split('\n')

            all_line = ''
            update_dep_info = []
            for line in update_dep_list:
                new_dep = ''
                dep_info_list = line.split(',')
                if user_old_update_dep.upper() == dep_info_list[4].upper():
                    dep_info_list[4] = user_new_update_dep
                    update_dep_info.append(line)
                    for x in dep_info_list:
                        new_dep += (x+',')
                    line = new_dep.strip().strip(',')
                all_line += (line + '\n')
            f_write.write(all_line.strip('\n'))

            print('更改成功,被更改用户为：')
            for i in update_dep_info:
                print(i.split(',')[1])
            print()
        os.remove('employee_db.txt')
        os.rename('employee_db.txt.swap','employee_db.txt')