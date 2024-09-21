def polynom_sum(p1: list[int], p2: list[int]) -> list[int]:
    if len(p1) > len(p2):
        j = len(p1) - 1
        for i in range(len(p2) - 1, -1, -1):
            p1[j] += p2[i]
            j -= 1

        return p1
    else:
        j = len(p2) - 1
        for i in range(len(p1) - 1, -1, -1):
            p2[j] += p1[i]
            j -= 1

        return p2


m1 = int(input())
num_list1 = input().split(" ")
num_list1 = [int(x) for x in num_list1]

m2 = int(input())
num_list2 = input().split(" ")
num_list2 = [int(x) for x in num_list2]

ans = polynom_sum(num_list1, num_list2)

print(max(m1, m2))

for i in range(len(ans)):
    print(ans[i], end=" ")
