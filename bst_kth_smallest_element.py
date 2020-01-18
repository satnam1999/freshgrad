
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
lst=[]                
def inorder(root,lst): 
    if root is not None:
        inorder(root.left,lst)
        lst.append(root.val)
        inorder(root.right,lst)             
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
k=int(input('Enter the kth value:'))
if n==-1 and i==0:
    print("Smallest kth value 0")
else:
    print()
    inorder(r,lst)
    print("Smallest kth value",lst[k-1])
    
 
    
