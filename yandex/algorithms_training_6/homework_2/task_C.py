def two_pointer_statues(n: int, r: int, dist: list[int]) -> int:
    ans = 0

    right = 1
    for left in range(n):
        while right < n and (dist[right] - dist[left] <= r):
            right += 1
        ans += n - right

    return ans


a, b = map(int, input().split())
nums = [int(x) for x in input().split()]

print(two_pointer_statues(a, b, nums))
