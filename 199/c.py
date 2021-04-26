n = int(input())
S = str(input())
q = int(input())
Z = []
for i in range(q):
    Q = list(map(int, input().split()))
    Z.append(Q)
ZZ=[]
c=0; flg = 0
while c <= q-2:
    if Z[c][1] == Z[c+1][2] and Z[c][2] == Z[c+1][1]:
        flg = 1
    else:
        if flg == 1:
            flg = 0
        else:
            ZZ.append(Z[c])
        # ZZ.append(Z[c+1])
    c+=1
ZZ.append(Z[-1])

# print(ZZ)



for Q in ZZ:
    if Q[0] == 1:
        A = S[:Q[1]-1]
        B = S[Q[1]-1]
        C = S[Q[1]: Q[2]-1]
        D = S[Q[2]-1]
        E = S[Q[2]:]

        S = A+D+C+B+E

    else:
        A = S[:n]; B = S[n:]
        S = B+A

print(S)
