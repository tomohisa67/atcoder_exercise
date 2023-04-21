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
            m[i][j] = m[i-1][j] + m[i][j-1] - m[i-1][j-1]

        
for i in range(Q):
    ans = m[H-1,B[i]] + m[A[i]][W-1] - m[A[i]][B[i]] - m[C[i]][D[i]]
    print(ans)
            
        
            
        
            



# m = np.zeros((H,W))
# for i in range(H):
#     for j in range(W):
#         if i == 0 and j == 0:
#             m[i,j] = X[0,0]
#         elif i == 0:
#             m[i,j] = m[i,j-1] + X[i,j]
#         elif j == 0:
#             m[i,j] = m[i-1,j] + X[i,j]
#         else:
#             m[i,j] = m[i-1,j] + m[i,j-1] - m[i-1,j-1]
        