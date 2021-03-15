n = int(input())
X = list(map(int, input().split()))

# 約数を列挙してリストに格納する
def func(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

U = []
for i in X:
    U.append(func(i)[1])

Z=list(set(U))

ans=1
for i in Z:
    ans *= i

print(ans)

# for i in range(2, 51):
#     print(i, func(i))