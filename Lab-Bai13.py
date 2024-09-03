# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:11:53 2024

@author: pc
"""

a=int(input("Nhap ngay sinh: "))
b=int(input("Nhap thang sinh: "))
c=int(input("Nhap nam sinh: "))
if 1<=a<=31 and 1<=b<=12 and 1000<=c:
#a
    a=str(a)
    b=str(b)
    c=str(c)
    print(a+"/"+b+"/"+c)
#b
    print(a+"/"+b+"/"+c[2:4])
#c
    print(c+"/"+b+"/"+a)
else:
    print("Nhap sai! Moi ban nhap lai!")