N = int(input())
s = str(input())


import itertools
import math

ans = 0
u = itertools.combinations(s, 3)
for index in u:
    print(index)

print(ans)



