k, n = map(int, input().split())
A = [0]+list(map(int, input().split()))
Z = []
for i in range(n):
    Z.append(A[i+1] - A[i])
Z.append(k-A[n])

# Zは[O-A1の距離, A_1-A_2・・・A_n-０]を格納したリスト。
# 円の特徴を利用して一か所だけスキップできる＝最大値をスキップする。
# ただしA1スタートにしたときは0-A_1とA_n-0の二カ所スキップできる。

print(min(sum(Z)-max(Z), sum(Z[1:n])))