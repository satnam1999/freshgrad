
def numIslands(matrix):
    
    res = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j]==1:
                if dfs(matrix, i, j):
                    res += 1
    return res

def dfs(matrix, i, j):
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or matrix[i][j] == 0:
        return False
    if matrix[i][j] == 1:
        matrix[i][j] = 0
        dfs(matrix, i, j-1)
        dfs(matrix, i, j+1)
        dfs(matrix, i-1, j)
        dfs(matrix, i+1, j)
        dfs(matrix, i-1, j-1)
        dfs(matrix, i+1,j-1)
        dfs(matrix ,i-1,j+1)
        dfs(matrix, i+1, j+1)
        return True
        
lst=list(map(int,input().split()))
a=[0]*lst[0]
n=lst[0]
for i in range(lst[0]):
	a[i]=list(map(int,input().split()))
print(numIslands(a)-1) 
