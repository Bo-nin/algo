# 9252
# LCS 2

# 공통부분수열중 가장 긴거?
# 부분집합 다구하면 1000글자 무조건 터짐

# 2^1000 ? 미쳤어

# 

import sys

input = sys.stdin.readline

lcs1 = "0" + input().split()[0]
lcs2 = "1" + input().split()[0]
# lcs1이 메인 lcs2가 비교군
arrs = [[0]*len(lcs2) for _ in range(len(lcs1))]
print(lcs1, lcs2)
for i in range(1,len(lcs1)):
  for j in range(1,len(lcs2)):
    print(i,j)
    
    if arrs[i][j] != 0 and (arrs[i][j] == arrs[i-1][j] or arrs[i][j] == arrs[i][j-1]):
      continue
    if arrs[i-1][j] > arrs[i][j-1]:
      arrs[i][j] = arrs[i-1][j]
      if lcs1[i] == lcs2[j]:
        arrs[i][j] += 1
        for k in range(i, len(lcs1)):
          arrs[k][j] = arrs[i][j]
        for l in range(j, len(lcs2)):
          arrs[i][l] = arrs[i][j]
    else :
      arrs[i][j] = arrs[i][j-1]
      if lcs1[i] == lcs2[j]:
        arrs[i][j] += 1
        for k in range(i, len(lcs1)):
          arrs[k][j] = arrs[i][j]
        for l in range(j, len(lcs2)):
          arrs[i][l] = arrs[i][j]
    for a in range(len(arrs)):
      print(*arrs[a])
    print()
    
print(arrs[-1][-1])

if arrs[-1][-1] != 0:
  i, j = len(lcs1)-1, len(lcs2)-1
  ans = ""
  while(i > 0 and j > 0):
    if arrs[i-1][j] == arrs[i][j]:
      i -= 1
      continue
    if arrs[i][j-1] == arrs[i][j]:
      j -= 1
      continue
    ans = lcs1[i] + ans
    i -= 1
    j -= 1
  print(ans)

for i in range(len(arrs)):
  print(*arrs[i])
# 역추적접근 했는데 왜 실패뜨는거지
# 문자열들이 중복체크된거 처리
# 중복연속들 어떻게 처리하지?
# 하나의 행 혹은 열에서 증가가 이미 일어났다면 다음 행 or 열로 넘어가기