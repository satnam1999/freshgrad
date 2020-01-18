#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 10:02:41 2020

@author: abcd
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-




class node:
    def __init__(self,data):
        self.__data=data
        self.__next=None
    def set_next(self,next_node):
        self.__next=next_node
    def d(self):
        return self.__data
    def get_next(self):
        return self.__next
class LinkedList:
    def __init__(self):
        self.__head=None
        self.__tail=None
        
    def add(self,data):
        new_node=node(data)
        if(self.__head is None):
            self.__head=self.__tail=new_node
        else:
            new_node.set_next(self.__head)
            self.__head=new_node
    
    def display(self):
        temp=self.__head
        while(temp is not None):
            print(int(temp.d()),end=" ")
            temp=temp.get_next()
  
       
    def pop(self):
        if self.__head is None:
            return None
        else:
            popped = self.__head.d()
            self.__head = self.__head.get_next()
            return popped

           
stack1=LinkedList()

exp=input()
s=''

for i in exp:
    if i.isdigit():
        stack1.add(i)
    elif i=='+':
        stack1.add(int(stack1.pop())+int(stack1.pop()))
    elif i=='-':
        stack1.add(int(stack1.pop())-int(stack1.pop()))
    elif i=='*':
        stack1.add(int(stack1.pop())*int(stack1.pop()))
    elif i=='/':
        stack1.add(int(stack1.pop())/int(stack1.pop()))    
    else:
        stack1.add(eval(stack1.pop()+ str(i) + stack1.pop()))
print("Answer is ",end="")
stack1.display()

