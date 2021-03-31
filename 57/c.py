n = int(input())

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
INF = 10**7
ans = INF
N = func(n)
# print(N)
lengthN = len(N)


if lengthN % 2 == 0:
    for i in range(lengthN):
        # print(N[i], N[-i])
        a, b = len(str(N[i])), len(str(N[-i-1]))
        _ = max(a, b)
        # print(a, b)
        ans = min(ans, _)
else:
    for i in range((lengthN-1)//2):
        # print(N[i], N[-i-1])
        a, b = len(str(N[i])), len(str(N[-i-1]))
        _ = max(a, b)
        ans = min(ans, _)
        # print(str(N[lengthN//2]))
    ans = min(ans, len(str(N[lengthN//2])))
print(ans)