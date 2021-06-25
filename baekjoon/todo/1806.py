# 1806
# 부분합
# gold 4

n, s = list(map(int, input().split()))
numList = list(map(int, input().split()))

l, r = 0, 1
_min = 100000
while(1):
  _sum = sum(numList[l:r])
  if _sum >= s:
    _min = min(_min, r-l)
    l += 1
  elif r == n-1:
    break
  else:
    r += 1
print(_min)