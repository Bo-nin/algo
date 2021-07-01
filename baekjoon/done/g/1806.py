# 1806
# 부분합
# gold 4

n, s = list(map(int, input().split()))
numList = list(map(int, input().split()))
pSum = numList[0]
l, r = 0, 1
_min = 100001
while(1):
  if pSum >= s:
    if _min > r-l:
      _min = r-l
    pSum -= numList[l]
    l += 1
  elif r == n:
    break
  else:
    pSum += numList[r]
    r += 1
if _min == 100001:
  print(0)
else:
  print(_min)