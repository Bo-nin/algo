# 미세먼지 멈춰!
import copy
move = [[-1,0],[1,0],[0,-1],[0,1]]

def diffusion(room):
  newRoom = list(copy.deepcopy(room))
  for i in range(len(room)):
    for j in range(len(room[0])):
      if room[i][j] > 4:
        effCnt = 0
        e = room[i][j] // 5
        for m in move:
          ni, nj = i+m[0], j+m[1]
          if ni >= 0 and ni < len(room) and nj >= 0 and nj < len(room[0]):
            if room[ni][nj] != -1:
              newRoom[ni][nj] += e
              effCnt += 1
        newRoom[i][j] -= e*effCnt
  return newRoom

def circulation(room, airPurifier):
  # 움직이고 땡긴다
  
  upm = []
  for _ in range(airPurifier[0]):
    upm.append(move[0])
  for _ in range(len(room[0])-1):
    upm.append(move[3])
  for _ in range(airPurifier[0]):
    upm.append(move[1])
  for _ in range(len(room[0])-1):
    upm.append(move[2])
  dpm = []
  for _ in range(len(room) - airPurifier[1] -1):
    dpm.append(move[1])
  for _ in range(len(room[0])-1):
    dpm.append(move[3])
  for _ in range(len(room) - airPurifier[1] -1):
    dpm.append(move[0])
  for _ in range(len(room[0])-1):
    dpm.append(move[2])
  mvm = [upm,dpm]
  for i in range(2):
    r,c = airPurifier[i], 0
    for j in range(len(mvm[i])):
      if j == len(mvm[i])-1:
        room[r][c] = 0
        break
      r += mvm[i][j][0]
      c += mvm[i][j][1]
      room[r][c] = room[r + mvm[i][j+1][0]][c + mvm[i][j+1][1]]

  

def _17144():
  r, c, t = map(int,input().split())
  room = [list(map(int,input().split())) for _ in range(r)]
  airPurifier = []

  for i in range(r):
    if room[i][0] == -1:
      airPurifier.append(i)

  # print()
  for _ in range(t):
    room = diffusion(room)
    # for i in range(r):
    #   print(*room[i])
    # print()
    circulation(room, airPurifier)
    # for i in range(r):
    #   print(*room[i])
    # print()
  tot = 2
  for i in range(r):
    for j in range(c):
      tot += room[i][j]
  return tot
print(_17144())
