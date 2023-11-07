import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))

segtree = [0] * (1<<22)

def make_segtree(node, start, end):
    if (start == end):
        segtree[node] = A[start]
        return
    mid = (start + end) // 2
    make_segtree(node * 2, start, mid)
    make_segtree(node * 2 + 1, mid + 1, end)
    segtree[node] = segtree[node * 2] + segtree[node * 2 + 1]

make_segtree(1, 0, N - 1)

def query_segtree(node, start, end, left, right):
    if (right < start or left > end):
        return 0
    if (left <= start and right >= end):
        return segtree[node]
    mid = (start + end) // 2
    l = query_segtree(node * 2, start, mid, left, right)
    r = query_segtree(node * 2 + 1, mid + 1, end, left, right)
    return l + r

def update_segtree(node, start, end, idx, val):
    if (idx > end or idx < start):
        return
    if (idx <= start and idx >= end):
        segtree[node] = val
        return
    mid = (start + end) // 2
    update_segtree(node * 2, start, mid, idx, val)
    update_segtree(node * 2 + 1, mid + 1, end, idx, val)
    segtree[node] = segtree[node * 2] + segtree[node * 2 + 1]


for _ in range(Q):
    x, y, a, b = map(int, input().split())
    if x > y:
        x, y = y, x
    x -= 1
    y -= 1
    a -= 1
    print(query_segtree(1, 0, N - 1, x, y))
    update_segtree(1, 0, N - 1, a, b)
