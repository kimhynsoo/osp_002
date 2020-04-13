#!/usr/bin/python

F1=F2=1
n=int(input("fibonacci number? "))
sum=0
if (n == 1):
    print("1")
    print("F1 = 1")
elif (n==2):
    print("1,1")
    print("F2 = 1")
else:
    print("1,1,",end="")
    for i in range(1,n-1):
        if (i==n-2):
            sum = F1+F2
            print("%d"%sum);
            print("F%d = %d"%(n,sum))
            break
        
        sum = F1+F2
        print("%d,"%sum,end="");
        F1=F2
        F2=sum

