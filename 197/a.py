s = list(input())
s.append(s[0])
s.remove(s[0])
print("".join(s))
