import io
import sys

_INPUT = """\
10
1 19 75 37 17 16 33 18 22
41 28 89 74 98 43 42 31
"""
sys.stdin = io.StringIO(_INPUT)

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

K = [0]
T = [0] * N
for i in range(1, N):
    if i == 1:
        T[i] = A[i-1]
        K.append(i-1)
    else:
        t1 = T[i-1] + A[i-1]
        t2 = T[i-2] + B[i-2]
        if t1 >= t2:
            T[i] = t2
            K.append(i-2)
        else:
            T[i] = t1
            K.append(i-1)

ans = str(N)
ind = N-1
while ind > 0:
    ans = str(K[ind]+1) + " " + ans
    ind = K[ind]

print(len(K))
print(ans)