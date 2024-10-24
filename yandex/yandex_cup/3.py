def max_dance_width(line: str, max_width: int) -> int:
    if '?' not in line:
        width, right_max, left_max = 0, 0, 0
        for el in line:
            if el == 'R':
                width += 1
                if width > right_max:
                    right_max = width
            else:
                width -= 1
                if width < left_max:
                    left_max = width
        new_max_width = abs(right_max - left_max)
        print(line, new_max_width, right_max, left_max)
        if max_width < new_max_width:
            return new_max_width
        else:
            return max_width
    else:
        max_width = max_dance_width(line.replace('?', 'R', 1), max_width)
        max_width = max_dance_width(line.replace('?', 'L', 1), max_width)
        return max_width


dance_line = input()
print(max_dance_width(dance_line, 0))
