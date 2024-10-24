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
