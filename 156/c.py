n = int(input())
X = list(map(int, input().split()))

INF = 10**8
ans = INF
# 愚直にやるパターン


for i in range(1, 101): # 考慮する座標
    cnt = 0
    for x in X:
        cnt += (i - x)**2
    ans = min(ans, cnt)

print(ans)

