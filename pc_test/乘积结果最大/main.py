# # 程序文件Pex8_6.py
# from scipy.integrate import odeint
# import numpy as np
# from mpl_toolkits import mplot3d
# import matplotlib.pyplot as plt
#
#
# def lorenz(w, t):
#     sigma = 10;
#     rho = 28;
#     beta = 8 / 3
#     x, y, z = w;
#     return np.array([sigma * (y - x), rho * x - y - x * z, x * y - beta * z])
#
#
# t = np.arange(0, 50, 0.01)  # 创建时间点
# sol1 = odeint(lorenz, [0.0, 1.0, 0.0], t)  # 第一个初值问题求解
# sol2 = odeint(lorenz, [0.0, 1.0001, 0.0], t)  # 第二个初值问题求解
# plt.rc('font', size=16);
# plt.rc('text', usetex=True)
# ax1 = plt.subplot(121, projection='3d')
# ax1.plot(sol1[:, 0], sol1[:, 1], sol1[:, 2], 'r')
# ax1.set_xlabel('$x$');
# ax1.set_ylabel('$y$');
# ax1.set_zlabel('$z$')
# ax2 = plt.subplot(122, projection='3d')
# ax2.plot(sol1[:, 0] - sol2[:, 0], sol1[:, 1] - sol2[:, 1], sol1[:, 2] - sol2[:, 2], 'g')
# ax2.set_xlabel('$x$');
# ax2.set_ylabel('$y$');
# ax2.set_zlabel('$z$')
# plt.savefig("figure8_6.png", dpi=500);
# plt.show()
# print("sol1=", sol1, '\n\n', "sol1-sol2=", sol1 - sol2)
# 程序文件Pex8_5.py
# from scipy.integrate import odeint
# from sympy.abc import t
# import numpy as np
# import matplotlib.pyplot as plt
#
#
# def Pfun(y, x):
#     y1, y2 = y;
#     return np.array([y2, -2 * y1 - 2 * y2])
#
#
# x = np.arange(0, 10, 0.1)  # 创建时间点
# sol1 = odeint(Pfun, [0.0, 1.0], x)  # 求数值解
# plt.rc('font', size=16);
# plt.rc('font', family='SimHei')
# plt.plot(x, sol1[:, 0], 'r*', label="数值解")
# plt.plot(x, np.exp(-x) * np.sin(x), 'g', label="符号解曲线")
# plt.legend();
# plt.savefig("figure8_5.png");
# for i in range(100):
#     plt.show()
# 程序文件Pex20_13.py
# from PIL import Image,ImageDraw, ImageFont
# a=Image.open('flower.jpg')  #读入图像
# b=ImageDraw.Draw(a) #实例化Draw类
# myfont=ImageFont.truetype("c:\\Windows\\Fonts\\simsun.ttc",48)
# b.text((20,20),"美丽的花",font=myfont,fill=(255,0,0))
# a.show(); a.save("figure20_13.png")
# import numpy as np
# import pylab as plt
# from sklearn.svm import SVR
#
# np.random.seed(123)
# x=np.arange(200).reshape(-1,1)
# y=(np.sin(x)+3+np.random.uniform(-1,1,(200,1))).ravel()
#
# model = SVR(gamma='auto'); print(model)
# model.fit(x,y); pred_y = model.predict(x)
# print("原始数据与预测值前15个值对比：")
# for i in range(15): print(y[i],pred_y[i])
#
# plt.rc('font',family='SimHei'); plt.rc('font',size=15)
# plt.scatter(x, y, s=5, color="blue", label="原始数据")
# plt.plot(x, pred_y, '-r*',lw=1.5, label="预测值")
# plt.legend(loc=1)
#
# score=model.score(x,y); print("score:",score)
# ss=((y-pred_y)**2).sum()  #计算残差平方和
# print("残差平方和：", ss)
# plt.show()

import random
from matplotlib import pyplot

def make_num(num):
    return_num = 0
    for i in num:
        return_num = return_num * 10 + i
    return return_num

x = []
y = []
max_mul = 0
max_mul_a = 0
max_mul_b = 0

num_list = [1, 3, 4, 5, 7]
for i in range(10000):
    a = []
    j = 3
    while j:
        append_element = random.choice(num_list)
        if append_element not in a:
            a.append(append_element)
            j -= 1
    b = []
    k = 2
    while k:
        append_element = random.choice(num_list)
        if (append_element not in a) and (append_element not in b):
            b.append(append_element)
            k -= 1
    a_num = make_num(a)
    b_num = make_num(b)
    if a_num * b_num > max_mul:
        max_mul, max_mul_a, max_mul_b = a_num * b_num, a_num, b_num
    y.append(a_num * b_num)
    x.append(i)
print(max_mul, max_mul_a, max_mul_b)
fig , ax = pyplot.subplots()
ax.plot(x,y,'*')
ax.set_title('Simple Test')
pyplot.savefig("Test Result")
pyplot.show()