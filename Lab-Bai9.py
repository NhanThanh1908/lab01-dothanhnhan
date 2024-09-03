# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 18:11:47 2024

@author: pc
"""

print(" =========== MENU ============ ")
print("\t1. Hu tieu")
print("\t2. Chao long")
print("\t3. Banh canh")
print("\t4. Bun rieu")
print("\t5. Pho bo")
print(" ============================== ")
menu=["1","2","3","4","5","hu tieu","chao long","banh canh","bun rieu","pho bo"]
luachon=input(" Mời nhập lựa chọn: ").lower()
if luachon in menu: 
   print(" ============================== ")
else:
    print("Mon an ban chon ko co trong menu! Vui long nhap lai")