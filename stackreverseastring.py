#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 09:46:41 2020

@author: abcd
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 09:50:47 2020

@author: abcd
"""



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
            print(temp.d(),end="")
            temp=temp.get_next()
  
        
    def delete_end(self):
        temp=self.__head
        while(temp.get_next().get_next() is not None):
            temp=temp.get_next()
        temp2=temp.get_next()
        temp.set_next(None)
        self.__tail=temp
        del temp2



        
            
        
            
stackk=LinkedList()

a=input()
for i in a:
    stackk.add(i)

        
stackk.display()
