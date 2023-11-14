import sys
input = sys.stdin.readline

import math

C = int(input())

# cnt = 0
# for x in range(0, C + 1):
#     for y in range(0, C + 1):
#         if math.gcd(x, y) == 1:
#             print(x,y)
#             cnt += 1
# print(cnt)

cnts = [1, 3]
for x in range(2, 1000 + 1):
    cnt = 0
    for y in range(0, x):
        if math.gcd(x, y) == 1:
            cnt += 1
    cnts.append(cnts[x-1] + cnt * 2)

for _ in range(C):
    N = int(input())
    print(cnts[N])
