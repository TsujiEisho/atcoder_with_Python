n, m, x = map(int, input().split())
c = [0]*n; A=[[]for i in range(n)]
for i in range(n):
    W = list(map(int, input().split()))
    c[i] = W[0]; A[i] = W[1:]

"""
bit全探索を行う。
本全体の集合をs，i冊目の本とj番目のアルゴについて考える。
1つの本の買い方の通りにつき，アルゴの理解度としてsmartに格納。
smartの各要素がxを超えていれば，costsumを計算しその最小値をansに格納。
ansはINF=10**10で初期化しておく。
"""

INF = 10**10; ans =INF

for s in range(2**n):
    costsum=0
    smart = [0]*m
    for i in range(n):
        # i番目の本を買わない場合
        if (s>>i) & 1:    continue

        # 買う場合
        costsum += c[i]

        for j in range(m):
            smart[j] += A[i][j]

        # 理解度の判定
        ok = True
        for _ in smart:
            if _ < x:
                ok = False
    if ok:
        ans = min(ans, costsum)

if ans==INF:
    ans = -1
print(ans)