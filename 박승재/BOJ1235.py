import sys
input = sys.stdin.readline

N = int(input())

A = []
for _ in range(N):
    A.append(input().strip())

for k in range(1, 101):
    s = set([a[-k:] for a in A])
    if len(s) == len(A):
        print(k)
        break
