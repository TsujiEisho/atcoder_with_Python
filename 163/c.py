"""
カウンターリストを作成し，上司をインデックス，
要素として何人の部下がいるかを格納していく。
"""


n = int(input())
A = [0, 0] + list(map(int, input().split()))
A.sort()
B = [0]*(n+1)
for i in range(1, n+1):
    x = A[i]
    B[x] += 1
for i in range(1, n+1):
    print(B[i])