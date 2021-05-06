import math
n = int(input())
aArr = list(map(int,input().split()))
b, c = map(int,input().split())
res = 0

for a in aArr:
  res += 1
  a -= b
  if a>0:
    res += math.ceil(a/c)
print(res)