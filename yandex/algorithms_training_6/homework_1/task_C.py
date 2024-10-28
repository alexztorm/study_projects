def letter_on_the_screen(n: int, screen: list[str]) -> str:
    x1, x2, y1, y2 = -1, n, n, -1

    for i in range(n):
        for j in range(n):
            if screen[i][j] == '#':
                if i > x1:
                    x1 = i
                if j < y1:
                    y1 = j
                if i < x2:
                    x2 = i
                if j > y2:
                    y2 = j

    x3, y3, x4, y4 = -1, n, n, -1
    x5, y5, x6, y6 = -1, n, n, -1

    for i in range(x2, x1 + 1):
        for j in range(y1, y2 + 1):
            if screen[i][j] == '.':
                ...

    return "X"


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
             '#..#']]
    ]
    ans = ['I', 'X', 'O', 'C', 'L', 'H', 'P', 'P', 'X', 'I', 'O', 'X']

    for l in range(len(ans)):
        if letter_on_the_screen(tests[l][0], tests[l][1]) == ans[l]:
            print(True)
        else:
            print(l, letter_on_the_screen(tests[l][0], tests[l][1]), ans[l])
