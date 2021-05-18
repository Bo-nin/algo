# 16236
# 아기 상어
import copy

# 위 왼 오 아
mv = [[-1,0],[0,-1],[0,1],[1,0]]


def bfs(b, r, c, s):
  tmp = [[r,c,0]]
  nextTemp = []
  while(True):
    ansBox = []
    while(tmp):
      r,c,t = tmp.pop(0)
      # print(r,c,t)
      if b[r][c] > 0 and b[r][c] < s:
        ansBox.append([r,c,t])
      if b[r][c] == 999:
        continue
      b[r][c] = 999
      for m in mv:
        nr, nc = r+m[0], c+m[1]
        if nr >= 0 and nr < len(b) and nc >= 0 and nc < len(b):
          if b[nr][nc] <= s:
            nextTemp.append([nr, nc, t+1])
    if len(ansBox) != 0:
      ansBox.sort()
      return ansBox[0]
    if len(nextTemp) == 0:
      return 0
    tmp = copy.deepcopy(nextTemp)
    nextTemp = []
  
def _16236():
  n = int(input())
  b = [list(map(int,input().split())) for _ in range(n)]
  s = 2
  e = 0
  t = 0
  r = 0
  c = 0
  for i in range(n):
    for j in range(n):
      if b[i][j] == 9:
        b[i][j] = 0
        r, c = i, j

  while(True):
    tmpB = copy.deepcopy(b)
    res = bfs(tmpB, r, c, s)
    if res == 0:
      break
    r = res[0]
    c = res[1]
    t += res[2]
    b[r][c] = 0
    e += 1
    if e == s:
      s += 1
      e = 0
    
    # for _b in b:
    #   print (*_b)
    # print(t)
  return t


print(_16236())