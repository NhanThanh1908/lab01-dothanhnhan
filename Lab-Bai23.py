# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:01:47 2024

@author: pc
"""

a=float(input("Nhap gia tri a: "))
b=float(input("Nhap gia tri b: "))
c=float(input("Nhap gia tri c: "))
d=float(b**2-4*a*c)
if d<0:
    print("Phuong trinh vo nghiem")
elif d>0:
    print("Phuong trinh co 2 nghiem phan bien:",round((-b+d**0.5)/(2*a),3),round((-b-d**0.5)/(2*a),3))
else:
    print("Phuong trinh co nghiem kep:",-b/2*a)