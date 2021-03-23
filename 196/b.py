x = str(input())

if "." in x:
    print(x.split(".")[0])
else:
    print(int(x))
