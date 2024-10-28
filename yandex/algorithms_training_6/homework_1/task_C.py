def letter_on_the_screen(n: int, screen: list[str]) -> str:
    if not screen:
        return 'X'

    is_filled = False
    for i in range(n):
        if '#' in screen[i]:
            is_filled = True
            break

    if not is_filled:
        return 'X'

    x1, x2, y1, y2 = n, -1, -1, n

    for i in range(n):
        for j in range(n):
            if screen[i][j] == '#':
                if i > y1:
                    y1 = i
                if j < x1:
                    x1 = j
                if i < y2:
                    y2 = i
                if j > x2:
                    x2 = j

    lines_with_blanks = []

    for i in range(y2, y1 + 1):
        if '.' in screen[i][x1:x2+1]:
            lines_with_blanks.append(True)
        else:
            lines_with_blanks.append(False)

    if True not in lines_with_blanks:
        return 'I'

    dark_rectangle = False
    rect_count = 0
    rect_cords = []

    for i in range(y2, y1 + 1):
        for j in range(x1, x2 + 1):
            if screen[i][j] == '#':
                if dark_rectangle and not lines_with_blanks[i - y2]:
                    dark_rectangle = False
            else:
                if not dark_rectangle:
                    dark_rectangle = True

                    rect_count += 1
                    if rect_count > 2:
                        return 'X'
                    rect_cords.append([0, 0, 0, 0])

                    rect_cords[rect_count - 1][0], rect_cords[rect_count - 1][1] = i, j
                    rect_cords[rect_count - 1][2], rect_cords[rect_count - 1][3] = i, j
                else:
                    rect_cords[rect_count - 1][2], rect_cords[rect_count - 1][3] = i, j

    for _ in range(rect_count):
        for i in range(rect_cords[0][0], rect_cords[0][2] + 1):
            for j in range(rect_cords[0][1], rect_cords[0][3] + 1):
                if screen[i][j] == '#':
                    return 'X'

    for i in range(y2, y1 + 1):
        for j in range(x1, x2 + 1):
            if screen[i][j] == '.':
                in_rect = False

                for k in range(rect_count):
                    if rect_cords[k][0] <= i <= rect_cords[k][2] and rect_cords[k][1] <= j <= rect_cords[k][3]:
                        in_rect = True
                        break

                if not in_rect:
                    return 'X'

    x3, y3, x4, y4 = rect_cords[0][1], rect_cords[0][2], rect_cords[0][3], rect_cords[0][0]

    if rect_count == 1:

        if x1 < x3 <= x4 < x2 and y2 < y4 <= y3 < y1:
            return 'O'
        elif x1 < x3 <= x4 == x2 and y2 < y4 <= y3 < y1:
            return 'C'
        elif x1 < x3 <= x4 == x2 and y2 == y4 <= y3 < y1:
            return 'L'
        else:
            return 'X'
    else:
        x5, y5, x6, y6 = rect_cords[1][1], rect_cords[1][2], rect_cords[1][3], rect_cords[1][0]

        if x1 < x3 == x5 <= x4 == x6 < x2 and y2 == y4 <= y3 < y6 <= y5 == y1:
            return 'H'
        elif x1 < x3 == x5 <= x4 < x6 == x2 and y2 < y4 <= y3 < y6 <= y5 == y1:
            return 'P'
        else:
            return 'X'


k = int(input('1 - input, 2 - auto: '))
if k == 1:
    m = int(input())

    input_screen = []
    for i in range(m):
        input_screen.append(input())

    print(letter_on_the_screen(m, input_screen))
else:
    tests = [
        [4, ['.##.',
             '.##.',
             '.##.',
             '....']],
        [5, ['#...#',
             '.#.#.',
             '..#..',
             '.#.#.',
             '#...#']],
        [3, ['###',
             '#.#',
             '###']],
        [5, ['.....',
             '.###.',
             '.#...',
             '.###.',
             '.....']],
        [4, ['#...',
             '#...',
             '###.',
             '....']],
        [5, ['.#.#.',
             '.###.',
             '.#.#.',
             '.#.#.',
             '.....']],
        [10, ['..........',
              '..####....',
              '..#..#....',
              '..#..#....',
              '..#..#....',
              '..####....',
              '..#.......',
              '..#.......',
              '..........',
              '..........']],
        [5, ['#####',
             '##..#',
             '#####',
             '##...',
             '##...']],
        [0, []],
        [1, ['#']],
        [4, ['####',
             '##.#',
             '####',
             '####']],
        [4, ['##.#',
             '##.#',
             '####',
             '#..#']],
        [4, ['####',
             '##.#',
             '#.##',
             '####']],
        [10, ['..........',
              '.#########',
              '.#########',
              '.###.#####',
              '.#......##',
              '.#......##',
              '.#########',
              '..........',
              '..........',
              '..........']],
        [9, ['.........',
             '.####...#',
             '.####...#',
             '.####...#',
             '.########',
             '.####...#',
             '.####...#',
             '..###...#',
             '.........']]
    ]
    ans = ['I', 'X', 'O', 'C', 'L', 'H', 'P', 'P', 'X', 'I', 'O', 'X', 'X', 'X']

    for l in range(len(ans)):
        if letter_on_the_screen(tests[l][0], tests[l][1]) == ans[l]:
            print(True)
        else:
            print(l, letter_on_the_screen(tests[l][0], tests[l][1]), ans[l])
