rope = [(0, 0), (0, 0)]
vects = {"U": (0, 1),
         "D": (0, -1),
         "L": (-1, 0),
         "R": (1, 0)}

touched = [(0, 0)]


def sign(x):
    if x > 0:
        return 1
    if x < 0:
        return -1
    return 0


def vAdd(a, b):
    return tuple(map(sum, zip(a, b)))


def vDiff(a, b):
    return tuple(map(lambda x: x[0] - x[1], zip(a, b)))


def handleTail(head, tail, ind):
    print(f"Handling {head} -- {tail}")
    # Move the Tail
    delta = vDiff(head, tail)
    if max(map(abs, delta)) > 1:
        d = [sign(delta[0]), sign(delta[1])]
        print(f"{d} -> rope[{ind}] to {vAdd(tail, d)}")
        t = vAdd(tail, d)
        return t

    return tail


with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        mov, steps = theLine.strip().split(" ")
        steps = int(steps)
        vect = vects[mov]
        print(f"== {mov} {steps} ==")
        for i in range(steps):
            # Move the Head
            rope[0] = vAdd(rope[0], vect)
            print(f"Head to {rope[0]}")

            # Move the Trail
            for i in range(1, len(rope)):
                rope[i] = handleTail(rope[i-1], rope[i], i)

            # Touch the Tail
            if rope[-1] not in touched:
                touched.append(rope[-1])
                print(f"New tail touch point {rope[-1]}")

print(len(touched))
