n, a, b = map(int, input().split())

uw = n%(a+b)
u = n//(a+b)


if uw>a:
    uw = a
print(u*a + uw)