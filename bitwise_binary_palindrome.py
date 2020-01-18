n=int(input())
s=''
def bin(n,s):
  while(n>0):
    if n%2==0:
      s=s+'0'
    else:
      s=s+'1'
    n=n//2
  return s
s=bin(n,s)
if s==s[::-1]:
  print('yes')
else:
  print('no')
