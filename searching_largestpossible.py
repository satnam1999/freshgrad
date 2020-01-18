n=int(input())
lst=input().split()
from itertools import permutations
l=[list(p) for p in permutations(lst)]
m=0
for i in l:
  s=''
  for j in i:
    s=s+j
  if int(s)>m:
    m=int(s)
print(m)
