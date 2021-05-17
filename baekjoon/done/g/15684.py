# 1개 그으면 2개의 위치가 바뀜

# 내가 영향받은 열의 사다리는 반드시 다시 타야함
#  => 같은 열에 가로선 반드시 짝수개 필요

# 1번째 열부터 생성해야하는 사다리 좌표조합 생성
# 1번째, 2번째 쭉쭉 체크
# 이 룰 망함
import itertools
import copy

def isPosible(sadaris, a, b):
  if sadaris[a][b-1] or sadaris[a][b+1]:
    return False
  return True

def isSuccess(sadaris):
  for i in range(1,len(sadaris[0])):
    x, y = i, 1
    while(y < len(sadaris)):
      
      if sadaris[y][x]:
        x += 1
      elif sadaris[y][x-1]:
        x -= 1
      y += 1
    if x != i:
      return False
  return True

def _15684():
  n, m, h = map(int,input().split())
  seros = [list(map(int,input().split())) for _ in range(m)]
  sadaris = [[0]*(n+2) for _ in range(h+1)]

  # 사다리 갯수 초기체크
  isEvens = [True]*(n+1)
  for sero in seros:
    isEvens[sero[1]] = not isEvens[sero[1]]
    sadaris[sero[0]][sero[1]] = 1
  simpleCnt = 0
  for isEven in isEvens:
    if not isEven:
      simpleCnt += 1
  if simpleCnt > 3:
    return -1

  pArr = []
  for i in range(1,h+1):
    for j in range(1,n+1):
      if isPosible(sadaris, i, j):
        pArr.append([i,j])
  for i in range(4):
    coms = list(itertools.combinations(pArr,i))
    for com in coms:
      isWrong = False
      for j in range(i):
        for k in range(j+1,i):
          
          if com[j][0] == com[k][0]:
            if com[j][1] == com[k][1] -1 or com[j][1] == com[k][1] +1:
              isWrong = True
      if isWrong:
        continue
      tmpSadaris = copy.deepcopy(sadaris)
      for co in com:
        tmpSadaris[co[0]][co[1]] = 1
      if isSuccess(tmpSadaris):
        return i
  return -1

      

print(_15684())






  # 룰이머지ㅣㅣㅣㅣㅣㅣㅣㅣ
  # paths = [[] for _ in range(h+1)]
  # for i in range(1,h+1):
  #   x, y = i, 1
  #   while(y <= h):
  #     if sadaris[y][x]:
  #       x += 1
  #       paths[i].append([x,y])
  #     elif sadaris[y][x-1]:
  #       x -= 1
  #       paths[i].append([x-1,y])
  #     y += 1
  # unsolvedPaths = [[] for _ in range(h+1)]
  # for path in paths:
  #   for pat in path:
  # 이거 망함


  # 각 열 짝수를 만족하는수준에서 완탐으로
