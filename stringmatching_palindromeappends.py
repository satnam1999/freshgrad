
def chk(str,l,h):
    while(l<h):
        if(s[l]!=s[h]):
            return False
        l=l+1
        h=h-1
    return True
s=input()
for i in range(len(s)):
  if chk(s,i,len(s)-1):
     break
print(i)
