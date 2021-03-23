n, m = map(int, input().split())
"""
問題がAC済みかどうかのリストを作る。
ACしていない問題のペナルティを考慮する
"""

checkAC = [0 for i in range(n+1)]
checkWA = [0 for i in range(n+1)]


for _ in range(m):
    p, s = map(str, input().split())
    p = int(p)

    # その問題をACしていないときのことを考える。
    if checkAC[p] == 0:
        if s == "AC":
            checkAC[p] = 1
        elif s == "WA":
            checkWA[p] += 1

# print(checkWA)

WA = 0
for i in range(n+1):
    if checkAC[i]:
        WA += checkWA[i]
print(sum(checkAC), WA)
