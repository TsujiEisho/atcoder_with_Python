a, b, c, x, y = map(int, input().split())

"""
cを2個買うことでa,bが1つずつ買ったものとみなせる。
x,y 整数だからcを奇数個買うことは条件に合わない。

最初はabをxy枚それぞれ買うこと（m円）からスタート。
max(x, y)回までa,bを減らしてcを買うことをしてもいいから
ループを回す。都度金額を計算して小さい方をansに格納しておく。
"""

c *= 2
ans = a*x + b*y

if (a+b) <= c:
    pass
else:
    D = a+b-c # cを買うことによる差額
    for i in range(max(x, y)):
        ans -= D


print(ans)
