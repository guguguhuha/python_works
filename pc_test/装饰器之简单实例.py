def call_print(f):
    def g():
        print("you\'re call %s function"%(f.__name__,))
    return g

def fun_1():
    pass
fun1 = call_print(fun1)

@call_print
def fun_2():
    pass

fun_1()
fun_2()
