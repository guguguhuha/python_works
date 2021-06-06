import functools
def func(x):
    sum_fun=[]
    for i in range(1,x+1):
        a=functools.reduce(lambda a,b:a*b ,list(range(1,i+1)))
        sum_fun.append(a)
    return  sum(sum_fun)
a=int(input("请输入一个数："))
print("1到%d的阶乘和为："%a)
print(func(a))