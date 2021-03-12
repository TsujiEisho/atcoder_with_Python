INF = 10**10; ans = INF

n, m , x = map(int, input().split())

A = [[] for i in range(n)]; c=[0]*n

for i in range(n):
    c_as = list(map(int, input().split()))
    c[i], A[i] = c_as[0], c_as[1:]

# 買う本の集合をsとして探索開始。
for s in range(0, 1 << n):
    smart = [0]*m
    cost_sum=0
    # いくつ買うか。
    for i in range(n):
        # 買わない場合
        if (s >> i)%2 ==0:
            continue
        # 買うとき
        cost_sum += c[i]
        for j in range(m):
            smart[j] += A[i][j]
    ok = True
    for i in range(m):
        if smart[i] < x:
            ok = False
    if ok:
        ans = min(ans, cost_sum)

if ans == INF:
    ans = -1
print(ans)