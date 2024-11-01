n = int(input())

a = [int(x) for x in input().split()]
b = [a[0]]

for i in range(1, n):
    b.append(b[i - 1] + a[i])

for num in b:
    print(num, end=' ')
