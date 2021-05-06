n, m = map(int, input().split())
pan = [list(map(int, input().split())) for _ in range(n)]


_max = 0
# 일자막대
for i in range(n):
  for j in range(m - 3):
    _max = max(_max, pan[i][j] + pan[i][j + 1] + pan[i][j + 2] + pan[i][j + 3])
for i in range(n - 3):
  for j in range(m):
    _max = max(_max, pan[i][j] + pan[i + 1][j] + pan[i + 2][j] + pan[i + 3][j])
    
# 네모
for i in range(n - 1):
  for j in range(m - 1):
    _max = max(_max, pan[i][j] + pan[i][j + 1] + pan[i + 1][j] + pan[i + 1][j + 1])

# ㄴ
for i in range(n - 1):
  for j in range(m - 2):
    _max = max(_max, pan[i][j] + pan[i][j + 1] + pan[i][j + 2] + pan[i + 1][j + 2])
    _max = max(_max, pan[i][j] + pan[i][j + 1] + pan[i][j + 2] + pan[i + 1][j])
    _max = max(_max, pan[i + 1][j] + pan[i + 1][j + 1] + pan[i + 1][j + 2] + pan[i][j + 2])
    _max = max(_max, pan[i + 1][j] + pan[i + 1][j + 1] + pan[i + 1][j + 2] + pan[i][j])
for i in range(n - 2):
  for j in range(m - 1):
    _max = max(_max, pan[i][j] + pan[i + 1][j] + pan[i + 2][j] + pan[i + 2][j + 1])
    _max = max(_max, pan[i][j] + pan[i + 1][j] + pan[i + 2][j] + pan[i][j + 1])
    _max = max(_max, pan[i][j + 1] + pan[i + 1][j + 1] + pan[i + 2][j + 1] + pan[i + 2][j])
    _max = max(_max, pan[i][j + 1] + pan[i + 1][j + 1] + pan[i + 2][j + 1] + pan[i][j])
# 지그
for i in range(n - 1):
  for j in range(m - 2):
    _max = max(_max, pan[i][j] + pan[i][j + 1] + pan[i + 1][j + 1] + pan[i + 1][j + 2])
    _max = max(_max, pan[i + 1][j] + pan[i + 1][j + 1] + pan[i][j + 1] + pan[i][j + 2])
for i in range(n - 2):
  for j in range(m - 1):
    _max = max(_max, pan[i][j]+ pan[i+1][j]+pan[i+1][j+1]+pan[i+2][j+1])
    _max = max(_max, pan[i][j+1]+ pan[i+1][j]+pan[i+1][j+1]+pan[i+2][j])
# 화살표
for i in range(n - 1):
  for j in range(m - 2):
    _max = max(_max, pan[i][j] + pan[i][j + 1] + pan[i][j + 2] + pan[i + 1][j + 1])
    _max = max(_max, pan[i + 1][j] + pan[i + 1][j + 1] + pan[i + 1][j + 2] + pan[i][j + 1])
for i in range(n - 2):
  for j in range(m - 1):
    _max = max(_max, pan[i][j] + pan[i + 1][j] + pan[i + 2][j] + pan[i + 1][j + 1])
    _max = max(_max, pan[i][j + 1] + pan[i + 1][j + 1] + pan[i + 2][j + 1] + pan[i+1][j])
    
print(_max)