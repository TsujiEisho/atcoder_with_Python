L = list(map(int, input().split()))

c=0; v=0
for i in L:
    if i == L[0]:
        c+=1
    elif i == L[1]:
        v+=1

if c==2 or v==2:
    print("Yes")
else:
    print("No")