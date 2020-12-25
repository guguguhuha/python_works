import  math
def sum_fec(n):
    Sum=[]
    for i in range(1,n+1):
        a=math.factorial(i)
        Sum.append(a)
    return  sum(Sum)
a=int(input("请输入一个数："))
print("1到%d的阶乘和为："%a)
print(sum_fec(a))