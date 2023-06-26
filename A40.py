import io
import sys
INPUT = """\
7
1 2 1 2 1 2 1
"""
sys.stdin = io.StringIO(INPUT)

# Nから3つ選ぶ組み合わせの数
def comb(n):
    return n*(n-1)*(n-2)//6

N = int(input())
A = list(map(int, input().split()))

# Aを辞書にする
dic = {}
for i in range(N):
    if A[i] in dic:
        dic[A[i]] += 1
    else:
        dic[A[i]] = 1

count = 0
for i in dic:
    count += comb(dic[i])

print(count)