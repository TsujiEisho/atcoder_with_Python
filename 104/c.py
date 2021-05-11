d, g = map(int, input().split())
pc = [list(map(int, input().split())) for i in range(d)]
ans = 10**7

for bit in range(1 << d):
    count = 0 # 問題数
    sum = 0 # 点数
    nokori = set(range(1, d+1))

    for i in range(d):
        if bit & (1 << i):
            sum += pc[i][0] * (i+1) * 100 + pc[i][1]
            count += pc[i][0]
            nokori.discard(i + 1)

    # sumがg点未満ならばnokoriから最も大きいものを一つ解く。
    if sum < g:
        use = max(nokori)
        n = min(pc[use-1][0], -(-(g - sum) // (use * 100))) # 中途半端に解く問題をいくら解くかはこう書ける。
        count += n
        sum += n*use*100

    if sum >= g:
        ans = min(ans, count)
print(ans)
