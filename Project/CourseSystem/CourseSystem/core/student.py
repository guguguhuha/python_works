# -*- coding:utf-8 -*-
"""学生视图"""
from lib import common
# 学生名单列表
student_info = {
    "user": None
}

# 学生注册
def register():
    pass


# 学生登录
def login():
    pass


# 学生选择学校
@common.auth("student")
def choose_school():
    pass


# 学生选择课程
@common.auth("student")
def choose_course():
    pass


# 学生查看分数
@common.auth("student")
def check_score():
    pass


# 功能函数字典
func_dict = {
    "1": register,
    "2": login,
    "3": choose_school,
    "4": choose_course,
    "5": check_score
}


# 学生视图
def student_view():
    while True:
        print("""
        ===========学生视图===========   
                  1.注册            
                  2.登录              
                  3.选择校区
                  4.选择课程
                  5.查看分数              
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
