n = int(input())
P = tuple(map(int, input().split()))
Q = tuple(map(int, input().split()))

import itertools
U = list(range(1, n+1))
e = itertools.permutations(U, n)
cnt = 1; p=0; q=0
for index in e:
    if index == P:
        p = cnt
    if index == Q:
        q = cnt
    cnt += 1

print(abs(p-q))
