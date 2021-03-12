A =[[] for i in range(3)]
for i in range(3):
    A[i] = list(map(int, input().split()))
n = int(input())

# ビンゴのものを1として格納。
D = [[0, 0, 0] for i in range(3)]
for b in range(n):
    x = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == x:
                D[i][j] = 1

# 横と縦のビンゴ判定。3ならビンゴ。
tate = [0, 0, 0]
for i in range(3):
    yoko=0
    for j in range(3):
        yoko += D[i][j]
        tate[j] += D[i][j]
    if yoko == 3:
        print("Yes")
        exit()

q = D[0][0] + D[1][1] +D[2][2]
p = D[0][2] + D[1][1] + D[0][2]

if (3 in tate) or (p==3) or (q==3):
    print("Yes")
    exit()
print("No")