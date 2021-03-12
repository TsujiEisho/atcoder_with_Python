n, m = map(int,input().split())
A=list(map(int, input().split()))

# 宿題をすべて終わらせるのに必要な日数
s = sum(A)
if s > n:
    print(-1)
else:
    print(n-s)
