D = int(input())
N = int(input())

num = [0] * D
lc = [0] * D
rc = [0] * D
for i in range(N):
    l, r = map(int, input().split())
    lc[l-1] += 1
    rc[r-1] += 1

for i in range(D):
    if i == 0:
        num[0] = lc[0]
    else:
        inc = lc[i]
        dec = rc[i-1]
        num[i] = num[i-1] + inc - dec
    
    print(num[i])


