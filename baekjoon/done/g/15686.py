#부르트포스
import itertools

def _15686():
  n, m = map(int,input().split())
  arr = [list(map(int,input().split())) for _ in range(n)]

  chickens = []
  houses = []
  for i in range(n):
    for j in range(n):
      if arr[i][j] == 1:
        houses.append([i,j])
      elif arr[i][j] == 2:
        chickens.append([i,j])
  coms = list(itertools.combinations(chickens, m))
  _min = 999999999
  for com in coms:
    tmpsMin = 0
    for house in houses:
      if tmpsMin >= _min:
        break
      tmp = 1000
      for co in com:
        tmp = min(tmp, abs(house[0]-co[0])+abs(house[1]-co[1]))
      tmpsMin += tmp
    _min = min(_min, tmpsMin)
  return _min

print(_15686())
