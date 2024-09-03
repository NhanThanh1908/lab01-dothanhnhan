# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:44:13 2024

@author: pc
"""

a=int(input("Nhap so nguyen: "))
sochu=["Khong","Mot","Hai","Ba","Bon","Nam","Sau","Bay","Tam","Chin"]
if 0<=a<=9:
    print(sochu[a])
else:
    print("Ko hop le! Vui long nhap lai!")