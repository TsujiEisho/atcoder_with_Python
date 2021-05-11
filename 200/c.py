from math import factorial
import collections
def combinations_count(n, r):
    ''' 組み合わせ '''
    return factorial(n) // (factorial(n - r) * factorial(r))

n = int(input())
A = list(map(int, input().split()))
A = [i%200 for i in A]
c = 0
U = collections.Counter(A)
for i in U.values():
    if i>1:
        c+= combinations_count(i, 2)

print(c)








