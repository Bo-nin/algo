# silver1
# 1로 만들기 2

from collections import deque
import copy

x = int(input())

isVisit = [1]*1000001

bfsQueue = deque()
bfsQueue.append([x])
ans = []
while(bfsQueue):
  tq = bfsQueue.popleft()
  if isVisit[tq[-1]]:
    isVisit[tq[-1]] = 0
  else:
    continue
  if tq[-1] == 1:
    ans = tq
    break
  if tq[-1] % 3 == 0:
    ntq = list(copy.deepcopy(tq))
    ntq.append(int(tq[-1]/3))
    bfsQueue.append(ntq)
  if tq[-1] % 2 == 0:
    ntq = list(copy.deepcopy(tq))
    ntq.append(int(tq[-1]/2))
    bfsQueue.append(ntq)
  ntq = list(copy.deepcopy(tq))
  ntq.append(tq[-1]-1)
  bfsQueue.append(ntq)
print(len(ans)-1)
print(*ans)