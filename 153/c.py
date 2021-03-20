n, k = map(int, input().split())
h = list(map(int, input().split()))
h.sort(reverse=True)
h = h[k:] # 実質的に攻撃で倒さなければならないモンスターの体力の集合

print(sum(h))