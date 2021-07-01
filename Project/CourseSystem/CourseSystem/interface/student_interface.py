# -*- coding:utf-8 -*-
# 学生接口函数
from db import models


# 学生注册接口
def register(name, pwd):
    # 1.判断用户是否存在
    stu_obj = models.Student.select(name)

    # 检查返回
    if stu_obj:
        return False, "该用户已存在"

    # 不存在则注册,然后保存
    stu_obj = models.Student(name, pwd)
    stu_obj.save()

    return True, "注册成功"


# 学生登录接口
def login(user, pwd):
    # 检查是否拥有这人
    stu_obj = models.Student.select(user)

    # 如果是None，则返回错误信息
    if not stu_obj:
        return False, "并无此用户！"
    else:
        if pwd == stu_obj.pwd:
            return True, "登录成功！"
        else:
            return False, "密码错误！"


# 学生选择学校接口
def choose_sch(school_name, user):
    # 获取学生对象
    student = models.Student.select(user)

    # 判断学生对象中是否拥有学校
    if student.school:
        return False, "该学生已经绑定过学校了"

    # 如果不存在则添加学校
    student.choose_sch(school_name)
    return True, '绑定学校成功！'


# 获取学生所在学校下的课程、
def get_course(user):
    # 获取当前学生对象
    stu_obj = models.Student.select(user)

    # 取学校的名字，若不存在则返回错误信息
    sch_name = stu_obj.school
    if not sch_name:
        return False, "该学生并没有绑定学校！"

    # 获取学校对象
    sch_obj = models.School.select(sch_name)

    # 对课程列表进行判断
    course_list = sch_obj.course_list
    if not course_list:
        return False, "该学校下没有课程列表！"
    return True, course_list


# 学生添加课程接口
def add_course(course_name, user):
    # 获取学生对象
    stu_obj = models.Student.select(user)

    # 判断该课程是否在学生课程列表之中
    if course_name in stu_obj.course_list:
        return False, "该课程已在学生列表之中"

    # 调用学生对象中添加课程的方法
    stu_obj.add_course(course_name)
    return True, f"课程：{course_name} 添加成功！"


# 学生查看分数接口
def check_score(user):
    # 获取学生对象
    stu_obj = models.Student.select(user)

    # 获取成绩字典
    score_dict = stu_obj.score_dict
    if score_dict:
        return score_dict
    return None
