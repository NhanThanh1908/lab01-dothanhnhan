# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 17:27:05 2024

@author: pc
"""

import math
a=float(input("Nhap so thuc a: "))
b=float(input("Nhap so thuc b: "))
x=((((a+b)/(pow(a,1/3)+pow(b,1/3)))-(pow(a*b,1/3)))/pow((pow(a,1/3)-pow(b,1/3)),2))
print("Ket qua la:",round(x,3))