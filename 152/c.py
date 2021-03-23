n = int(input())
P = list(map(int, input().split()))

# p_jまでの最小値をMとしてメモしておく。
# もしそれよりp_iが大きければ条件に当てはまらない。
ans = 0
M = P[0] # マイナス数値で初期化しておく
for P_i in P:
    # print(P_i)
    if P_i <= M:
        ans += 1
    M = min(P_i, M)

print(ans)

