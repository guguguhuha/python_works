import time
def timing_func(f):
    def wrapper():
        start = time.time()
        f()
        stop = time.time()
        return (stop - start)
    return wrapper

<<<<<<< HEAD

def fun1():
    print("lalala")
    time.sleep(1)
fun1=timing_func(fun1)
=======
def fun1():
    print("lalala")
    time.sleep(1)
fun1 = timong_func(fun1)
>>>>>>> 087b2ff9085292099cac11516e676a873e99562a

@timing_func
def fun2():
    print("hehehe")
    time.sleep(1)

print(fun1())
print(fun2())
