# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 21:37:22 2024

@author: pc
"""

import math
a=str(input("Nhap hinh muon tinh: "))
if a=="hinh chu nhat":
    b=float(input("Nhap chieu dai: "))
    c=float(input("Nhap chieu rong: "))
    print("Chu vi hinh chu nhat: ",(b+c)*2)
    print("Dien tich hinh chu nhat: ",b*c)
elif a=="hinh tron":
    r=float(input("Nhap ban kinh hinh tron: "))
    print("Chu vi hinh tron: ",round(2*math.pi*r,3))
    print("Dien tich hinh tron: ",round((r**2)*math.pi,3))
elif a=="hinh vuong":
    e=float(input("Nhap canh: "))
    print("Chu vi hinh vuong: ",e*4)
    print("Dien tich hinh vuong: ",e**2)
else:
    print("Nhap sai! Vui long nhap lai!")