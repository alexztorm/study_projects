n = int(input())
stack = []
prefix_sum = [0]

for i in range(n):
    command = input()

    if command[0] == '+':
        stack.append(int(command[1:]))
        prefix_sum.append(prefix_sum[-1] + stack[-1])
    elif command[0] == '-':
        print(stack.pop())
        prefix_sum.pop()
    elif command[0] == '?':
        m, k = len(stack), int(command[1:])
        print(prefix_sum[m] - prefix_sum[m - k])
