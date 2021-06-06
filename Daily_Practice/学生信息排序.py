data = []
print("请输入学生信息格式（输入0退出）\nID 名字 英语成绩 python成绩 C语言成绩")
while True:
    qwer=str(input())
    if qwer=='0':
        break
    ad=qwer.split()
    ad.append(sum([int(ad[2]),int(ad[3]),int(ad[4])]))
    data.append(ad)
data.sort(key=lambda x: x[5])
print(' ID  名字 英语 python C语言 总成绩')
for i in data:
    for j in i:
        print("{:^5}".format(j),end='')
    print()