measurements = 0
measurePoints = [20, 60, 100, 140, 180, 220]
X = 1
t = 1


def measure():
    if t in measurePoints:
        print(f"Measuring t={t} to be {X} [{t * X}]")
        return t * X
    return 0


with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        if "noop" in theLine:
            measurements += measure()
            t += 1
            continue
        _, param = theLine.strip().split(" ")
        measurements += measure()
        t += 1
        measurements += measure()
        t += 1
        X += int(param)

print(measurements)
