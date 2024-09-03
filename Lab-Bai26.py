# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:47:10 2024

@author: pc
"""

#a. cho 3 so
a=float(input("Nhap so a: "))
b=float(input("Nhap so b: "))
c=float(input("Nhap so c: "))
if a>b:
    a,b=b,a
if a>c:
    a,c=c,a
if b>c:
    b,c=c,b
print("Cac so theo thu tu tang dan: ",a,b,c)
#b. So N
x=int(input("Nhap so nguyen N: "))
y=str(x)
z=list(y)
z.sort()
n=''.join(z)
h=int(n)
print("Cac so theo thu tu tang dan: ",h)