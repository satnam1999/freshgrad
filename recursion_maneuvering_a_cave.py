def fibonacci(i,j,m,n):
    if i>m or j>n:
      return 0
    if i==m and j==n:
      return 1
    q = fibonacci(i+1,j,m,n) + fibonacci(i,j+1,m,n)
    return q
 
lst=input().split()
m=int(lst[0])
n=int(lst[1])
i=0
j=0
ans = fibonacci(i,j,m-1,n-1)
print(ans)
