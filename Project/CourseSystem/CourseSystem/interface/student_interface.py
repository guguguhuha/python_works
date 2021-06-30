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
