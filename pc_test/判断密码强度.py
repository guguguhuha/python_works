# 输入一个字符串作为密码，密码只能由数字与字母组成。编写程序判断输入的密码的强度，并输出。
#
# 判断标准为：满足其中一条，密码强度增加一级。
#
# 1）有数字
#
# 2）有大写字母
#
# 3） 有小写字母
#
# 4）位数不少于8位


def judge(password):
    result = 0

    n =len(password)

    if n >= 8:
        result += 1

    for i in range(n):

        if '0' <= password[i] <= '9':
            result += 1

            break

    for i in range(n):

        if 'A' <= password[i] <= 'Z':
            result += 1

            break

    for i in range(n):

        if 'a' <= password[i] <= 'z':
            result += 1
            break

    return  result


def main():
    """

        主函数

    """

    while True:

        password = input('请输入密码(直接回车为退出)：')

        if password == '':
            break

        s = judge( password)

        print("%s的密码强度为%d级" % (password, s))


main()