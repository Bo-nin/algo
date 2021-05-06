import time


n = int(input())
gamePan = [['■']*(n+2)] + [['■']+['□']*n+['■'] for _ in range(n)] + [['■']*(n+2)]
snakeBody = [[1,1]]
gamePan[1][1] = '▲'
k = int(input())
apples = [list(map(int,input().split())) for _ in range(k)]
for apple in apples:
  gamePan[apple[0]][apple[1]] = '♠'
l = int(input())
orders = [list(input().split()) for _ in range(l)]

#상우하좌
directions = [[-1,0],[0,1],[1,0],[0,-1]]
directionIndex = 1
second = 1
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
for game in gamePan:
  print(*game)
print ('press \'enter\' to start')
input()
while(1):
  print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
  for game in gamePan:
    print(*game)
  print(second)
  second += 1
  snakeBody.append([snakeBody[-1][0]+directions[directionIndex][0], snakeBody[-1][1]+directions[directionIndex][1]])
  y,x = snakeBody[-1][0],snakeBody[-1][1]
  if gamePan[y][x] == '■' or gamePan[y][x] == '▲':
    gamePan[y][x] ='X'
    break
  elif gamePan[y][x] == '□':
    delY, delX = snakeBody.pop(0)
    gamePan[delY][delX] = '□'
  gamePan[y][x] = '▲'
  if len(orders) == 0:
    pass
  elif int(orders[0][0]) == second:
    if orders[0][1] == 'L':
      directionIndex -= 1
      if directionIndex < 0:
        directionIndex = 3
    else:
      directionIndex += 1
      if directionIndex > 3:
        directionIndex = 0
    orders.pop(0)
  
  time.sleep(0.4)
time.sleep(0.4)
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
for game in gamePan:
  print(*game)
print(f'---GAMEOVER---\n score: {second}')





# #맵보기
# for game in gamePan:
#   print(*game)