# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:03:39 2024

@author: pc
"""

a=float(input("Nhap can nang cua ban: "))
b=float(input("Nhap chieu cao cua ban: "))
if a>0 and 0<b<3:
    print("So do kiem tra suc khoe BMI cua ban la: ",round(a/(b**2),1))
else:
    print("Nhap sai! Moi nhap lai")