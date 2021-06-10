# 1753
# 최단경로

# class Node:
#   def __init__(self, value, prv, nxt):
#     self.value = value
#     self.prv = prv
#     self.nxt = nxt
import sys

def _1753():
  v, e = map(int,input().split())
  k = int(input())
  dix = [[] for _ in range(v+1)]
  for _ in range(e):
    inp = list(map(int,sys.stdin.readline().rstrip().split()))
    dix[inp[0]].append(inp)
  ds = [2000000]*(v+1)
  ds[k] = 0
  pq = []
  for i in range(1,v+1):
    if i != k:
      pq.append([i,ds[i]])
  pq.append([k,ds[k]])

  while(pq):
    nn = pq.pop()
    # if nn[1] != 2000000 and nn[1] <= ds[nn[0]]:
    if nn[1] <= ds[nn[0]]:
      ds[nn[0]] = nn[1]
      for di in dix[nn[0]]:
        if ds[di[1]] > ds[di[0]] + di[2]:
          pq.append([di[1], ds[di[0]] + di[2]])


  for i in range(1,v+1):
    if ds[i]> 1999999:
      print("INF")
    else:
      print(ds[i])
_1753()

