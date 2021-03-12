s = str(input())
n = len(s)

def D(s):
    U = list(s)
    L = list(s[::-1])
    for i in range(len(U)):
        if U[i] == L[i]:
            pass
        else:
            return False
            break
    return True



if D(s) and D(s[(n-1)//2-1]) and D(s[(n+3)//2 -1:]):
    print("Yes")
else:
    print("No")