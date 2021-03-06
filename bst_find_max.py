

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 09:35:38 2020

@author: abcd
"""

class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.val=data

def insert(root,node): 
    if root is None: 
        root = node
    else: 
        if root.val < node.val: 
            if root.right is None: 
                root.right = node 
            else: 
                insert(root.right, node) 
        else: 
            if root.left is None: 
                root.left = node 
            else: 
                insert(root.left, node) 
                
def inorder(root,lst): 
    if root is not None:
      inorder(root.left,lst)
      lst.append(root.val)
      inorder(root.right,lst)
lst=[]             
i=0
while(True):
    n=int(input())
    if i==0 and n!=0 and n!=-1:
        r=node(n)
    elif n<1:
        break
    else:
        insert(r,node(n))
    i=i+1
print("Maximum element is ",end="")
inorder(r,lst)
print(max(lst))
