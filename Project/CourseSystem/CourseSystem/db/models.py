# -*- coding:utf-8 -*-
from db import db_handler


class Base:
    # 保存数据
    def save(self):
        db_handler.save(self)

    # 查看数据
    @classmethod
    def select(cls, user_name):
        obj = db_handler.select(cls, user_name)
        return obj


class Admin(Base):
    # 初始化 --- 给当前对象赋值
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    # 创建学校
    def create_school(self, sch_name, sch_addr):
        school_obj = School(sch_name, sch_addr)
        school_obj.save()

    # 创建课程
    def create_course(self, school_obj, course_name):
        # 调用课程类，实例化对象
        course_obj = Course(course_name)
        course_obj.save()
        # 将课程添加到课程列表
        school_obj.course_list.append(course_name)
        # 更新数据
        school_obj.save()

    # 创建老师
    def create_teacher(self, teacher_name, teacher_pwd):
        # 调用老师类创建并保存
        teacher_obj = Teacher(teacher_name, teacher_pwd)
        teacher_obj.save()


# 教师类
class Teacher(Base):

    # 初始化
    def __init__(self, name, pwd):
        self.user = name
        self.pwd = pwd
        self.course_list = []

    # 展示课程列表
    def show_course(self):
        return self.course_list

    # 添加课程
    def add_course(self, course_name):
        self.course_list.append(course_name)
        self.save()

    # 获取课程下学生名单
    def get_stu_list(self, course_name):
        course_obj = Course.select(course_name)
        return course_obj.stu_list

    # x修改课程下学生成绩
    def mark_score(self, course_name, stu_name, score):
        # 1.获取学生对象
        stu_obj = Student.select(stu_name)

        # 给学生对象中的课程打分
        stu_obj.score_dict[course_name] = score
        stu_obj.save()


# 学校类
class School(Base):
    # 初始化
    def __init__(self, name, addr):
        # 在这必须写user，为了select方法的统一
        self.user = name
        self.addr = addr
        # 创建课程列表
        self.course_list = []


# 学生类
class Student(Base):

    # 初始化
    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd
        # 一个学生只能有一个小曲
        self.school = None
        # 一个学生可以选择多门课程
        self.course_list = []
        # 学生课程的分数
        self.score_dict = {}


# 课程类
class Course(Base):

    # 初始化对象
    def __init__(self, course_name):
        self.user = course_name
        # 创建学生列表
        self.stu_list = []


if __name__ == "__main__":
    pass
