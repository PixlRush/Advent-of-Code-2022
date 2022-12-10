X = 1
t = 1


def measure():
    hscan = t % 40
    if X <= hscan <= X+2:
        print("#", end='')
    else:
        print(" ", end='')
    if hscan == 0:
        print("")


with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        if "noop" in theLine:
            measure()
            t += 1
            continue
        _, param = theLine.strip().split(" ")
        measure()
        t += 1
        measure()
        t += 1
        X += int(param)
