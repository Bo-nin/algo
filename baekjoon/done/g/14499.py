n, m, y, x, k = map(int,input().split())

pan = [list(map(int,input().split())) for _ in range(n)]
orders = list(map(int,input().split()))
directions = [[],[0,1],[0,-1],[-1,0],[1,0]]
col = [0,0,0]
row = [0,0,0]

for order in orders:
  newCol = []
  newRow = []
  
  y += directions[order][0]
  x += directions[order][1]
  if y>=0 and y<=n-1 and x>=0 and x<=m-1:
    if order == 1:
      newCol = [col[0],row[2],col[2]]
      newRow = [col[1],row[0],row[1]]
    elif order == 2:
      newCol = [col[0],row[0],col[2]]
      newRow = [row[1], row[2], col[1]]
    elif order == 3:
      newCol = [col[1],col[2],row[1]]
      newRow = [row[0], col[0], row[2]]
    elif order == 4:
      newCol = [row[1],col[0],col[1]]
      newRow = [row[0],col[2],row[2]]
    row = newRow
    col = newCol


    if pan[y][x] == 0:
      pan[y][x] = col[1]
    else:
      col[1] = pan[y][x]
      pan[y][x] = 0
    print(row[1])
  else:
    y -= directions[order][0]
    x -= directions[order][1]
  # for p in pan:
  #   print(*p)
  # print()
  # print(*row)
  # print()
  # print(*col)
  # print()