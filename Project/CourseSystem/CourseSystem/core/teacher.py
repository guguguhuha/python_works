# -*- coding:utf-8 -*-
"""教师视图"""
from lib import common
from interface import teacher_interface
from interface import common_interface

# 老师名单列表
teacher_info = {
    "user": None
}


# 教师登录
def login():
    while True:
        teacher_name = input("请输入姓名:>").strip()
        pwd = input("请输入密码:>").strip()

        # 调用教师接口完成登录
        flag, msg = teacher_interface.login(teacher_name, pwd)

        # 检验返回值
        if flag:
            print(msg)
            # 添加当前状态
            teacher_info["user"] = teacher_name
            break
        else:
            print(msg)


# 教师查看可教授课程
@common.auth("teacher")
def check_course():
    flag, msg = teacher_interface.check_course(
        teacher_info.get("user")
    )
    if flag:
        print(msg)
    else:
        print(msg)


# 教师添加所教授课程
@common.auth("teacher")
def choose_course():
    while True:
        # 先打印所有学校，进行选择
        flag, msg = common_interface.get_all_school_interface()
        if not flag:
            print(msg)
            break
        for i, j in enumerate(msg, 1):
            print(f"编号{i}   学校：{j}")

        # 输入并检查输入
        choice = input("请选择学校奥:>").strip()
        if not choice.isdigit():
            print("输入类型有误！")
            continue

        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("编号有误！")
            continue

        # 选择学校名称
        school_name = msg[choice - 1]

        # 从选择的学校中获取所有的课程
        flag, msg = common_interface.get_course(school_name)

        # 判断返回
        if not flag:
            print(msg)
            break

        # 选择课程
        for i, j in enumerate(msg, 1):
            print(f"序号：{i}  课程：{j}")

        choice = input("请输入课程编号:>").strip()
        # 检查输入
        if not choice.isdigit():
            print("输入类型有误！")
            continue
        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("输入编号有误！")
            continue

        # 获取课程名称
        course_name = msg[choice - 1]

        # 调用教师选择课程接口
        flag, msg = teacher_interface.add_course(
            course_name, teacher_info.get("user")
        )

        # 判断返回
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 教师查看课程下的学生
@common.auth("teacher")
def check_stu_list():
    while True:

        # 调用接口获取课程列表
        flag, msg = teacher_interface.check_course(
            teacher_info.get("user")
        )
        if not flag:
            print(msg)
            break

        # 打印课程让其选择
        for i, j in enumerate(msg, 1):
            print(f"序号：{i}   课程：{j}")

        choice = input("请输入选择:>").strip()
        if not choice.isdigit():
            print("输入有误！")
            continue
        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("选项有误！")
            continue
        course_name = msg[choice - 1]

        flag, msg = teacher_interface.get_stu_list(
            course_name, teacher_info.get("user")
        )

        if flag:
            print(msg)
            break
        else:
            print(msg)


# 教师给课程下的学生打分
@common.auth("teacher")
def mark_score():
    '''
    # 1、先获取老师下所有的课程，并选择
    # 2、获取选择的课程下所有的学生，并选择修改的学生
    # 3、调用修改学生分数接口修改分数
    '''
    while True:
        # 1.调取该老师下的所有课程接口
        flag, msg = teacher_interface.check_course(teacher_info.get("user"))

        # 判断返回
        if not flag:
            print(msg)
            break

        # 2.打印课程让其选择
        for i, j in enumerate(msg, 1):
            print(f"序号：{i}   课程：{j}")

        choice = input("请输入选择:>").strip()

        # 检查输入
        if not choice.isdigit():
            print("输入有误！")
            continue
        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("选项有误！")
            continue

        # 获取课程名称
        course_name = msg[choice - 1]

        # 获取学生列表
        flag, msg = teacher_interface.get_stu_list(
            course_name, teacher_info.get("user")
        )

        # 判断返回
        if not flag:
            print(msg)
            break

        # 打印学生让老师选择
        for i, j in enumerate(msg, 1):
            print(f"序号：{i}，学生：{j}")

        choice = input("请输入学生序号:>").strip()

        # 检查输入
        if not choice.isdigit():
            print("输入有误！")
            continue
        choice = int(choice)
        if choice not in range(len(msg) + 1):
            print("选项有误！")
            continue

        # 获取学生名称
        stu_name = msg[choice - 1]

        # 老师输入要打的分
        score = input("请输入所打分值:>").strip()

        # 检查输入
        if not score.isdigit():
            print("请检查输入！")
            continue
        score = int(score)

        # 调用接口修改分数
        flag, msg = teacher_interface.mark_score(
            course_name, stu_name, score,
            teacher_info.get("user")
        )

        # 判断返回
        if flag:
            print(msg)
            break
        else:
            print(msg)


# 功能函数字典
func_dict = {
    "1": login,
    "2": check_course,
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
