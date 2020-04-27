#!/usr/bin/python
import my_pkg

if __name__=='__main__':
    n=0

    while True:
        n=int(input("Select menu: 1)conversion 2)union/intersection 3)exit ?"))
        if n==1:
            my_pkg.go1()
        if n==2:
            my_pkg.go2()
        if n==3:
            print("exit the program...")
            break
