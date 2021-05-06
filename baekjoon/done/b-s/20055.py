def aArrChange(integer: int):
  return [integer, 0]

n, k = map(int, input().split())
aArr = list(map(int,input().split()))
aArr = list(map(aArrChange, aArr))
upPoint = 0
downPoint = n-1
endKey = 0
phase = 0
cycle = list(range(2*n-1, -1, -1))
while(1):
  phase += 1
  # 1
  upPoint -= 1
  if upPoint == -1:
    upPoint = 2*n-1
  downPoint -= 1
  if downPoint == -1:
    downPoint = 2*n-1
  if aArr[downPoint][1]:
    aArr[downPoint][1] = 0
  cycle.append(cycle.pop(0))
  # print(cycle)
  # print(*aArr)
  # 2
  for i in cycle:
    if aArr[i][1]:
      if not aArr[(i+1)%(2*n)][1] and aArr[(i+1)%(2*n)][0]:
        aArr[i][1] = 0
        aArr[(i+1)%(2*n)][1] = 1
        aArr[(i+1)%(2*n)][0] -= 1
        if not aArr[(i+1)%(2*n)][0]:
          endKey += 1
  if aArr[downPoint][1]:
    aArr[downPoint][1] = 0
  # print(*aArr)
  # 3
  if not aArr[upPoint][1] and aArr[upPoint][0]:
    aArr[upPoint][1] = 1
    aArr[upPoint][0] -= 1
    if not aArr[upPoint][0]:
      endKey += 1
  if aArr[downPoint][1]:
    aArr[downPoint][1] = 0
  # print(*aArr)
  if endKey >= k:
    break
print(phase)