import time
def timing_func(f):
    def wrapper():
        start = time.time()
        f()
        stop = time.time()
        return (stop - start)
    return wrapper

@timing_func
def fun1():
    print("lalala")
    time.sleep(1)

@timing_func
def fun2():
    print("hehehe")
    time.sleep(1)

print(fun1())
print(fun2())