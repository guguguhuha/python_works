# -*- coding:utf-8 -*-
import os
from conf import settings
import pickle


# 保存函数
def save(obj):
    # 1.
    # 分别用类名来创建文件夹
    # 再用对象名来存每个对象的信息
    # obj.__class__ 获取当前类的信息
    # obj.__class__.__name__ 获取当前类的名称
    class_name = obj.__class__.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 2.判断文件夹是否存在，不存在则创建文件夹
    if not os.path.exists(user_dir_path):
        os.makedirs(user_dir_path)

    # 3.拼接用户名的pickle文件路径，以用户名作为文件名
    user_path = os.path.join(
        user_dir_path, obj.user
    )

    # 4.将用户信息存入pickle文件
    with open(user_path, "wb") as f:
        pickle.dump(obj, f)


# 查看信息
def select(cls, user_name):
    # 类名文件夹 --> 对象文件 --> 读取
    class_name = cls.__name__
    user_dir_path = os.path.join(
        settings.DB_PATH, class_name
    )

    # 1.判断文件夹是否存在，不存在就创建
    if not os.path.exists(user_dir_path):
        os.makedirs(user_dir_path)

    # 2.拼接当前用户的pickle路径，以用户名创建文件
    user_path = os.path.join(
        user_dir_path, user_name
    )

    # 3.判断文件是否存在，如果存在，读取信息返回
    #   如果不存在，则代表用户不存在
    if os.path.exists(user_path):
        with open(user_path, "rb") as f:
            obj = pickle.load(f)
            return obj


if __name__ == "__main__":
    class Test:
        def __init__(self, user, y, z):
            self.user = user
            self.y = y
            self.z = z


    a = Test("1", "2", "3")
    print("sdgfsdgfdtsdg")
    save(a)
