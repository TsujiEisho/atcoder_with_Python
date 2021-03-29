n = int(input())
A = list(map(int, input().split()))
INF = 10**7
ans = INF
for i in range(1, len(A)):
    L = A[:i]
    R = A[i:]


    for i in range(len(L)):
        L[i] = bin(L[i])
    l = L[0]
    for j in range(1, len(L)):
        l |= L[j]

    for i in range(len(R)):
        R[i] = bin(R[i])
    r = R[0]
    for j in range(1, len(R)):
        r |= R[j]

    print(L, R, l, r)


