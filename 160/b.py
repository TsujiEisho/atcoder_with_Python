x = int(input())

G = x//500
x -= G*500
g = x//5
print(G*1000+g*5)