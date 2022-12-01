sigmas = []

with open("input.txt", 'r') as theFile:
    acc = 0
    inLine = theFile.readline()
    while inLine:
        if inLine != "\n":
            acc += int(inLine)
        else:
            sigmas.append(acc)
            acc = 0
        inLine = theFile.readline()

print(max(sigmas))
