# 2473
# 세 용액
# gold 4
import copy
def solution():
  n = int(input())
  originList = list(map(int,input().split()))
  _min = 3000000001
  minSet = []
  originList.sort()
  for tarIdx in range(n):
    l = 0
    r = n-2
    koiList = originList[:tarIdx] + originList[tarIdx+1:]
    tarNum = originList[tarIdx]
    for _ in range(n-2):
      if _min > int(abs(koiList[l]+koiList[r]+tarNum)):
        _min = int(abs(koiList[l]+koiList[r]+tarNum))
        
        minSet = [koiList[l], koiList[r], tarNum]
      if abs(koiList[l]+koiList[r-1]+tarNum) > abs(koiList[l+1]+koiList[r]+tarNum):
        l += 1
      else:
        r -= 1
  minSet.sort()
  print(*minSet)
solution()