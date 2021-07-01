# -*- coding:utf-8 -*-
"""公告接口"""
import os
from conf import settings
from db import models


# 查看所有学校
def get_all_school_interface():
    # 获取所有的学校列表
    school_dir = os.path.join(
        settings.DB_PATH, "School"
    )

    # 判断文件夹是否存在
    if not os.path.exists(school_dir):
        return False, "暂无学校列表，请联系管理员添加！"

    # 若文件夹存在，则获取文件夹中所有文件的名称
    school_list = os.listdir(school_dir)
    return True, school_list


# 获取学校下的所有课程
def get_course(school_name):
    # 1.获取学校对象
    school_obj = models.School.select(school_name)

    # 2.获取学校对象下的课程
    course_list = school_obj.course_list
    # 判断
    if not course_list:
        return False, "该学校下没有课程绑定！"
    else:
        return True, course_list


if __name__ == "__main__":
    print(get_all_school_interface())
