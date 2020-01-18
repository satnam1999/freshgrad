n=int(input())
lst=list(map(int,input().split()))
ogi=(format(n,'08b'))

a=list(ogi)

x=lst[0]
y=lst[1]
if x+1>8 or y+1>8:
    a=['0']+a

a[-(x+1)],a[-(y+1)]=a[-(y+1)],a[-(x+1)]
b=''.join(a)
print(int(b,2))
print(ogi)

# 
#c[x-1],c[y-1]=c[y-1],c[x-1]
#c="".join(c)
#print(int(c,2))
#print(ogi)


