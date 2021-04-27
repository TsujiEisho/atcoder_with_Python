"""
そのまま問題文通りに実装すると計算量的にダメ。
フリップ操作を誤魔化すことで通すことができる。
n分ずれてて，2nであまりをとることで誤魔化す。
こういうのはどうせflipを誤魔化すってなんとなくわかるらしい。
"""


n = int(input())
s = list(input())
q = int(input())



flip = False

for i in range(q):
    t, a, b = map(int, input().split())

    if t == 1:
        if flip:
            a -= 1; b -= 1
            s[(a+n)%(2*n)] , s[(b+n)%(2*n)] = s[(b+n)%(2*n)], s[(a+n)%(2*n)]
        else:
            a -= 1; b-= 1 #0-index
            s[a], s[b] = s[b], s[a]
    else:       #t == 2
        flip = not flip

if flip:
    s = s[n:] + s[:n]

print("".join(s))