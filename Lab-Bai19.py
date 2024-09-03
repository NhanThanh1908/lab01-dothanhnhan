# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:03:58 2024

@author: pc
"""

a=int(input("Nhap so nguyen a: "))
b=int(input("Nhap so nguyen b: "))
c=int(input("Nhap so nguyen c: "))
nhonhat=a
if b>nhonhat:
    nhonhat=b
if c>nhonhat:
    nhonhat=c
print("So nho nhat trong 3 so la: ",nhonhat)