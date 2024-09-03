# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:37:17 2024

@author: pc
"""

a=int(input("Nhap so nguyen duong N: "))
if a>=10 and a<=99:
    b=a//10
    c=a%10
    print("Tong hai chu so cua N: ",b+c)
else:
    print("Nhap sai! Moi nhap lai")
    