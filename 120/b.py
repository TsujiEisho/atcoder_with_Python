a, b, k = map(int, input().split())
ans = []
n = 1
for i in range(1, min(a, b)+1):
    if (a/i).is_integer() and (b/i).is_integer():
        ans.append(i)
print(ans[-k])

