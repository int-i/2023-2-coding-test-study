from collections import deque
n, k = map(int, input().split())
visit = [0] * 100001
cnt = 1
nums = deque([n])

if n >= k:
    print(n - k)
else:
    while not visit[k]:
        tmp = nums.popleft()
        if tmp >= 1 and visit[tmp - 1] == 0:
            visit[tmp - 1] = visit[tmp] + 1
            nums.append(tmp - 1)
        if tmp < 100000 and visit[tmp + 1] == 0:
            visit[tmp + 1] = visit[tmp] + 1
            nums.append(tmp + 1)
        if tmp * 2 <= 100000 and visit[tmp * 2] == 0:
            visit[tmp * 2] = visit[tmp] + 1
            nums.append(tmp * 2)
    print(visit[k])
