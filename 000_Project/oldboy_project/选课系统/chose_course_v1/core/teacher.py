#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author: Tdcqma
from interface import common_interface,teacher_interface
from lib import common
teacher_status = {
    'name':None
}

def login():
    '''
    教师登录
    :return:
    '''

    if teacher_status['name']:
        print('\033[1;31mYou are logged in and can do other things.\033[0m')
        return

    while True:
        teacher_name = input('Please input your username:').strip()
        if teacher_name == 'q':break
        password = input('Please input your password:').strip()

        flag,res = common_interface.common_login(teacher_name,password,'teacher')
        if flag:
            teacher_status['name'] = teacher_name
            print(res)
            break
        else:
            print(res)
            continue

@common.login_auth(auth_type='teacher')
def look_selected_course():
    course_list = teacher_interface.get_selected_course(teacher_status['name'])
    if not course_list:
        print('\033[1;31mYou have not chosen the course, please choose the course first.\033[0m')
        return
    print('Your select course\'s info:')
    for i,course_name in enumerate(course_list):
        print('\033[1;32mNO:%s \t CourseName:%s\033[0m' % (i,course_name))

@common.login_auth(auth_type='teacher')
def to_select_course():
    '''
    教师选择要教授的课程
    :return:
    '''

    while True:
        exist_course_list = common_interface.get_all_courses()
        if not exist_course_list:
            print('There\'s no course is created,please create course first.')
            return

        for i,course_name in enumerate(exist_course_list):
            print('\033[1;32mID: %s\tCourseName: %s\033[0m' % (i,course_name))
        #school_choose = input('please select school name(Enter num):').strip()
        course_choice = input('Please select course name(Enter num): ').strip()

        if course_choice == 'q':break

        if course_choice.isdigit():
            course_choice = int(course_choice)
            if course_choice >= 0 and course_choice < len(exist_course_list):
                teacher_interface.choose_course(teacher_status['name'],exist_course_list[course_choice])
                break
            else:
                print('\033[1;31mYour select course is not exist.please check it again.\033[0m')
        else:
            print('\033[1;31mPlease enter num of course.\033[0m')

@common.login_auth(auth_type='teacher')
def look_course_below_student():
    '''
    查看教授课程下面有哪些学生
    首先要将教授的课程列表显示出来
    :return:
    '''
    exist_course_list = teacher_interface.get_selected_course(teacher_status['name'])
    if not exist_course_list:
        print('\033[1;31mYou have not chosen the course, please choose the course first.\033[0m')
        return

    print('Your select course\'s info:')
    for i, course_name in enumerate(exist_course_list):
        print('\033[1;32mNO:%s \t CourseName:%s\033[0m' % (i, course_name))

    course_choice = input('Please select course to see students:').strip()

    if course_choice.isdigit():
        course_choice = int(course_choice)
        if course_choice >= 0 and course_choice < len(exist_course_list):
            student_list = teacher_interface.get_student_by_course(exist_course_list[course_choice])
            if not student_list:
                print('\033[1;31mThere\'s no student select this course yes.\033[0m')
                return

            for i,student_name in enumerate(student_list):
                print('\033[1;32mNO:%s \t StudentName:%s\033[0m' % (i, student_name))
        else:
            print('\033[1;31mYour selected course is not exist.\033[0m')
    else:
        print('\033[1;31mPlease enter num of course.\033[0m')


@common.login_auth(auth_type='teacher')
def edit_student_score():
    # 获取老师选择教授的所有课程
    while True:
        teach_all_course = teacher_interface.get_all_teached_course(teacher_status['name'])
        if not teach_all_course:
            print('you haven\'t choosed course,please choose course first.')
            break

        for i,course_name in enumerate(teach_all_course):
            print('ID:%s\tCourseName:%s'%(i,course_name))

        course_choice = input('Please input number of course:').strip()

        if course_choice.isdigit():
            course_choice = int(course_choice)
            if course_choice >= 0 and course_choice < len(teach_all_course):
                all_student_list = teacher_interface.get_student_by_course(teach_all_course[course_choice])

                if not all_student_list:
                    print('\033[1;31mSorry. haven\'t student choose this course.\033[0m')
                    break

                for i,student_name in enumerate(all_student_list):
                    print('ID:%s\tStudentName:%s'%(i,student_name))

                student_choice = input('please choose student and to edit cores.').strip()
                if student_choice.isdigit():
                    student_choice = int(student_choice)
                    if student_choice >= 0 and student_choice < len(all_student_list):
                        print('Your selected student name:%s' % (all_student_list[student_choice]))
                        score = input('Please input score of course:').strip()
                        if score.isdigit():
                            score = int(score)
                            if score >= 0 and score <= 100:
                                teacher_interface.teacher_change_student_score(teacher_status['name'],all_student_list[student_choice],teach_all_course[course_choice],score)
                                break
                            else:
                                print('score must be num 1 between 100.')
                        else:
                            print('\033[1;31mscore must be digits.please input again.\033[0m')
                else:
                    print('please input number of student.')
        else:
            print('please input number of course.')