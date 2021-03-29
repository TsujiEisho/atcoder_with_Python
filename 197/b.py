h, w, x, y = map(int, input().split())
S = [[0 for i in range(w)] for j in range(h)]
x-=1; y-=1
ans = 1

# 特殊パターン
if h == 1:
    S = []
    s = str(input())
    for j in range(w):
        if s[j] == "#":
            S.append(1)
        else:
            S.append(0)
    # 横方向に調べるS[x-1]
    # 右方向
    r = 1
    while y + r < w:
        if S[y+r] == 0:
            # print(x, y + r)
            ans += 1
        else:
            break
        r += 1
    # 左方向
    l = 1
    while y - l >= 0:
        if S[y - l] == 0:
            # print(x, y - l)
            ans += 1
        else:
            break
        l += 1


elif w == 1:
    S = []
    for i in range(h):
        s = str(input())
        if s == "#":
            S.append(1)
        else:
            S.append(0)
    # 横方向に調べるS[x-1]
    # 右方向
    r = 1

    while y + r < h:
        if S[y + r] == 0:

            ans += 1
        else:
            break
        r += 1
    # 左方向
    l = 1
    while y - l >= 0:
        if S[y - l] == 0:
            # print(x, y - l)
            ans += 1
        else:
            break
        l += 1


else:
    for i in range(h):
        s = str(input())
        for j in range(w):
            if s[j] == "#":
                S[i][j] = 1



    # 横方向に調べるS[x-1]
    # 右方向
    r = 1
    while y+r < w:

        if S[x][y+r] == 0:
            # print(x, y + r)
            ans += 1
        else:
            break
        r+=1

    # 左方向
    l = 1
    while y-l >= 0:
        if S[x][y-l] == 0:
            # print(x, y - l)
            ans += 1
        else:
            break
        l+=1

    # 縦方向に調べるS[][y-1]
    # 上方向
    u=1
    while x-u >= 0:
        if S[x-u][y] == 0:
            # print(x-u, y)
            ans += 1
        else:
            break
        u+=1

    # 下方向
    d=1
    while x+d < h:
        if S[x+d][y] == 0:
            # print(x+d, y)
            ans += 1
        else:
            break
        d+=1


print(ans)