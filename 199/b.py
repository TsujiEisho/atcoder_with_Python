n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
amax , amin = max(A), min(A)
bmax , bmin = max(B), min(B)

if bmin - amax >= 0:
    print(bmin - amax +1)
else:
    print(0)

