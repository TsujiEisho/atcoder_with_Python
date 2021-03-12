h, w = map(int, input().split())

if h== 1 or w==1:
    print(1)
    exit()

if w%2 == 0:
    print(w//2 * h)

elif w%2 == 1:
    p = w//2 + 1
    q = w - p

    if h%2 == 0:
        print((p+q)*h//2)


    elif h%2 == 1:
        hodd = h//2+1
        heven = h-hodd
        print(p*hodd + q*heven)

