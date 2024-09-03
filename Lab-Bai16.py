# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:36:07 2024

@author: pc
"""

a=int(input("Nhap gio: "))
b=int(input("Nhap phut: "))
c=int(input("Nhap giay: "))
if 0<=a<=23 and 0<=b<=59 and 0<=c<=59:
    print("Bay gio la: ",a,"h",b,"p",c,"s")
    a=a*3600
    b=b*60
    print("Doi ra giay la: ",a+b+c)
else:
    print("Nhap sai! Vui long nhap lai")