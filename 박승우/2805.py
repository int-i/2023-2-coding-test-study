import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
left = 1
right = max(tree)
mid = (left + right)//2
while True:
    count = 0
    for i in range(n):
        if tree[i] > mid:
            count += tree[i]-mid
    if count >= m:
        if left == right:
            print(left)
            break
        else:
            left = mid + 1
            mid = (right + left) // 2
    else:
        if left == right:
            print(left - 1)
            break
        elif left == right - 1:
            print(left - 1)
            break
        else:
            right = mid - 1
            mid = (right + left) // 2
