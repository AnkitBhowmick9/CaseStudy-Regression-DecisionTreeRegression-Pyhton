# -*- coding: utf-8 -*-
"""
Created on Wed Jan 30 22:46:46 2019

@author: Ankit Bhowmick
"""

n = int(input("Enter the number of elements to be inserted: "))
a = []
for i in range(0,n):
     elem = int(input("Enter element: "))
     a.append(elem)
avg = sum(a)/n

print("Average of elements in the list " ,round(avg,2))    