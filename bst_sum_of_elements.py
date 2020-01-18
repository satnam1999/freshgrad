

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
                
def inorder(root): 
    
    if root is None:
        return 0
    return root.val+inorder(root.left)+inorder(root.right)
              
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
if n==-1 and i==0:
    print("Sum of all nodes are 0")
else:
    print("Sum of all nodes are ",end="")
    print(inorder(r))
