#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 10:21:44 2020

@author: abcd
"""

n=int(input())
def bin(n):
  s=''
  while(n>0):
    if n%2==0:
      s=s+'0'
    else:
      s=s+'1'
    n=n//2
  return s[::-1]
a=bin(n)
s=''

m=0
c=0
for i in a:
    if i=='1':
        c=c+1
    else:
        c=0
    if c>m:
        m=c
print(m)
    
