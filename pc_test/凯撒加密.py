import string
def kaisa(s,k):
    lower=string.ascii_lowercase#小写字母
    upper = string.ascii_uppercase#大写字母
    dight=string.digits#数字
    before=string.ascii_letters + string.digits
    after=lower[k:]+lower[:k]+upper[k: ]+upper[:k]+dight[k:]+dight[:k]#后移k位
    table=''.maketrans(before, after)#创建映射表
    return s.translate(table)
s=input("请输入密码：")
k=int(input("后移位数："))
print("加密后的密码为：",end='')
print(kaisa(s,k))
