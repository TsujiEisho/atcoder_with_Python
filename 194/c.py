"""
A_iが絶対値200以下であることからA_i - A_jの
種類は多くとも410である。だからこれをxとおいて
xの個数をそれぞれ調べてx**2の総和を出力する。
"""

N = int(input())
A = list(map(int, input().split()))
MaxA = 400
cnt = [0]*(MaxA*2+1)
ans = 0

for i in range(N):
    cnt[MaxA + A[i]] += 1 #値がいくつあるか記録。

    for aj in range(-MaxA, MaxA+1):
        c = cnt[MaxA+aj] # 値がいくつあるかを参照してcに格納。
        x = A[i] - aj
        ans+=x**2*c

print(ans)