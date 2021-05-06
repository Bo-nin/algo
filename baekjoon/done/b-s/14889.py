import itertools

def fun(n, arr):
  coms = list(map(list, itertools.combinations(range(n), n//2)))
  result = 10000000000
  for start in coms:
    link = [x for x in range(n) if x not in start]
    startValue = 0
    linkValue = 0
    for i in start:
      for j in start:
        startValue += arr[i][j]
    for i in link:
      for j in link:
        linkValue += arr[i][j]
    result = min([abs(startValue-linkValue), result])
    if result == 0:
      return result
  return result
n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
print(fun(n, arr))