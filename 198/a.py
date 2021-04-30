n = int(input())
if n<2:
    print(0)
    exit()

import math
def permutations_count(n, r):
    return math.factorial(n) // math.factorial(n - r)

print(permutations_count(n-1, 1))

