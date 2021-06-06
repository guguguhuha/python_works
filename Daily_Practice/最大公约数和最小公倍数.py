# -*- coding: UTF-8 -*-
import random


def find_num(m, n):
    ret = min(m, n)

    for i in range(1, ret + 1)[::-1]:  # 逆序
        if m % i == 0 and n % i == 0:
            max_div = i  # 最大公约数
            break

    min_mul = (m * n / max_div)  # 最小公倍数
    return max_div, min_mul


if __name__ == "__main__":

    n = random.randint(1, 100)
    # n = random.randrange(1, 101)

    while True:  # 检验输入
        try:
            m = int(input("请输入一个整数: "))
            break
        except:
            print("输入类型有误！")

    max_divisor, min_multiple = find_num(m, n)

    Format = "{:}和{:}的\n最大公约数为{:}\n最小公倍数为{:}".format(m, n, max_divisor, round(min_multiple))

    print(Format)
