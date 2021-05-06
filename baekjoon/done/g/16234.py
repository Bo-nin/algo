import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

n, l, r = map(int,input().split())
# n, l, r = 50,1,100

arr = [list(map(int,input().split())) for _ in range(n)]
# arr = [list(range())]
# 완탐?

union = [[0]*n for _ in range(n)]
dr = [[1,0],[0,1],[-1,0],[0,-1]]

def dfs(i,j):
    global union
    if not union[i][j]:
        return
    for d in dr:
        ni, nj = i+d[0], j+d[1]
        if ni >=0 and ni < n and nj >= 0 and nj < n:
            if not union[ni][nj]:
                tmp = abs(arr[i][j] - arr[ni][nj])
                if tmp >= l and tmp <= r:
                    union[ni][nj] = union[i][j]
                    dfs(ni,nj)
    
res = 0
#  완탐 아닌듯
while(1):
    idx = 0
    for i in range(n):
        for j in range(n):
            if not union[i][j]:
                idx += 1
                union[i][j] = idx
                dfs(i,j)
    idxPop = [0]*(idx+1)
    idxCnt = [0]*(idx+1)

    for i in range(n):
        for j in range(n):
            idxPop[union[i][j]] += arr[i][j]
            idxCnt[union[i][j]] += 1
    for i in range(1,idx+1):
        idxPop[i] = idxPop[i] // idxCnt[i]
    for i in range(n):
        for j in range(n):
            arr[i][j] = idxPop[union[i][j]]
    # print()
    # for u in union:
    #     print(*u)
    # print()
    # for u in arr:
    #     print(*u)
    if n**2 <= idx:
        break
    else:
        union = [[0]*n for _ in range(n)]
        res += 1
print(res)