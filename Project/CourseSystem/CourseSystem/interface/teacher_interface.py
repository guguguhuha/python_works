# -*- coding:utf-8 -*-
# 教师接口
from interface import common_interface
from db import models


# 教师登录接口
def login(name, password):
    # 1.判断用户是否存在
    teacher_obj = models.Teacher.select(name)

    # 2.不存在则返回相应信息
    if not teacher_obj:
        return False, "用户名不存在！"

    # 3.用户存在则校验密码
    if password == teacher_obj.pwd:
        return True, "登录成功！"
    else:
        return False, "密码错误！"


# 查看可教授课程
def check_course(teacher_name):
    # 获取老师对象
    teacher_obj = models.Teacher.select(teacher_name)

    # 查看课程列表
    course_list = teacher_obj.show_course()

    # 判断返回值
    if not course_list:
        return False, "课程列表中暂无课程！"
    else:
        return True, course_list


# 添加课程
def add_course(course, user):
    # 获取老师对象
    teacher_obj = models.Teacher.select(user)

    course_list = teacher_obj.course_list

    if course in course_list:
        return False, "该课程已在列表中"

    # 不存在则添加
    teacher_obj.add_course(course)

    return True, f"课程{course}添加完毕"


# 得到学生列表
def get_stu_list(course, user):
    teacher_obj = models.Teacher.select(user)

    stu_list = teacher_obj.get_stu_list(course)

    if not stu_list:
        return False, "该课程下没有学生"

    return True, stu_list


# 给课程下学生打分
def mark_score(course, stu, score, user):
    # 获取老师对象
    teacher_obj = models.Teacher.select(user)

    # 调用修改对象方法
    teacher_obj.mark_score(course, stu, score)

    return True, "打分成功！"
