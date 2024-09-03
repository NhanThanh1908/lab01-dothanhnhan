# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:40:25 2024

@author: pc
"""

a=int(input("Nhap gio: "))
b=int(input("Nhap phut: "))
c=int(input("Nhap giay: "))
if a>=0 and a<24 and b>=0 and b<=59 and c>=0 and c<=59:
    print("Bay gio la: ",a,":",b,":",c)
    print("Doi ra giay la: ",a*3600+b*60+c)
else:
    print("Nhap sai! Vui long nhap lai")