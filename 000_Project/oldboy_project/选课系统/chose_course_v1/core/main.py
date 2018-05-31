from core import admin,teacher,student

def admin_view():
    print('\033[1;34m-----Admin View-----\033[0m')
    admin_view_dic = {
        '1':['用户注册',admin.register],
        '2':['用户登录',admin.login],
        '3':['创建学校',admin.create_school],
        '4':['创建老师',admin.create_teacher],
        '5':['创建课程',admin.create_course],
    }

    while True:
        key_list = []
        for x,y in admin_view_dic.items():
            print(x,y[0])
            key_list.append(x)
        choice = input('Please choose action:').strip()
        if choice == 'q':break
        if choice not in key_list:
            print('\033[1;31m[x] Have no this action,please retry.\033[0m')
            continue

        admin_view_dic[choice][1]()

def teacher_view():
    print('\033[1;34m-----Teacher View-----\033[0m')
    teacher_view_dic = {
        '1':['教师登录',teacher.login],
        '2':['已选授程',teacher.look_selected_course],
        '3':['选择课程',teacher.to_select_course],
        '4':['查课程学生',teacher.look_course_below_student],
        '5':['改学生成绩',teacher.edit_student_score],
    }

    while True:
        key_list = []
        for x,y in teacher_view_dic.items():
            print(x,y[0])
            key_list.append(x)
        choice = input('Please choose action:').strip()
        if choice == 'q':break
        if choice not in key_list:
            print('\033[1;31m[x] Have no this action,please retry.\033[0m')
            continue

        teacher_view_dic[choice][1]()

def student_view():
    print('\033[1;34m-----Student View-----\033[0m')
    student_view_dic = {
        '1':['学生注册',student.register],
        '2':['学生登录',student.login],
        '3':['选择校区',student.select_school],
        '4':['选择课程',student.select_course],
        '5':['查看成绩',student.look_score],
        '6':['已选课程',student.get_all_my_course]
    }

    while True:
        key_list = []
        for x,y in student_view_dic.items():
            print(x,y[0])
            key_list.append(x)
        choice = input('Please choose action:').strip()

        if choice == 'q':break
        if choice not in key_list:
            print('\033[1;31m[x] Have no this action,please retry.\033[0m')
            continue
        student_view_dic[choice][1]()

menu_dic = {
    '1':{
        'view':['管理视图',admin_view],
    },
    '2':{
        'view':['教师视图',teacher_view],
    },
    '3':{
        'view':['学生视图',student_view],
    },
}

print('\033[1;34m >>欢迎来到老男孩选课系统<< \033[0m')
def run():
    while True:
        key_list = []
        for x,y in menu_dic.items():
            print(x,y['view'][0])
            key_list.append(x)
        choice = input('Please choose view: ').strip()

        if choice == 'b':
            print('\033[1;31m欢迎再次使用老男孩选课系统，bye。\033[0m')
            break
        if choice not in key_list:
            print('视图不存在，请重新选择。')
            continue

        menu_dic[choice]['view'][1]()