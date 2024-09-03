# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:13:19 2024

@author: pc
"""

a=int(input("Nhap so nguyen a: "))
b=int(input("Nhap so nguyen b: "))
c=int(input("Nhap so nguyen c: "))
lonnhat=a
if b>lonnhat:
    lonnhat=b
if c>lonnhat:
    lonnhat=c
print("So lon nhat trong 3 so la: ",lonnhat)