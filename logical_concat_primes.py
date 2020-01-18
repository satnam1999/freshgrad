#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  5 15:18:22 2020

@author: abcd
"""

#print unique charcters in reverse order

#integer va
#prime no from 1 to n
#concatenate 


s=int(input())
lst=[]
for i in range(2,s):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lst.append(i)

lst2=[]
for i in lst:
    for j in lst:
        lst2.append(int(str(i)+str(j)))

lst3=[]
for i in (lst2):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        lst3.append(i)
if s<=3:
	print(1)
else:
	print(len(lst3))


