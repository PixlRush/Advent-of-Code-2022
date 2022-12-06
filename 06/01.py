index = 0

with open("input.txt", 'r') as theFile:
    theLine = theFile.readline()
    for i in range(4, len(theLine)):
        window = theLine[i-4:i]
        maxinst = max(map(window.count, window))
        if maxinst == 1:
            index = i
            break

print(index)
