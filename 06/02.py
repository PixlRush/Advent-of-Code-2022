index = 0

with open("input.txt", 'r') as theFile:
    theLine = theFile.readline()
    for i in range(14, len(theLine)):
        window = theLine[i-14:i]
        maxinst = max(map(lambda x: window.count(x), window))
        if maxinst == 1:
            index = i
            break

print(index)
