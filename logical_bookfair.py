def wrapper(lst,n,i):
    r=[0]*(n+2)
    r[i]=lst[i]
    return r[i]
def max_steal(lst,n,i,k):
  	if (i)>=n:
          return 0
  	return max(wrapper(lst,n,i)+max_steal(lst,n,i+k+1,k),max_steal(lst,n,i+1,k))
    
def rob(nums,k):    
    def rob_helper(i): 
        if length - 1 == i:
            return nums[i]							
        if i >= length:
            return 0
        if i in map:
            return map[i]
        f_sum = nums[i] + rob_helper(i+k+1)
        s_sum = nums[i+1] + rob_helper(i+k+2)
        map[i] = max(f_sum, s_sum)
        return map[i]
    
    length = len(nums)
    map = {}
    
    return rob_helper(0)
lst=list(map(int,input().split(',')))
n=lst[0]
k=lst[1]
lst1=[]
for i in range(n):
	lst1.append(int(input()))
i=0
print(rob(lst1,k))




