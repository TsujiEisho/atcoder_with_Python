n, m = map(int, input().split())

from scipy.special import comb
A = comb(n, 2, exact=True) # nだけ

B = comb(m, 2, exact=True) # mだけ

print(A+B)
