# 1005
# ACM Craft
# gold 3

from collections import defaultdict

def dfs(w, memo, orderedDict, dTimes):
    res = []
    for key in orderedDict[w]:
        if memo[key] != -1:
            pass
        else:
            memo[key] = dfs(key, memo, orderedDict,dTimes)
        res.append(memo[key])
    if res:
        return max(res) + dTimes[w]
    else:
        return dTimes[w]
        
        

t = int(input())
for _ in range(t):        
    n, k = map(int,input().split())
    dTimes = [0] + list(map(int,input().split()))
    orderedDict = defaultdict(list)
    for _ in range(k):
        x,y = map(int,input().split())
        orderedDict[y].append(x)
    w = int(input())
    memo = [-1]*(n+1)
    print(dfs(w,memo,orderedDict,dTimes))

        