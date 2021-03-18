def call_print(f):
    def g():
        print("you\'re call %s function"%(f.__name__,))
    return g

@call_print
def fun_1():
    pass

@call_print
def fun_2():
    pass

fun_1()
fun_2()