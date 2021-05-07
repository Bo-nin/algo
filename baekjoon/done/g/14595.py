# 14959 (g2)

# 방은 1부터 시작
n = int(input())
m = int(input())
bigs = [list(map(int, input().split())) for _ in range(m)]
# array 쓰면 무조건 터짐

blinks = []
for big in bigs:
  ef = []
  for i in range(len(blinks)):
    #완전히 감싸는 경우
    if big[0] <= blinks[i][0] and big[1] >= blinks[i][1]:
      ef.append(i)
      blinks[i] = big[:]
    #부분만 겹치는경우
    elif not (big[0] > blinks[i][1] or big[1] < blinks[i][0]):
      ef.append(i)
      blinks[i] = [min([big[0], blinks[i][0]]), max([big[1], blinks[i][1]])]
  #겹치는게 없는경우
  if not ef:
    i = 0
    for blink in blinks:
      if big[1] < blink[0]:
        break
      i += 1
    blinks.insert(i,big[:])
  #겹치는 방들 하나로 병합
  else:
    ap = [ blinks[ef[0]][0], blinks[ef[-1]][1] ]
    for ei in reversed(ef):
      blinks.pop(ei)
    blinks.insert(ef[0], ap)
  # print(ef, blinks)
mergedRoomNumber = 0
for blink in blinks:
  mergedRoomNumber += (blink[1]-blink[0])

print(n-mergedRoomNumber)