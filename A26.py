import io
import sys
_INPUT = """\
4
17
31
35
49
"""
sys.stdin = io.StringIO(_INPUT)

def primality_test(x):
    if x == 2:
        return True
    elif x < 2 or x % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= x:
            if x % i == 0:
                return False
            i += 2
        return True

Q = int(input())
for i in range(Q):
    x = int(input())
    is_prime_number = primality_test(x)
    if is_prime_number:
        print("Yes")
    else:
        print("No")
        