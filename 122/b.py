"""
リストを作ってその中にあるかどうかで判定。
もしなければカウントを終了して今までの最長かどうかを判定。
"""

S = str(input())
li = ["A", "T", "C", "G"]
ans = 0; cnt = 0

for i in S:
    if i in li:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 0
ans = max(ans, cnt) # 最後がACTGの時にこれがないとansが更新されない。
print(ans)