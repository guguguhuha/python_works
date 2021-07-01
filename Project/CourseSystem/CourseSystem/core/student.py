# -*- coding:utf-8 -*-
"""学生视图"""
from lib import common
from interface import student_interface
from interface import common_interface

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
        flag, msg = student_interface.login(user, pwd)

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
    while True:
        # 获取学校列表，让学生选择
        flag, msg = common_interface.get_all_school_interface()

        # 对返回进行判断
        if not flag:
            print(msg)
            break

        # 打印学校列表
        for i, j in enumerate(msg, 1):
            print(f"序号：{i}   学校：{j}")

        # 进行选择，并对选择进行检验
        choice = input("请输入序号:>").strip()
        if not choice.isdigit():
            print("输入类型错误！")
            continue
        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("编号错误！")
            continue

        # 获取学校名称
        school_name = msg[choice - 1]

        # 调用学生选择学校接口
        flag, msg = student_interface.choose_sch(
            school_name, student_info.get("user")
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)
            break


# 学生选择课程
@common.auth("student")
def choose_course():
    while True:
        # 获取该学生的学校，查看课程列表
        flag, msg = student_interface.get_course(
            student_info.get("user")
        )

        if not flag:
            print(msg)
            break

        # 打印课程列表，学生选择
        for i, j in enumerate(msg, 1):
            print(f"序号：{i}   课程：{j}")

        choice = input("请输入你的选择：")
        if not choice.isdigit():
            print("选择类型错误！")
            continue
        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("选择序号错误！")
            continue

        # 获取课程列表
        course_name = msg[choice - 1]

        # 调用学生选择课程接口
        flag, msg = student_interface.add_course(
            course_name, student_info.get("user")
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 学生查看分数
@common.auth("student")
def check_score():
    # 调用分数接口
    score_dict = student_interface.check_score(
        student_info.get("user")
    )

    # 判断返回
    if not score_dict:
        print("该生没有绑定课程！")

    print(score_dict)


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
