from tkinter import *


def confirm():
    ID = str(e_1.get()).upper()
    e_1.delete(0, END)
    if len(ID) != 18:
        s = "请输入18位的身份证号码\n请重新输入"
    else:
        s = ''
        factor = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        last = ['1','0','X','9','8','7','6','5','4','3','2']
        sum = 0
        for i in range(17):
            sum += int(ID[i])*factor[i]
        m = sum % 11
        lastchar = ID[-1]
        if lastchar == last[m]:
            s += '为合法身份证号码\n'
            s += '出生日期为'+ID[6:10]+'年'+ID[10:12]+'月'+ID[12:14]+'日\n'
            if int (ID[-2]) % 2 == 0:
                s += '持卡人为女性\n'
            else:
                s += '持卡人为男性\n'
        else:
            s = "%s为非法身份证号码\n" % ID
    L_2["text"] = s


root = Tk()
root.title("身份证校验")
root.geometry("500x300+400+200")

L_1 = Label(root, text="请输入你的身份证号码：").grid(row=0, column=0)
e_1 = Entry(root, width=30);e_1.grid(row=0, column=1)
b_1 = Button(root, text="确定", command=confirm, width=10).grid(row=0, column=2, sticky=EW)
L_2 = Label(root, text="");L_2.place(relx=0.4, rely=0.4)


root.mainloop()