N = int(input())
A = list(map(int, input().split()))

# A.sort(reverse=True)


price = 1000


for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if A[k] == price - A[i] - A[j]:
                print("Yes")
                exit()
print("No")


# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         for k in range(N):
#             if i == k and j == k:
#                 continue
#             if A[i]+A[j]+A[k] == 1000:
#                 print("Yes")
#                 exit()

# print("No")
