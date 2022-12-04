overlap = 0

with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        first, second = theLine.split(",")
        fstart, fend = first.split("-")
        sstart, send = second.split("-")
        fstart = int(fstart)
        fend = int(fend)
        sstart = int(sstart)
        send = int(send)
        # Check f contained in s
        if (fstart >= sstart and fend <= send) or (sstart >= fstart and send <= fend):
            overlap += 1

print(overlap)
