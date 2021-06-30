# -*- coding:utf-8 -*-
"""学生视图"""
from lib import common
from interface import student_interface

# 学生名单列表
student_info = {
    "user": None
}


# 学生注册
def register():
    while True:
        user = input("请输入姓名:>").strip()
        pwd = input("请输入密码:>").strip()
        re_pwd = input("请再次输入密码:>").strip()

        # 检查密码的一致性
        if pwd != re_pwd:
            print("两次密码不一致！")
            continue
        else:
            # 调用接口层注册
            flag, msg = student_interface.register(user, pwd)

            # 检查返回
            if flag:
                print(msg)
                break
            else:
                print(msg)


# 学生登录
def login():
    while True:
        user = input("请输入用户名:>").strip()
        pwd = input("请输入密码:>").strip()

        # 调用登录接口
        flag,msg = student_interface.login(user, pwd)

        # 判断返回
        if not flag:
            print(msg)
        else:
            print(msg)
            # 添加当前用户状态
            student_info["user"] = user
            break



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
