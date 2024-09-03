# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 16:55:49 2024

@author: pc
"""

import random
#a. 0 den 1000
print("a. So nguyen ngau nhien tu 0 den 100 la: ",random.randrange(1,100,1))
print("a. So thuc ngau nhien tu 0 den 100 la: ",random.uniform(1,100))
#b. 50 den 99
print("b. So nguyen ngau nhien tu 50 den 99 la: ",random.randrange(50,99,1))
print("b. So thuc ngau nhien tu 50 den 99 la: ",random.uniform(50,99))
#c. -39 den 79
print("c. So nguyen ngau nhien tu -39 den 79 la: ",random.randrange(-39,79,1))
print("c. So thuc ngau nhien tu -39 den 79 la: ",random.uniform(-39,79))
#d. -79 den -39
print("d. So nguyen ngau nhien tu -79 den -39 la: ",random.randrange(-79,-39,1))
print("d. So thuc ngau nhien tu -79 den -39 la: ",random.uniform(-79,-39))