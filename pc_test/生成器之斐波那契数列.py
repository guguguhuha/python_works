def f():
    a, b = 0, 1            #序列解包，同时为多个元素赋值
    while True:
        yield a            #暂停执行，需要时再产生一个新元素
        a, b = b, a+b      #序列解包，继续生成新元素
a = f()                    #创建生成器对象
for i in range(10):        #斐波那契数列中前10个元素
    print(next(a), end=' ')
