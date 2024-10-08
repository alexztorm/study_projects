def hanoi_towers(n, time, log, from_peg, to_peg):
    if n == 1:
        time += 1
        log.append([from_peg, to_peg])
        return time, log

    unused_peg = 6 - from_peg - to_peg

    time, log = hanoi_towers(n - 1, time, log, from_peg, unused_peg)

    time += 1
    log.append([from_peg, to_peg])

    time, log = hanoi_towers(n - 1, time, log, unused_peg, to_peg)

    return time, log
