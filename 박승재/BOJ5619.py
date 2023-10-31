import sys
input = sys.stdin.readline

N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))
A.sort()

if len(A) < 4:
    A.append(10001) 

c = []
for i in range(4):
    for j in range(4):
        if i != j:
            c.append(int(f'{A[i]}{A[j]}'))
c.sort()

print(c[2])
