n = int(input())
import collections
l=[]
for i in range(n):
    l.append(str(input()))

c = collections.Counter(l)
print(c)
print(c.most_common()[0])
