# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 16:58:21 2024

@author: pc
"""

a=int(input("Nhap bien so xe cua ban: ",))
if a>=1000 and a<=9999:
    a=str(a)
    sodautien=a[0:1]
    sothuhai=a[1:2]
    sothuba=a[2:3]
    sothutu=a[3:4]
    b=int(sodautien)
    c=int(sothuhai)
    d=int(sothuba)
    e=int(sothutu)
    n=b+c+d+e
    if n>10:
        n=str(n)
        sothu1=n[0:1]
        sothu2=n[1:2]
        m=int(sothu1)
        o=int(sothu2)
        print("So nut cua ban la: ",m+o,"nut")
    else:
        print("So nut xe ban la: ",n,"nut")
else:
    print("Nhap sai!Vui long nhap lai!")