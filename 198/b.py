# 入力が高々10桁なことに注意。
n = str(input())

for i in range(10):
    s = "0"*i + n
    if s == s[::-1]:
        print("Yes")
        exit()
print("No")