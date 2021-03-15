# URL : https://atcoder.jp/contests/abc195/tasks/abc195_b
a, b, w = map(int, input().split())
w *= 1000
aa = w // a
bb = (w + b - 1) // b
print(aa, bb)
if bb > aa:
    print("UNSATISFIABLE")
else:
    print(bb, aa)
