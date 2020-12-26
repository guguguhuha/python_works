with open("xueyajilu.txt","r",encoding="utf-8") as f:
    a=f.readlines()
left_high=[]
left_low=[]
right_high = []
right_low = []
for i in a:
    temp=(i.strip()).split(",")
    left_high.append(temp[1])
    left_low.append(temp[2])
    right_high.append(temp[3])
    right_low.append(temp[4])
lh=max(left_high)
ll=max(left_low)
rh = max(right_high)
rl = max(right_low)
print("{:<10}{:<5}{:<5}".format("对比项","左臂","右臂"))
print("{:<8}{:<7}{:<5}".format("高压最大值",lh,rh))
print("{:<8}{:<7}{:<5}".format("低压最大值",ll,rl))

