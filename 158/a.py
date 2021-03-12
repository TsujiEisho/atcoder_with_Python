s = str(input())
for i in range(2):
    if s[i] == s[i+1]:
        pass
    else:
        print("Yes")
        exit()
print("No")