# -*- coding: UTF-8 -*-
import re
import functools


def format_str(s):  # 格式化字符串
    s = s.replace(" ", "")
    s = s.replace("++", "+")
    s = s.replace("+-", "-")
    s = s.replace("-+", "-")
    s = s.replace("--", "+")
    s = s.replace("/+", "/")
    s = s.replace("*+", "*")
    #    print("该表达式格式化后的结果为：%s" % s)
    return s


def check_str(s):  # 检查字符串是否合法
    flag = True  # 初始化假设字符串合法
    if s.count("(") != s.count(")"):  # 检查（）是否个数相等
        flag = False
    if re.search("[a-zA-Z]", s):  # 检查是否出现了非法字符
        flag = False
    #    print("该表达式的合法性为：%s" % flag)
    return flag


def div_mul(s):  # 进行表达式中乘或除的计算
    while True:
        ret = re.search("(?P<num1>\d+(?:\.\d+)?)(?P<sign>[*/])(?P<num2>[+-]?\d+(?:\.\d+)?)", s)  # 匹配乘或除的式子，
        # 第二个操作数可以匹配符号，防止比如 1*-3匹配不到
        # 第一个操作数没有匹配符号是因为防止 1-2*-3 --> 1  (-2*-3) --> 1 6 -->在下一个函数中成为 1+6 --> 7  的错误结果

        # ret = re.search("(?P<num1>\d+(?:\.\d+)?)(?P<sign>[*/])(?P<num2>\d+(?:\.\d+)?)", s)
        # if not ret:
        #     ret = re.search("(?P<num1>\d+(?:\.\d+)?)(?P<sign>[*/])(?P<num2>[+-]?\d+(?:\.\d+)?)", s)

        if ret:  # 如果ret不为空就代表表达式中含有加或减的式子
            exp = ret.group()  # 把表达式分离开来
            num1 = ret.group("num1")  # 操作数1
            num2 = ret.group("num2")  # 操作数2
            sign = ret.group("sign")  # 运算符号
            if sign == "*":  # 乘法
                result = float(num1) * float(num2)
            if sign == "/":  # 除法
                result = float(num1) / float(num2)
            print("{}{}{}={}".format(num1, sign, num2, result))  # 运行结果的打印
            s = s.replace(exp, str(result))  # 将计算结果替代表达式

        else:  # 如果ret为空就代表该表达式中已经没有乘或除的式子了，就跳出循环
            break
    s = format_str(s)  # 格式化该字符串中的输出结果
    return s


def add_sub(s):  # 进行表达式中加或减的计算
    result = 0  # 先定义一个求和的总变量为0
    if re.search("[+-]", s):
        ret = re.findall("[+/-]?\d+(?:\.\d+)?", s)  # 只匹配一个数字以及该数字前的符号，最后进行相加
        print(ret)  # 打印所匹配的内容，即所有要相加的数
        result = str(functools.reduce(lambda x, y: float(x) + float(y), ret))  # 进行各个数的相加
        print(result)
        s = s.replace(s, result)  # 将计算结果替代表达式
    return s


def calc(s):  # 进行表达式的计算
    s = div_mul(s)
    s = add_sub(s)
    # s = s.replace("(", "")#去括号
    # s = s.replace(")", "")
    s = s.strip("()")  # 去括号
    print("该表达式计算后的结果为：%s" % s)
    return s


def main():
    strs = input()

    while not check_str(strs):
        print("非法表达式！请重新输入")
        strs = input()

    strs = format_str(strs)

    while re.search("\(", strs):  # 如果还有（）就进入循环
        ret = re.search("\([^()]+\)", strs)  # 匹配最里面的（）
        if (ret):
            exp = ret.group()  # 进行表达式的分离
            print(exp)
            result = calc(exp)  # 进行表达式的计算
            strs = strs.replace(exp, result)  # 表达式与结果的替换
            strs = format_str(strs)  # 格式化
            print(strs)

    strs = calc(strs)
    print(strs)


main()
print(eval("1-2*((60-30 +(9-2*5/3+7/3*99/4*2998+10*568/14)*(-40 / 5))-(-4*3)/(16-3*2))"))

# 1-2*((60-30 +(9-2*5/3+7/3*99/4*2998+10*568/14)*(-40 / 5))-(-4*3)/(16-3*2))
# 2776672.6952380957
