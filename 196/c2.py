n = int(input())
L = str(n)
l = len(L) # l:その数字が何桁か

if l==1:
    ans = 0

else:
    if l%2 == 0: # 偶数桁のとき
        Ll, Lr = L[:l//2], L[l//2:]


