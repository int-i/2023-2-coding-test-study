N = int(input())
A = list(map(int, input().split()))

inc_dp = [1] * N
dec_dp = [1] * N

# 가장 긴 증가하는 부분 수열
for i in range(1, N):
    for j in range(i):
        if A[i] > A[j]:
            inc_dp[i] = max(inc_dp[i], inc_dp[j] + 1)

# 가장 긴 감소하는 부분 수열
for i in range(N - 2, -1, -1):
    for j in range(N - 1, i, -1):
        if A[i] > A[j]:
            dec_dp[i] = max(dec_dp[i], dec_dp[j] + 1)

max_length = 0
for i in range(N):
    length = inc_dp[i] + dec_dp[i] - 1
    max_length = max(max_length, length)

print(max_length)
