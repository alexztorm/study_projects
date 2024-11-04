def censor_mult(n: int, c: int, s: str) -> int:
    max_size, cur_sum = 1, 0
    calc_a, calc_b = 0, 0
    first_a = -1

    right = 1

    if s[0] == 'a':
        calc_a += 1
        first_a = 0

    for left in range(n):
        # print(s[left:right + 1], calc_a, calc_b, cur_sum, max_size)
        while right < n:
            if s[right] == 'a':
                calc_a += 1
                if first_a == -1:
                    first_a = right
            elif s[right] == 'b':
                if first_a != -1:
                    calc_b += 1
                    cur_sum += calc_a

            # print(s[left:right + 1], calc_a, calc_b, cur_sum, end=' ')

            if cur_sum > c:
                right += 1
                break
            else:
                if right - left + 1 > max_size:
                    max_size = right - left + 1
                right += 1

            # print(max_size)

        if s[left] == 'a':
            cur_sum -= calc_b
            calc_a -= 1
        elif s[left] == 'b':
            if left > first_a != -1:
                calc_b -= 1

    return max_size


# a, b = map(int, input().split())
# line = input()

# print(censor_mult(a, b, line))

print(censor_mult(3, 1, 'aab'))
print(censor_mult(6, 2, 'aabcbb'))
print(censor_mult(700, 47553, 'bbbabbabaaabaababaaaabbaabaabaaabbabqabaabbbbaaaabaaabaaabbbaaabaaaaaaaaaaaaaabbaabaababbaabaabbbaaaabaabaaaabaabaabbaaabbbabbbbbaabbbaabaaabbaaaaabbbaabbaabbbabababbabaabaabbabbbbabbbbaarbababbabbaaaaabbbabaaabbaaaaaaaabaabaaababbbaabbbabbabbabaabbabbaabaaaabaabaaabbbbbbababaabababaabbabbbbbbafaabbabaaabaaaababaaabbaabaabbabbababababbaaaabbbbbbabbbabbbabbbbaaaabbaabbabbabbaaabbbbababbaaaabbaabbabbbabaababbabbaabbbababaabbabbbdabaaaabaabbaabaaabbbababbbbabbabbaaabbbaaaabbaabbbbbbbaabababaaaabbbbaaaaabbaabaabaabbababaaaaaababbbbaababbbababaaaabaabaaaabbbbbbbbbbbbbaabbaaabbbbaeaapabbaabbbbbaaababababbbabbaaaaabaababbbaababbbaaabrbaabbbababbaabbaabababbbbabaaaabbaaabbbabbbababbbaabbabbbbbaabaab'))
print(censor_mult(50, 159, 'aaabaababaabaaaabaabbxaazbaaaababaababbbaaaabaabbb'))
print(censor_mult(14, 7, 'bbbbbaaabababa'))
print(censor_mult(2, 0, 'ab'))
print(censor_mult(2, 0, 'ba'))
print(censor_mult(6, 1, 'xxxxxx'))
print(censor_mult(3, 1, 'bbr'))
print(censor_mult(1, 0, 'a'))
print(censor_mult(50, 0, 'ilsvmrbeemrszqvobxfuqraptxqzaqjaaxclbeccrwabcmfome'))
