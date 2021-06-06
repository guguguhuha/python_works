#计算n的阶乘累加求和
from functools import reduce
def sum_fac(n):
    Sum=[]
    for i in range(1,n+1):
        a=reduce(lambda x,y:x*y,range(1,i+1))
        Sum.append(a)
    return sum(Sum)
num=int(input(""))
print(sum_fac(num))
