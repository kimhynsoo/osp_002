#!/usr/bin/python
def go1():
    num= int(input("input binary number : "),2)
    num1=format(num,'o')

    print("=> OCT> ",num1)
    print("=> DEC> ",num)
    num2=format(num,'X')
    print("=> HEX> ",num2)
