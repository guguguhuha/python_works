#from openpyxl import Workbook
import string
#wb=Workbook()
#ws=wb.active
with open("20-21-1（周二班）期中考试学号（加密）成绩表.txt","r") as f1 , open("pj.csv","w")  as f2 :
    #
    q=f1.readlines()
    # print(q)
    n=11
    les=[['学号','总成绩','1','2','3','4']]
    for i in q:
        #print(int(i[:6]))

        for a in string.digits:
            for s in string.digits:
                for d in string.digits:
                    for f in string.digits:
                        for g in string.digits:
                            if  ((((((ord(a)*ord(g)) % n) * 10 + ((ord(s)*ord(f)) % n)) * 10 + ((ord(d)*ord(d)) % n))
                                  * 10 + ((ord(f)*ord(s)) % n)) * 10 + ((ord(g)*ord(a)) % n))==int(i[:6]):
                                #i=list(i.strip())
                               #i[:6]=''.join([a,s,d,f,g])
                                qwer=i.split()
                                #qwer.append('\n')
                                # print(qwer)

                                qwer[0]=''.join([a,s,d,f,g])
                               # ws.append(qwer)
                                les.append(qwer)

                                # f2.write(str(qwer))
                                # f2.write(''.join([a,s,d,f,g]))
                                # f2.write(i[1])
                                # f2.write(i[2])
                                # f2.write(i[3])
                                # f2.write(i[4])
                                # f2.write(i[5])
                                # f2.write('\n')
                               # wb.save('D:\Application\pycharm_works\_1\pj2.xlsx')
    for i in les:
        f2.write(','.join(i)+'\n')
print("have done!\n")
