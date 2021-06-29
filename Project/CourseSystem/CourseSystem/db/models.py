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
    def create_school(self,sch_name,sch_addr):
        school_obj = School(sch_name, sch_addr)
        school_obj.save()

class Teacher:
    pass

class School(Base):
    # 初始化
    def __init__(self,name,addr):
        # 在这必须写user，为了select方法的统一
        self.user = name
        self.addr = addr
        # 创建课程列表
        self.course_list = []

class Student(Base):
    pass


if __name__ == "__main__":
    pass
