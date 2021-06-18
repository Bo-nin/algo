# 1647
# 도시 분할 계획
# glod 4

# n개 노드 m개 간선 양방
# n개 노드를 2개의 최소신장트리로 나누기

import sys
# Prim 알고리즘 v^2


v, e = list(map(int,sys.stdin.readline().rstrip().split()))
ess = [list(reversed(list(map(int,sys.stdin.readline().rstrip().split())))) for _ in range(e)]
ess.sort(reverse=True)
# eds = [[] for _ in range(v+1)]
# for es in ess:
#   eds[es[0]].append(es)

# rdq = [ess[0][0]]
# isVisit = [0]*(v+1)
# isVisit[rdq[0]] = 1
# _max = 0
# total = 0
# for _ in range(v-2):
#   _min = 1000
#   wait = []
#   for rd in rdq:
#     for ed in eds[rd]:
#       if isVisit[ed[1]] == 0:
#         if ed[2] < _min:
#           _min = ed[2]
#           wait = ed
#   isVisit[wait[1]] = 1
#   rdq.append(wait[1])
#   eds[wait[0]].remove(wait)
#   total += _min
#   _max = max(_max, _min)
# print (total-_max)

# Kruskal 알고리즘 e log e


# 경로 압축하기
def findUnion(u, a):
  if (u[a] == a):
    return a
  u[a] = findUnion(u, u[a])
  return u[a]

# 낮은랭크가 하위유니온으로 들어오게 하기
def union(u, rank, a, b):
  a, b = findUnion(u, a), findUnion(u, b)
  if a == b :
    return False
  if rank[a] < rank[b]:
    u[a] = b
  else:
    u[b] = a
    if rank[a] == rank[b]:
      rank[a] += 1
  return True
  
  
u = list(range(v+1))
rank = [0]*(v+1)
total = 0
for _ in range(v-2):
  while(1):
    tt = ess.pop()
    if (union(u, rank, tt[1],tt[2])):
      total += tt[0]
      break
print(total)