# 9252
# LCS 2

# 공통부분수열중 가장 긴거?
# 부분집합 다구하면 1000글자 무조건 터짐

# 2^1000 ? 미쳤어

# 

import sys

input = sys.stdin.readline

lcs1 = "0" + input()
lcs2 = "0" + input()
# lcs1이 메인 lcs2가 비교군


arrs = [[0]*len(lcs2) for _ in range(len(lcs1))]

for i in range(len(lcs1)):
  for j in range(len(lcs2)):
    arrs[i][j] = max(arrs[i-1][j], arrs[i][j-1])
    if lcs1[i] == lcs2[j]:
      arrs[i][j] += 1
print(arrs[-1][-1])

for i in range(len(arrs)):
  print(*arrs[i])