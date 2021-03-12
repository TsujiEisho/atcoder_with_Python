n, k = map(int, input().split())

#そのままやるとTLEになるのである程度nを小さくしておく。
u = n//k
n -= u*k


pren = n
while True:
    n = abs(pren-k)
    if n >= pren:
        print(pren)
        exit()
    pren = n