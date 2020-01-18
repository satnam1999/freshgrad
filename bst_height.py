#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 10:21:26 2020

@author: abcd
"""

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

def height(root):
  if root is None:
    return 0
  else:
    m=height(root.left)
    n=height(root.right)
  return max(m+1,n+1)
    
i=0
while(True):
    n=int(input())
    if i==0 and n!=-1:
        r=node(n)
    elif n==-1:
        break
    else:
        insert(r,node(n))
    i=i+1
if(n==-1 and i==0):
  print("Height of the tree is 0",end="")
else:
  print("Height of the tree is ",end="")
  print(height(r))


      
      
        
