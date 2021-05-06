# 최대 n잔 동시추출
# 만들커피 M잔 커피는 1~M번호

# 추출기 없으면 주문 대기

def solution(n, coffeeTimes):
  coffeeSlot = [0]*n
  coffeeSlotOrderIdx = [-1]*n
  
  cnt = 0
  ordered = 0
  res = []
  if n >= len(coffeeTimes):
    coffeeTiemsIdx = coffeeTimes[:]
    coffeeTimes.sort()
    for coffeeTime in coffeeTimes:
      idx = coffeeTiemsIdx.index(coffeeTime)
      res.append(idx + 1)
      coffeeTiemsIdx[idx] = 0
    return res

  coffeeSlot = coffeeTimes[0:n]
  coffeeSlotOrderIdx = list(range(n))
  ordered = n-1
  while (ordered < len(coffeeTimes)):
    cnt = min(coffeeSlot)
    tmpRes = []
    coffeeSlot.index(cnt)
    for i in range(n):
      if ordered == len(coffeeTimes):
        break
      elif coffeeSlot[i] == cnt:
        tmpRes.append(coffeeSlotOrderIdx[i]+1)
        coffeeSlotOrderIdx[i] = ordered
        print(i,ordered)
        coffeeSlot[i] += coffeeTimes[ordered]
        ordered += 1
    res += sorted(tmpRes)
  left = []
  for _ in range(len(coffeeTimes) - len(res)):
    idx = coffeeSlot.index(max(coffeeSlot))
    left.append(coffeeSlotOrderIdx[idx]+1)
    coffeeSlot[idx] = 0
  res += left
  return res