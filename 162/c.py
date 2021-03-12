k = int(input())

from math import gcd

gcd_sum = [0] * 201
ans = 0

for i in range(1, k+1):
    for j in range(1, k+1):
        gcd_sum[i] += gcd(i,j)

print(gcd_sum)


for a in range(1,k+1):
    for b in range(1,k+1):
        g = gcd(a,b)
        print(g)
        ans += gcd_sum[g]

print(ans)

import itertools
U = list(range(1, k+1))
x = itertools.combinations_with_replacement(U, 3)
for i in x:
    a, b, c = i
    print(a, b, c)