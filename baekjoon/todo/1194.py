# 1194
# 달이 차오른다~ 가자
import copy
move = [[-1,0],[1,0],[0,-1],[0,1]]

def bfsFind(miro, r, c, cnt, keys, doors):
  h = miro[r][c]
  ih = ord(h)
  if h == '#':
    return
  elif ih >= 97 and ih <= 122:
    keys.append([h,r,c])
  elif ih >= 65 and ih <= 90:
    doors.append([h,r,c])
  miro[r][c] = '#'

  for m in move:
    nr, nc = r + m[0], c + m[1]
    if nr >= 0 and nc >= 0 and nr < len(miro) and nc < len(miro[0]):
      if miro[nr][nc] != '#':
        bfsFind(miro, nr, nc, cnt+1, keys, doors)



def _1194():
  # BFS로 완탐 한번 돌면서 획득열쇠 및 방문 문과 좌표 찾을것(열쇠, 문까지 거리도 체크) x 
  # 열쇠와 문이 둘다 존재하는 쌍으로 BFS거리찾기 x
  
  # 문제 잘못이해
  # 

  n, m = map(int,input().split())
  miro = [list(input()) for _ in range(n)]
  keys = []
  doors = []

  for i in range(n):
    for j in range(m):
      if miro[i][j] == '0':
        copiedMiro = list(copy.deepcopy(miro))
        bfsFind(copiedMiro, i, j, 0, keys, doors)
  print(keys)
  print(doors)

_1194()