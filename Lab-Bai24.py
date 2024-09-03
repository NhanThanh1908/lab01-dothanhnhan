# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:04:31 2024

@author: pc
"""

a=int(input("Nhap gio: "))
b=int(input("Nhap phut: "))
c=int(input("Nhap giay: "))
if 0<=a<23 and 0<=b<=59 and 0<=c<=59:
    print(a,"gio",b,"phut",c,"giay")
if a>=24:
    print("Gio ko hop le! Vui long nhap lai")
if b>=60:
    print("Phut ko hop le! Vui long nhap lai")
if c>=60:
    print("Giay ko hop le! Vui long nhap lai")