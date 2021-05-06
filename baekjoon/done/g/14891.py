topnees = [list(map(int, list(input()))) for _ in range(4)]
k = int(input())
orders = [list(map(int, input().split())) for _ in range(k)]
for i in range(k):
  orders[i][0] = orders[i][0]-1
pointers = [0, 0, 0, 0]

# n극은 0 s극은 1
# 바뀌는 점은 pointer +2랑 +6
# 방향은 그대로 포인터에 반영

def check(order, direction, idx):
  # print(f'{idx}번 톱니가 {direction}방향으로 {order}시계방향으로 돈다')
  if direction == -1:
    if idx != 0:
      if topnees[idx][(pointers[idx] + 6) % 8] != topnees[idx - 1][(pointers[idx - 1] + 2) % 8]:
        check(-1*order, -1, idx-1)
  if direction == 1:
    if idx != 3:
      if topnees[idx][(pointers[idx] + 2) % 8] != topnees[idx + 1][(pointers[idx + 1] + 6) % 8]:
        check(-1*order, 1, idx+1)
  pointers[idx] = (pointers[idx] - order + 8) % 8
  

def printer():
  sortedIndex = [list(range(8)) for _ in range(4)]
  for i in range(4):
    for j in range(8):
      if sortedIndex[i][j] == pointers[i]:
        sortedIndex[i] = sortedIndex[i][j:] + sortedIndex[i][:j]
          
  print(f'  {topnees[0][sortedIndex[0][0]]}  ',end=' ')
  print(f'  {topnees[1][sortedIndex[1][0]]}  ',end=' ')
  print(f'  {topnees[2][sortedIndex[2][0]]}  ',end=' ')
  print(f'  {topnees[3][sortedIndex[3][0]]}  ')
  print(f' {topnees[0][sortedIndex[0][7]]} {topnees[0][sortedIndex[0][1]]} ', end=' ')
  print(f' {topnees[1][sortedIndex[1][7]]} {topnees[1][sortedIndex[1][1]]} ', end=' ')
  print(f' {topnees[2][sortedIndex[2][7]]} {topnees[2][sortedIndex[2][1]]} ', end=' ')
  print(f' {topnees[3][sortedIndex[3][7]]} {topnees[3][sortedIndex[3][1]]} ')
  print(f'{topnees[0][sortedIndex[0][6]]}   {topnees[0][sortedIndex[0][2]]}', end=' ')
  print(f'{topnees[1][sortedIndex[1][6]]}   {topnees[1][sortedIndex[1][2]]}', end=' ')
  print(f'{topnees[2][sortedIndex[2][6]]}   {topnees[2][sortedIndex[2][2]]}', end=' ')
  print(f'{topnees[3][sortedIndex[3][6]]}   {topnees[3][sortedIndex[3][2]]}')
  print(f' {topnees[0][sortedIndex[0][5]]} {topnees[0][sortedIndex[0][3]]} ',end=' ')
  print(f' {topnees[1][sortedIndex[1][5]]} {topnees[1][sortedIndex[1][3]]} ',end=' ')
  print(f' {topnees[2][sortedIndex[2][5]]} {topnees[2][sortedIndex[2][3]]} ',end=' ')
  print(f' {topnees[3][sortedIndex[3][5]]} {topnees[3][sortedIndex[3][3]]} ')
  print(f'  {topnees[0][sortedIndex[0][4]]}  ', end=' ')
  print(f'  {topnees[1][sortedIndex[1][4]]}  ', end=' ')
  print(f'  {topnees[2][sortedIndex[2][4]]}  ', end=' ')
  print(f'  {topnees[3][sortedIndex[3][4]]}  ')
# printer()
for idx, order in orders:
  # left
  # print()
  # print(f'{idx}번 톱니를 중심으로 {order}시계방향으로 돈다')
  if idx != 0:
    if topnees[idx][(pointers[idx] + 6) % 8] != topnees[idx - 1][(pointers[idx -1] + 2) % 8]:
      check(-1*order, -1, idx-1)
  if idx != 3:
    if topnees[idx][(pointers[idx] + 2) % 8] != topnees[idx + 1][(pointers[idx +1] + 6) % 8]:
      check(-1*order, 1, idx+1)
  pointers[idx] = (pointers[idx] - order + 8) % 8
  # printer()
res = 0
for i in range(4):
  if topnees[i][pointers[i]] == 1:
    res += 2 ** i

print(res)