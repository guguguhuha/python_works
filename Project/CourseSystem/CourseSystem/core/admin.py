# -*- coding:utf-8 -*-
"""管理员视图"""
from interface import admin_interface
from interface import common_interface
from lib import common

# 当前用户信息
admin_info = {
    "user": None
}


# 管理员注册
def register():
    while True:
        name = input("请输入用户名:>").strip()
        pwd = input("请输入密码:>").strip()
        re_pwd = input("请再次输入密码:>").strip()
        if pwd != re_pwd:
            print("两次密码不一致！")
        else:
            flag, msg = admin_interface.register(name, pwd)  # flag --> True 、False
            if not flag:  # flag -> false 不满足条件，继续循环
                print(msg)
            else:  # flag -> True 满足条件，退出
                print(msg)
                break


# 管理员登录
def login():
    while True:
        user = input("请输入用户名:>").strip()
        pwd = input("请输入密码:>").strip()

        # 调用管理员登录接口
        flag, msg = admin_interface.login(user, pwd)

        # 判断登录状态
        if flag:
            print(msg)
            # 为当前用户添加状态
            admin_info["user"] = user
            break
        else:
            print(msg)


# 管理员创建学校
@common.auth("admin")
def creat_school():
    while True:
        # 1.输入学校的名字和地址
        name = input("请输入学校的名称:>").strip()
        addr = input("请输入学校的地址:>").strip()

        # 2.调用管理员创建学校接口
        flag, msg = admin_interface.create_school(
            name, addr, admin_info.get("user")
        )

        # 3.判断是否创建成功
        if not flag:
            print(msg)
        else:
            print(msg)
            break


# 管理员创建课程
@common.auth("admin")
def creat_course():
    while True:
        # 1.管理员先调用学校接口显示都有哪些学校
        flag, msg = common_interface.get_all_school_interface()

        # 如果学校不存在，打印错误信息
        if not flag:
            print(msg)

        # 否则就打印学校信息
        for i, j in enumerate(msg, 1):
            print(f"编号{i}    学校：{j}")

        # 选择学校为其添加课程
        choice = input("请输入学校编号:>").strip()

        # 检查输入情况 --- 输入类型
        if not choice.isdigit():
            print("请输入数字！")
            continue
        # 检查输入范围
        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("请输入正确的编号！")
            continue

        # 获取学校名字
        sch_name = msg[choice - 1]  # 索引值要减一，因为设置的 enumrate 从1开始

        # 选择学校添加课程
        course_name = input("请输入课程名字:>").strip()

        # 调用接口，管理员创建课程
        flag, msg = admin_interface.create_course(
            sch_name, course_name, admin_info.get("user")
        )

        # 检查返回判断
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 管理员创建老师
@common.auth("admin")
def creat_teacher():
    while True:
        # 输入老师的名字
        teacher_name = input("请输入教师姓名:>").strip()
        # 调用接口创建老师
        flag, msg = admin_interface.create_teacher(
            teacher_name, admin_info.get("user")
        )

        # 检查返回判断
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 功能函数字典
func_dict = {
    "1": register,
    "2": login,
    "3": creat_school,
    "4": creat_course,
    "5": creat_teacher
}


# 管理员视角
def admin_view():
    while True:
        print("""
        ===========管理员视图===========   
                  1.注册             
                  2.登录              
                  3.创建学校
                  4.创建课程
                  5.创建教师              
                  q.退出                
        ==============================
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
