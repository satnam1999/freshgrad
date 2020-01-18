def odd_occurrence(arr):
    result = 0
    for element in arr:
        result = result ^ element
    return result

 
n=int(input())
lst=list(map(int,input().split()))
print(odd_occurrence(lst))   



