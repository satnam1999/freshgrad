n=int(input())
k=0
h=0
sum=0
for i in range(1,n+1):
    if i%2==1:
        sum=sum+(9*(10**k))
        k=k+1
    elif i%2==0:
        sum=sum+(9*(10**h))
        h=h+1
print(sum)
