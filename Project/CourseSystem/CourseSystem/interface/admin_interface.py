# -*- coding:utf-8 -*-
"""管理员接口层"""
from db import models


# 管理员注册函数
def register(name, pwd):
    # 1.判断用户是否存在
    admin_obj = models.Admin.select(name)

    # 存在则返回错误信息
    if admin_obj:
        return False, "该用户已存在"

    # 不存在则注册
    admin_obj = models.Admin(name, pwd)
    # 保存信息
    admin_obj.save()

    return True, "注册成功！"


# 管理员登录函数
def login(user, pwd):
    # 1.查看当前用户是否存在
    admin_obj = models.Admin.select(user)

    # 2.如果不存在，则返回信息并返回至视图层
    if not admin_obj:
        return False, "该用户不存在"

    # 3.若用户存在，则验证密码，返回相应信息
    if pwd == admin_obj.pwd:
        return True, "登录成功！"
    else:
        return False, "密码错误！"


# 管理员创建学校接口
def create_school(sch_name, sch_addr, user):
    # 1.查看当前学校是否存在
    school_obj = models.School.select(sch_name)

    # 2.若存在则返回错误信息、
    if school_obj:
        return False, "该学校已存在！"

    # 3.不存在则创建 --- 由管理员创建
    admin_obj = models.Admin.select(user)

    admin_obj.create_school(sch_name, sch_addr)

    # 4.创建成功则返回相应信息
    return True, f"{sch_name} 创建成功！"
