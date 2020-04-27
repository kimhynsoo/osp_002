#!/usr/bin/python
import re
def go2():
    x=input("1st list: ")
    x1=[int(s) for s in re.findall(r'\b\d+\b',x)]

    y=input("2nd list: ")
    y1=[int(s) for s in re.findall(r'\b\d+\b',y)]
    a=list(set(x1).union(y1))
    b=list(set(x1).intersection(y1))
    print("=> union ",a)
    print("=> intersection ",b)



