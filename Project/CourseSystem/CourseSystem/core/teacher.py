# -*- coding:utf-8 -*-
"""教师视图"""
from lib import common
# 老师名单列表
teacher_info = {
    "user": None
}

# 教师登录
def login():
    pass


# 教师查看可教授课程
@common.auth("teacher")
def check_school():
    pass


# 教师选择所教授课程
@common.auth("teacher")
def choose_course():
    pass


# 教师查看课程下的学生
@common.auth("teacher")
def check_stu_list():
    pass


# 教师给课程下的学生打分
@common.auth("teacher")
def mark_score():
    pass


# 功能函数字典
func_dict = {
    "1": login,
    "2": check_school,
    "3": choose_course,
    "4": check_stu_list,
    "5": mark_score
}


# 教师视图
def teacher_view():
    while True:
        print("""
        ===========教师视图===========   
                  1.登录             
                  2.查看教授课程              
                  3.选择教授课程
                  4.查看课程下的学生
                  5.给课程下的学生打分              
                  q.退出                
        =============================
            """)
        choice = input("请输入你的选择>:")
        if choice not in func_dict:
            if choice == "q":
                print("返回上一级")
                break
            else:
                print("请检查输入！")
                continue
        else:
            func_dict.get(choice)()
