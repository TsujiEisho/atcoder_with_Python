a, b = map(str, input().split())

x = str(a*int(b))
y = str(b*int(a))
print(min(x, y))