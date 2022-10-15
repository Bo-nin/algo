
def mergeBalls (balls):
    tm = 0
    ts = 0
    td = 0
    for ball in balls:
        tm += ball[2]
        ts += ball[3]
        td += ball[4] % 2
    nm = tm//5
    if nm == 0:
        return []
    ns = ts//len(balls)
    newBalls = []
    for i in range(4):
        if td == 0 or td == len(balls):
            newBalls.append([balls[0][0], balls[0][1], nm, ns, i*2])
        else:
            newBalls.append([balls[0][0], balls[0][1], nm, ns, i*2+1])
    return newBalls

def main():
    n, m, k = list(map(int, input().split()))
    fireballs = [list(map(int, input().split())) for _ in range(m)]
    for ball in fireballs:
        ball[0] -= 1
        ball[1] -= 1
    # r,c ,질량, 속도, 방향
    # 방향은 시계 0 - 7
    d = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]

    # pan 초기화 된 상태

    pan = [[[] for _ in range(n)] for _ in range(n)]

    for _ in range(k):
        # 이동
        for ball in fireballs:
            ball[0] = ((ball[0] + ball[3] * d[ball[4]][0]) + n) % n
            ball[1] = ((ball[1] + ball[3] * d[ball[4]][1]) + n) % n
            pan[ball[0]][ball[1]].append(ball)
        fireballs = []
        for r in range(n):
            for c in range(n):
                if len(pan[r][c]) > 1:
                    tmp = mergeBalls(pan[r][c])
                    fireballs.extend(tmp)
                    pan[r][c] = []
                elif len(pan[r][c]) == 1:
                    fireballs.extend(pan[r][c])
                    pan[r][c] = []
    res = 0
    for ball in fireballs:
        res += ball[2]
    print(res)


main()