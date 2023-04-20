N, K = list(map(int, input().split()))

ans = 0
if K > 3*N:
    ans = 0
elif 2*N+1 <= K <= 3*N:
    ans = ((3*N-K+1)**2 + (3*N-K+1))/2
elif N+2 <= K <= 2*N+1:
    ans = N**2 - ((K-N-1)**2 - (K-N-1))/2 - ((2*N-K+2)**2 - (2*N-K+2))/2
elif 3 <= K <= N+2:
    ans = ((K-2)**2 + (K-2))/2
else:
    ans = 0

print(int(ans))