import numpy as np

H, W = list(map(int, input().split()))

X = np.zeros((H,W), dtype=int)
for i in range(H):
    tmp = list(map(int, input().split()))
    X[i] = tmp

Q = int(input())

Y = np.zeros((Q,4), dtype=int)
for i in range(Q):
    tmp = list(map(int, input().split()))
    Y[i] = tmp
A = Y[:,0]
B = Y[:,1]
C = Y[:,2]
D = Y[:,3]

m = np.zeros((H,W))
for i in range(H):
    for j in range(W):
        if i == 0 and j == 0:
            m[i][j] = X[0][0]
        elif i == 0:
            m[i][j] = m[i][j-1] + X[i][j]
        elif j == 0:
            m[i][j] = m[i-1][j] + X[i][j]
        else:
            m[i][j] = m[i-1][j] + m[i][j-1] - m[i-1][j-1] + X[i][j]

        
for i in range(Q):
    if A[i] == 1 and B[i] == 1:
        ans = m[0][0]
    elif A[i] == 1:
        ans = m[C[i]-1][D[i]-1] - m[H-1,B[i]-1]
    elif B[i] == 1:
        ans = m[C[i]-1][D[i]-1]  - m[A[i]-1][W-1]
    else:
        ans = m[C[i]-1][D[i]-1] - m[H-1][B[i]-1] - m[A[i]-1][W-1] + m[A[i]-2][B[i]-2]
    print(int(ans))
            
