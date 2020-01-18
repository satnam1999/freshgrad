s=input()
m=0
hash=set()
for j in range(len(s)):
    if s[j] not in hash:
   		hash.add(s[j])
    else:
     	hash.clear()
    if len(hash)>m:
      m=len(hash)
print(m)
