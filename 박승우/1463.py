n = int(input())
num = list()
num.append(0)
num.append(0)
num.append(1)
num.append(1)
for i in range(4, n + 1):
    blank = n
    blank_1 = n
    blank_2 = n
    if i % 2 == 0:
        blank = num[i // 2]
    if i % 3 == 0:
        blank_1 = num[i // 3]
    blank_2 = num[i - 1]
    num.append(min(min(blank, blank_1), blank_2) + 1)
print(num[n])
