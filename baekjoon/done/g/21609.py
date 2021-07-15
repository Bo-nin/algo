# 21609
# 상어 중학교
# gold 2
import sys
import copy
import collections
import time
# input = sys.stdin.readline
r = [-1,1,0,0]
c = [0,0,-1,1]
n, m = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(n)]
  
def deleteBlock(tmp_arr, i, j, safe):
  queue = collections.deque()
  queue.append([i,j])
  color = tmp_arr[i][j]
  tmp_arr[i][j] = -2
  block_num = 1
  rainbow_num = 0
  while(queue):
    i, j = queue.popleft()
    for idx in range(4):
      ni, nj = i+r[idx], j+c[idx]
      if ni >= 0 and ni < len(tmp_arr) and nj >= 0 and nj < len(tmp_arr):
        if tmp_arr[ni][nj] == 0 or tmp_arr[ni][nj] == color:
          if tmp_arr[ni][nj] == color or safe:
            tmp_arr[ni][nj] = -2
          else:
            tmp_arr[ni][nj] = -3
          queue.append([ni,nj])
          block_num += 1
  for i in range(n):
    for j in range(n):
      if tmp_arr[i][j] == -3:
        rainbow_num += 1
        tmp_arr[i][j] = 0
  
  return [block_num, rainbow_num]

def gravity(arr, j):
  empty = collections.deque()
  for i in range(n-1,-1,-1):
    if arr[i][j] == -2:
      empty.append(i)
    elif arr[i][j] == -1:
      empty = collections.deque()
    elif empty:
      arr[empty.popleft()][j] = arr[i][j]
      arr[i][j] = -2
      empty.append(i)

def rotate(arr):
  n = len(arr)
  new_arr = [[0]*n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      new_arr[n-j-1][i] = arr[i][j]
  return new_arr

tmp_arr = copy.deepcopy(arr)
play_key = True
score = 0
while(play_key) :
  play_key = False
  block_box = []
  for i in range(n):
    for j in range(n):
      if tmp_arr[i][j] > 0:
        block = deleteBlock(tmp_arr,i,j, False)
        if block[0] > 1:
          block_box.append([block,i,j])
          play_key = True
  delete_block = [[0,0]]
  for block in block_box:
    if block[0][0] >= delete_block[0][0]:
      if block[0][0] > delete_block[0][0]:
        delete_block = block
      elif block[0][1] > delete_block[0][1]:
        delete_block = block
      elif block[0][1] == delete_block[0][1]:
        if block[1] > delete_block[1]:
          delete_block = block
        elif block[1] == delete_block[1]:
          if block[2] == delete_block[2]:
            delete_block = block
        

  if len(delete_block) > 1:
    deleteBlock(arr, delete_block[1], delete_block[2], True)
    if delete_block[0][0] > 1:
      score += delete_block[0][0]**2

  for j in range(n):
    gravity(arr, j)
  arr = rotate(arr)
  for j in range(n):
    gravity(arr, j)

  print()
  for i in range(n):
    print(*arr[i])
  print()
  print(score, delete_block[0][0]**2)

  tmp_arr = copy.deepcopy(arr)
print(score)