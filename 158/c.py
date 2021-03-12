a, b = map(int, input().split())

pay=0
while True:
    # print(pay, pay*0.08, pay*0.1)
    if (int(pay*0.08) == a) and (int(pay*0.1) == b):
        print(pay)
        exit()
    pay += 1

    if pay >= 10**6:
        print(-1)
        exit()