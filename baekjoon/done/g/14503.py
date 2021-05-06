import time

n, m = map(int, input().split())
r, c, d = map(int, input().split())
area = [list(map(int, input().split())) for _ in range(n)]

directions = [[-1,0],[0,1],[1,0],[0,-1]]

numOfClean = 0
moveCnt = 0
while (1):
  if not area[r][c]:
    area[r][c] = 2
    numOfClean += 1
  d -= 1
  moveCnt += 1
  if d < 0:
    d = 3
  r, c = r + directions[d][0], c + directions[d][1]
  if r < 0 or r > n - 1 or c < 0 or c > m - 1 or area[r][c]:
    r, c = r - directions[d][0], c - directions[d][1]
  else:
    moveCnt = 0
    continue
  if moveCnt == 4:
    r, c = r + directions[(d + 2) % 4][0], c + directions[(d + 2) % 4][1]
    if r < 0 or r > n - 1 or c < 0 or c > m - 1 or area[r][c] == 1:
      break
    else:
      moveCnt = 0
print (numOfClean)

    