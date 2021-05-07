c = int(input())
arr = [list(map(int,input().split())) for _ in range(c)]
for scores in arr:
  count = 0
  total = 0
  for score in scores[1:]:
    total += score
  avg = total/scores[0]
  for score in scores[1:]:
    if score > avg:
      count += 1
  res = f'{round(count/scores[0]*100,3)}'
  while(len(res.split('.')[1]) < 3):
    res += '0'
  print(f'{res}%')