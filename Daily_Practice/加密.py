# 3 某个公司采用公用电话传递数据，数据是四位的整数，
# 在传递过程中是加密的，加密规则如下：
# 每位数字都加上5,然后用和除以10的余数代替该数字，
# 再将第一位和第四位交换，第二位和第三位交换。
# 试输入一个数，并求出对应的数字。
while True:
    ip=input("请输入一个四位数：")
    if len(ip)!=4:
        if ip=='':
            break
        else:
            print("你输入的位数有误，请重新输入 ")
    else:
        b=[]
        a=list(ip)
        a=list(map(int,a))
        for i in a:
            i=(i+5)%10
            b.append(i)
        print("加密后的数为：",end="")
        print(b[3],b[2],b[1],b[0],sep='')

