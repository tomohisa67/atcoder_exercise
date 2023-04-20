N, X = list(map(int, input().split()))
A = list(map(int, input().split()))

count = 0
for i in range(N):
    if A[i] == X: 
        count = count + 1

if count != 0:
    print("Yes")
else:
    print("No")
