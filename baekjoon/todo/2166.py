# 2166
# 다각형의 면적
# gold 5


n = int(input())
arr = [list(map(int,input().split())) for _ in range(n)]
arr.append(arr[0])

lt, rt = 0, 0
for i in range(n):
  lt += (arr[i][0] * arr[i+1][1])
  rt += (arr[i][1] * arr[i+1][0])
print(round(abs(rt-lt)/2,1))