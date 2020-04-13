#!/usr/bin/python

sum=0;
n=int(input("Please enter the number of number "))

for i in range(1,n+1):
    sum += int(input("No.%d number "%(i)))
computeaverage=sum//n

print("average is",computeaverage)
