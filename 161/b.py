n, m = map(int, input().split())

A = list(map(int, input().split()))

cnt=0
for i in A:
    if i >= sum(A) / (4*m):
        cnt += 1
if cnt >= m:
    print("Yes")
else:
    print("No")