priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = 0

with open("input.txt", 'r') as theFile:
    theLines = theFile.readlines()
    for i in range(0, len(theLines), 3):
        l1 = theLines[i]
        l2 = theLines[i+1]
        l3 = theLines[i+2]
        for badge in l1:
            if badge in l2 and badge in l3:
                priority += 1 + priorities.index(badge)
                break

print(priority)
