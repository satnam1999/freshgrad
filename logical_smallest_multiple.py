#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 14:19:29 2020

@author: abcd
"""

from itertools import permutations
N=int(input())
d=int(input())
a=list(str(N))
b=list(permutations(a))
flag=0

for i in range(len(b)):
    if b[i][0]=='0':
        b[i]=b[i][1:]
    b[i]=int(''.join(b[i]))

for i in sorted(b):   
    if i%d==0:
        print(i)
        flag=1
        break
if flag==0:
    print(-1)

