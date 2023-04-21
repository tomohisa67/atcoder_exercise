N, Q = list(map(int, input().split()))
A = list(map(int, input().split()))

cum = []
n = 0
for i in range(N):
    n = n + A[i]
    cum.append(n) 

for i in range(Q):
    L, R = map(int, input().split())
    if L == 1:
        ans = ans = cum[R-1]
    else:
        ans = cum[R-1] - cum[L-2]
    print(ans)