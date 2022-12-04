import re
overlap = 0

with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        fstart, fend, sstart, send = list(map(int, re.findall("[0-9]+", theLine)))
        # Check f contained in s
        if (fstart >= sstart and fend <= send) or (sstart >= fstart and send <= fend):
            overlap += 1

print(overlap)
