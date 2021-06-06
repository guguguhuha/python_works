s = input('输入行数（1-9）:')
print('%s行' % s)
line=int(s)# (1)此处为line变量赋值
for i in range(1, line + 1):
    space = ' ' * (line - i)  # 此句单引号中有一个空格
    print(space, end='')
    for j in range(1,i+1) :   # (2)此处用循环打印前一半字符串
        print(chr(64 + j), end='')
    for j in range(i - 1, 0, -1):
        print(chr(64 +j),end='')# (3)此处在循环体中打印后一半字符串
    print()

