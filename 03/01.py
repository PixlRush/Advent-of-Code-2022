priorities = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
priority = 0

with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        cSize = len(theLine)//2
        front, back = theLine[:cSize], theLine[cSize:]
        for item in front:
            if item in back:
                priority += 1 + priorities.index(item)
                break

print(priority)
