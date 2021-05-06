import itertools

n = int(input())
arr = list(map(int,input().split()))
ope = list(map(int,input().split()))
operators = []
for i in range(4):
  operators = operators + [i]*ope[i]
operatorSet = list(set(itertools.permutations(operators,n-1)))
_min = 1000000000
_max = -1000000000
while(operatorSet):
  operators = operatorSet.pop()
  res = arr[0]
  cnt = 1
  for operator in operators:
    if operator == 0:
      res += arr[cnt]
    elif operator == 1:
      res -= arr[cnt]
    elif operator == 2:
      res *= arr[cnt]
    else:
      if res < 0:
        res = (res*(-1)//arr[cnt])*(-1)
      else:
        res = res//arr[cnt]
    cnt += 1
  _min = min([_min, res])
  _max = max([_max, res])
print(_max)
print(_min)