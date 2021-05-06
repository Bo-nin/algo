def sol(n, coffeeTimes):
  coffeeSlot = [0]*n
  coffeeSlotOrderIdx = [-1]*n
  
  cnt = 0
  ordered = 0
  if n >= len(coffeeTimes):
    todo

  coffeeSlot = coffeeTimes[0:n]
  coffeeSlotOrderIdx = range(n)
  ordered = n-1
  res = []
  while (ordered < len(coffeeTimes)):
    cnt = min(coffeeSlot)
    tmpRes = []
    for i in range(n):
      if coffeeSlot[i] == cnt:
        tmpRes.append(coffeeSlotOrderIdx[i]+1)
        ordered += 1
        coffeeSlotOrderIdx[i] = ordered
        coffeeSlot[i] += coffeeTimes[ordered]
    res += sorted(tmpRes)

  return (max(coffeeSlot), res)