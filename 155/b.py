n = int(input())
A = [0] + list(map(int, input().split()))

for i in range(len(A)):
    if A[i]%2 == 0:
        if A[i]%3==0 or A[i]%5 == 0:
            pass
        else:
            print("DENIED")
            exit()

print("APPROVED")