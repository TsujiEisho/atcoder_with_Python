n = int(input())

# 約数の数を求める関数
def func(n):
    a = 0
    i = 1
    while i*i <= n:
        if n % i == 0:
            a += 1
            if i != n // i:
                a += 1
        i += 1
    return a

ans = 0
for i in range(1, n+1):
    if i%2 == 1 and func(i) == 8:
        ans += 1

print(ans)