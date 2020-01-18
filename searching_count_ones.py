def countones(arr,l,h):
  if(h>=l):
      mid=int((h+l)/2)
      if((mid==h or arr[mid+1]==0) and (arr[mid]==1)):
          return mid+1
      if(arr[mid==1]):
          return countones(arr,(mid+1),h)
      else:
    	  return countones(arr,l,(mid-1))
    
n=int(input())
lst=list(map(int,input().split()))
l=0
h=n-1
if countones(lst,l,h)==None:
    print("Count of 1's in given array is 0")
else:
	print("Count of 1's in given array is {}".format(countones(lst,l,h)))


