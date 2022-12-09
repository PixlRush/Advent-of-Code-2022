head = (0, 0)
tail = (0, 0)
vects = {"U": (0, 1),
         "D": (0, -1),
         "L": (-1, 0),
         "R": (1, 0)}

touched = {(0, 0)}


def vAdd(a, b):
    return tuple(map(sum, zip(a, b)))


def vDiff(a, b):
    return tuple(map(lambda x: x[0] - x[1], zip(a, b)))


with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        mov, steps = theLine.strip().split(" ")
        steps = int(steps)
        vect = vects[mov]
        print(f"== {mov} {steps} ==")
        for i in range(steps):
            head = vAdd(head, vect)
            print(f"Head to {head}")
            # Move the Tail
            delta = vDiff(head, tail)
            # Ensure tail needs to be moved
            if max(map(abs, delta)) > 1:
                # Must be orthogonal a 0 & 2
                if 0 in delta:
                    print(vect, end='')
                    tail = vAdd(tail, vect)
                else:
                    tVect = [0, 0]
                    tVect[0] = -1 if (delta[0] < 0) else 1
                    tVect[1] = -1 if (delta[1] < 0) else 1
                    print(tVect, end='')
                    tail = vAdd(tail, tVect)
                print(f" -> Tail to {tail}")

            # Touch the Tail
            if tail not in touched:
                touched.add(tail)
                print(f"New tail touch point {tail}")

print(len(touched))
