N = int(input())

ans = bin(N)[2:]

# ans = ""
# m = N
# for i in range(10):
#     tmp = m % 2
#     m = m // 2

#     ans += str(tmp)
#     if m == 1:
#         break

n = len(ans)

output = ""
for i in range(10-n):
    output += '0'

print(output + ans)