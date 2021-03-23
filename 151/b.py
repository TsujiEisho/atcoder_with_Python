n, k, m= map(int, input().split())
A = list(map(int, input().split()))
x = sum(A)

ans = m*n - x
if ans > k:
    print(-1)
elif ans<0:
    print(0)
else:
    print(ans)