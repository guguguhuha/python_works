def showSanjiao(n):
    n = n+1
    for i in range(n):
        for j in range(0,n-i):  #空格的个数
            print(end=' ')
        for k in range(n-i,n):  #*的个数
            print('*',end=' ')
        print('')

   
    for i in range(n):
        for j in range(n-i,n):  #空格的个数
            print(end=' ')
        for k in range(0,n-i):  #*的个数
            print('*',end=' ')
        print('')
 
m = int(input('输入行数：'))

showSanjiao(m)

               
