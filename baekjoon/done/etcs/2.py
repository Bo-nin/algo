

def solution(m):
  holsum = [1]
  hollist = [1]
  for i in range(3, m+1, 2):
    holsum.append(holsum[-1] + i)
    hollist.append(i)
    if holsum[-1] >= m :
      break
  key = holsum[-1] - m

  if (key %2 == 1):
    hollist.remove(key)

  else :
    if (key//2)%2 == 1:
      hollist.remove(key//2-2)
      hollist.remove(key//2+2)
    else:
      hollist.remove(key//2-1)
      hollist.remove(key//2+1)

  print(hollist)
  print(sum(hollist))
solution(1111111)
