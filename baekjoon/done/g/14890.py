# 14890
# 경사로
import copy

def isRight(arr, l, i):
  baseR = arr[i][0]
  j = 0
  n = len(arr)
  while(j < n):
    if baseR != arr[i][j]:  
      if abs(baseR - arr[i][j]) > 1:
        return 0
      if baseR > arr[i][j]:
        baseR = arr[i][j]
        for _ in range(l):
          if j == n:
            return 0
          if arr[i][j] != baseR:
            return 0
          arr[i][j] = 999
          j += 1
      elif baseR < arr[i][j]:
        tj = j
        for _ in range(l):
          tj -= 1
          if tj < 0:
            return 0
          if arr[i][tj] != baseR:
            return 0
          arr[i][tj] = 999
        baseR = arr[i][j]
        j += 1
    else:
      j += 1
  return 1



def isDown(arr, l, i):
  baseR = arr[0][i]
  j = 0
  n = len(arr)
  while(j < n):
    if baseR != arr[j][i]:  
      if abs(baseR - arr[j][i]) > 1:
        return 0
      if baseR > arr[j][i]:
        baseR = arr[j][i]
        for _ in range(l):
          if j == n:
            return 0
          if arr[j][i] != baseR:
            return 0
          arr[j][i] = 999
          j += 1
      elif baseR < arr[j][i]:
        tj = j
        for _ in range(l):
          tj -= 1
          if tj < 0:
            return 0
          if arr[tj][i] != baseR:
            return 0
          arr[tj][i] = 999
        baseR = arr[j][i]
        j += 1
    else:
      j += 1
  return 1

def _14890():
  n, l = map(int,input().split())
  o_arr = [list(map(int, input().split())) for _ in range(n)]


  res = 0
  arrR = copy.deepcopy(o_arr)
  arrD = copy.deepcopy(o_arr)
  
  for i in range(n):
    res += isRight(arrR, l, i)
    # print(i, res)
    res += isDown(arrD, l, i)
    # print(i, res)
    
  print(res)

_14890()
