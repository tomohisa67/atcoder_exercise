A, B = list(map(int, input().split()))

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

Z = make_divisors(100)
n = len(Z)

for i in range(A,B+1):
    for j in range(n):
        if Z[j] == i:
            print("Yes")
            exit()
            
print("No")