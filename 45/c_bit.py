s = input()
n = len(s) # 文字列の長さ
ans = 0

# bit全探索
for bit in range(1 << n-1):
    f = s[0]
    for i in range(n-1):

        if bit & (1 << i): #+を入れるとき
            f += "+"
        f += s[i+1]
    ans += sum((map(int, f.split("+"))))
print(ans)