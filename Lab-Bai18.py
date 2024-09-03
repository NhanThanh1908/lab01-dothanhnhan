# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 17:42:30 2024

@author: pc
"""

a=int(input("Nhap gio 1: "))
b=int(input("Nhap phut 1: "))
c=int(input("Nhap giay 1: "))
d=int(input("Nhap gio 2: "))
e=int(input("Nhap phut 2: "))
f=int(input("Nhap giay 2: "))
if 0<=a<=23 and 0<=d<=23 and 0<=b<=60 and 0<=e<=60 and 0<=d<=60 and 0<=f<=60:
    print("Gio thu nhat: ",a,"gio",b,"phut",c,"giay")
    print("Gio thu hai: ",d,"gio",e,"phut",f,"giay")
    doigio1=a*3600
    doiphut1=b*60
    doigio2=d*3600
    doiphut2=e*60
    x=(c+f)+(doiphut1+doiphut2)+(doigio1+doigio2)
    gio=x//3600
    phut=round((x%3600)//60,0)
    giay=round((x%3600)%60,0)
    print("Tong 2 gio la: ",gio,"gio",phut,"phut",giay,"giay")
    y=(c-f)+(doiphut1-doiphut2)+(doigio1-doigio2)
    hieugio=y//3600
    hieuphut=round((y%3600)//60,0)
    hieugiay=round((y%3600)%60,0)
    print("Hieu 2 gio la: ",hieugio,"gio",hieuphut,"phut",hieugiay,"giay")
else:
    print("Nhap sai! Vui long nhap lai")