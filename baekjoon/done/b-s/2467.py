# 2467
# 용액
# gold 5

def solution():
  n = int(input())
  koiList = list(map(int,input().split()))
  _min = 2000000001
  minSet = []
  l = 0
  r = n-1
  for _ in range(n-1):
    if _min > int(abs(koiList[l]+koiList[r])):
      _min = int(abs(koiList[l]+koiList[r]))
      minSet = [koiList[l], koiList[r]]
    if abs(koiList[l]+koiList[r-1]) > abs(koiList[l+1]+koiList[r]):
      l += 1
    else:
      r -= 1
  print(*minSet)
solution()