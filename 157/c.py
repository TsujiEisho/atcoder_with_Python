n, m = map(int, input().split())
"""
最大でn=3だから桁ごとに条件の数字を格納したリストを
作っておいて，それを参照して答えを出す。
"""

F=[]; S=[]; T=[]
for i in range(m):
    s, c = map(int, input().split())
    if s == 1:
        F.append(c)
    elif s == 2:
        S.append(c)
    else:
        T.append(c)
F.sort(); S.sort(); T.sort()
f=len(F); s=len(S); t=len(T)

if t==0:
    print(-1)
    exit()

ans = []

if f==0 and s==0:
    print(min(T))
    exit()
elif f ==0 and s!=0:
    ans.append(str(min(S)))
    ans.append(str(min(T)))
    print(''.join(ans))
    exit()
elif f!=0 and s==0:
    ans.append(str(min(F)))
    ans.append("0")
    ans.append(str(min(T)))
    print(''.join(ans))
    exit()
else:
    ans.append(str(min(F)))
    ans.append(str(min(S)))
    ans.append(str(min(T)))
    print(''.join(ans))
