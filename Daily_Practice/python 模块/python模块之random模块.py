import random

print(random.randint(0,8)) # 产生0 ~ 8的整数(包括 8 )

print(random.random()) # 产生0 ~ 1 之间的小数

print(random.randrange(0,8)) # 产生0 ~ 8的整数(不包括 8 )

print(random.choice('21414')) # 在所给序列里随机挑出一个随机数（字符）

print(random.sample('qeqrqwt',3))# 在所给序列里随机挑出自定义个随机数（字符）

a=[1,2,3,4,5,6,[7,7,8,8]]
random.shuffle(a) # 将所给序列随机乱序
print(a)

# 实现验证码的实现
def auth_code():
    code = ''
    for i in range(4):
        code_choice = [str(random.randint(0,9)),chr(random.randint(97,122))] # 为了实现数字和字母的随机分布
        code += random.choice(code_choice)
    return code

import string
def auth_code_2():
    code_choice = string.ascii_lowercase + string.digits
    code = random.sample(code_choice,4)
    code=''.join(code)
    return code

def auth_code_3():
    code=''
    for i in range(4):
        if i == random.randint(0,4):
            code += str(random.randint(0,9))
        else:
            code += chr(random.randint(97,122))
    return code


print(auth_code())

print(auth_code_2())

print(auth_code_3())
