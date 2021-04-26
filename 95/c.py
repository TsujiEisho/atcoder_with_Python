a, b, c, x, y = map(int, input().split())

"""
cを2個買うとa,bをひとつづつ買ったのと同じ。
決めつけでやる。
cをk個買うとすると，aはmax(x-k, 0) bはmax(b-k, 0)
"""
c *= 2
INF = 10**6
ans = INF
for k in range(max(x, y)+1):
    curans = c*k + max(x-k, 0)*a + max(y-k, 0)*b
    ans = min(ans, curans)

print(ans)