n = int(input())
L = str(n)
l = len(L) # l:その数字が何桁か

for i in range(1, 10**6+1):
    if int(str(i) * 2) > n:
        print(i-1)
        exit()









# 元の回答

# """
# 全部回すとTLEになる。
# 2桁のときは9コ，4桁は90コ，6は900コとなっているから
# 最上位の桁について半分にしたときにその下桁の数だけある。
# """
#
#
# ans = 0
# if l==1:
#     pass
#
# elif l==2:
#     for i in range(10, n+1):
#         i = str(i)
#         if i[0] == i[1]:
#             ans += 1
#
# elif l==3:
#     ans = 9
#
# elif l==4:
#     ans+=9
#     for i in range(1000, n+1):
#         i = str(i)
#         if i[:2] == i[2:]:
#             ans += 1
#
# elif l==5:
#     ans = 99
#
# elif l==6:
#     ans += 99
#     for i in range(100000, n+1):
#         i = str(i)
#         if i[:3] == i[3:]:
#             ans += 1
#
# elif l==7:
#     ans = 999
#
# elif l==8:
#     ans += 999
#     z = int(L[0])
#     ans += 1000*(z-1)
#     Ll, Lr = int(L[:4]), int(L[4:])
#     if Ll > Lr:
#         pass
#     elif Ll <= Lr:
#         w = int(L[1:4])+1
#         ans += w
#
#
# elif l==9:
#     ans = 9999
#
# elif l==10:
#     ans += 9999
#     z = int(L[0])
#     ans += 10000*(z-1)
#     Ll, Lr = int(L[:5]), int(L[5:])
#
#     if Ll > Lr:
#         pass
#     elif Ll <= Lr:
#         w = int(L[1:5])+1
#         ans += w
#
# elif l==11:
#     ans = 99999
#
#
# print(ans)

