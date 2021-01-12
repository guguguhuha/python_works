def gcd(x, y):  # 求x，y的最大公约数
    r = x % y
    while r != 0:
        x, y = y, r
        r = x % y
    return y


def lcm(x, y):  # 求x，y的最小公倍数
    return x * y / gcd(x, y)
while True:
    m = int(input('请输入瓷砖长度(cm)，输入0为退出：'))
    if m == 0:
        break
    n = int(input('请输入瓷砖宽度(cm)：'))
    L = lcm(m,n)
      # L为长度和宽度的最小公倍数
    print('要拼成最小正方形的面积是%d（cm^2）' % (L**2))