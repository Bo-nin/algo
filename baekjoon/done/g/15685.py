# 15685
# 드ㅜ라곤커브

# 시계방향 90도
# 격자를 벗어나지 않음

# 회전규칙
# 기준점 좌표를 뺀다
# x,y를 바꾼다
# x에 -1을 곱한다
# 기준점 좌표를 더한다


def rolling(args):
  x, y, gx, gy = args
  x, y = x - gx, y - gy
  x, y = y, x
  x *= -1
  x, y = x + gx, y + gy
  return ([x, y])


n = int(input())
ors = [list(map(int,input().split())) for _ in range(n)]
move = [[1,0],[0,-1],[-1,0],[0,1]]
assem = []
for o in ors:
  d, g = o[2], o[3]
  xys = [[o[0], o[1]],[o[0]+move[d][0], o[1]+move[d][1]]]
  for gi in range(g):
    nxys = []
    for i in range(len(xys)-2,-1,-1):
      x,y = xys[i]
      nxys.append(rolling([x,y,xys[-1][0], xys[-1][1]]))
    xys = xys + nxys
  assem = assem + xys

ans = 0
digs = [[0]*101 for _ in range(101)]
for x,y in assem:
  digs[y][x] = 1
for i in range(100):
  for j in range(100):
    if digs[i][j] and digs[i+1][j] and digs[i][j+1] and digs[i+1][j+1]:
      ans += 1

print(ans)