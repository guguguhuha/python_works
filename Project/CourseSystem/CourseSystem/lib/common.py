# -*- coding:utf-8 -*-

# 用户登录认证器
def auth(role):
    """
    :param role:角色
    :return:
    """
    from core import admin,teacher,student
    # 登录认证装饰器
    def login_auth(func):
        def inner(*args,**kwargs):
            if role == "admin":
                if admin.admin_info.get("user"):
                    res = func(* args,** kwargs)
                    return res
                else:
                    admin.login()
            elif role == "student":
                if student.student_info.get("user"):
                    res = func(* args,** kwargs)
                    return res
                else:
                    student.login()
            elif role == "teacher":
                if teacher.teacher_info.get("user"):
                    res = func(* args,** kwargs)
                    return res
                else:
                    teacher.login()
            else:
                print("当前用户没有权限！")
        return inner
    return login_auth


