# -*- coding:utf-8 -*-
"""
用户视图层 --- 主视图
"""

from core import admin
from core import teacher
from core import student

# 功能函数字典
func_dict = {
    "1": admin.admin_view,
    "2": teacher.teacher_view,
    "3": student.student_view
}


def run():
    while True:
        print("""
        ===========选课系统===========
                 1.管理员功能
                 2.教师功能
                 3.学生功能
                 q.退出
        =============================
            """)
        choice = input("请输入你的选择 >:")
        if choice not in func_dict:
            if choice == "q":
                print("谢谢使用！")
                break
            else:
                print("输入有误，请检查输入！")
                continue
        else:
            func_dict.get(choice)()
