def removeKdigits(num, k):
        s = len(num)-k
        if s == 0:
            return '0'
        num = [int(i) for i in num]
        ans = []
        def helper(num, s):
            if s == 1:
                ans.append(str(min(num)))
                return 
            minv = min(num[:-s+1])
            ind = num[:-s+1].index(minv)
            ans.append(str(minv))
            helper(num[ind+1:], s-1)
            return
        
        helper(num, s)
        s1 = ''.join(ans)
        s1 = int(s1)
        s1 = str(s1)
        return s1
n=(input())
k=int(input())
print(removeKdigits(n,k))
