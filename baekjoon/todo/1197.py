# 1197
# 최소 스패닝 트리
# gold 4


# Prim 알고리즘 v^2
v, e = list(map(int, input().split()))
ess = [list(reversed(list(map(int, input().split())))) for _ in range(e)]
ess.sort(reverse=True)
# eds = [[] for _ in range(v+1)]
# for es in ess:
#   eds[es[0]].append(es)

# rdq = [ess[0][0]]
# isVisit = [0]*(v+1)
# isVisit[rdq[0]] = 1
# total = 0
# for _ in range(v-1):
#   _min = 2147483647
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
# print (total)

# Kruskal 알고리즘 e log e



def isUnion(u, a, b):
  
  return findUnion(u, a) == findUnion(u, b)

def findUnion(u, a):
  while(u[a] != a):
    a = u[a]
  return a

def union(u, a, b):
  u[findUnion(u, a)] = findUnion(u, b)
  
u = list(range(v+1))

total = 0
for _ in range(v-1):
  while(1):
    tt = ess.pop()
    if (not isUnion(u,tt[1],tt[2])):
      union(u, tt[1], tt[2])
      total += tt[0]
      break
print(total)