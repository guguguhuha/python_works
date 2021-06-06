# -*- coding: UTF-8 -*-
# 微信 : 咕咕咕呼哈
# 手机号 : 15339887672

# 由于数据复制进来太多,所以我就把它存入了另外一个叫做data.py的文件里
# 并把所给的大列表命名为 data_list

from data import data_list as data  # 引用所给的数据

province_data = []
for i in data:  # 提取数据中的省份
    province_data.append(i[1][:2])  # 在这没有取3 是因为数据中的省份有的没有‘省’或‘市’字，再多没必要
province_data = set(province_data)  # 集合去重一下
# print(province_data)

classify_data = {data: [] for data in province_data}  # 生成一个存放数据的字典

for per_province in classify_data:  # 遍历提取的省份，从而添加元素
    for info in data:  # 遍历所给的信息
        if per_province == info[1][:2]:  # 如果省份匹配就添加
            classify_data[per_province].append(info)  # 添加元素

print(classify_data)  # 数据已生成

for per_province_data in classify_data:  # 逐条打印数据
    print(per_province_data)
    for message in classify_data[per_province_data]:
        print(message)

# 写入文件
with open('data.text', 'w', encoding="utf-8") as f:
    for per_province_data in classify_data:  # 逐条打印数据
        f.write(''.join([per_province_data, '\n']))
        for message in classify_data[per_province_data]:
            f.write(''.join([str(message), '\n']))
