forest = []

# Ingest the File
with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        forest.append([int(x) for x in theLine.strip()])

seen = set()

# Handle Row-wise visibility
for i in range(0, len(forest)):
    print(f"--== Row {i} ==--")
    print("--search-->")
    j = 0
    mHeight = -1
    for j in range(len(forest[0])):
        if forest[i][j] > mHeight:
            print(f"Hit {forest[i][j]} from {mHeight} at {(i,j)}")
            seen.add((i, j))
            mHeight = forest[i][j]

    print("<--search--")
    mHeight = -1
    for J in range(len(forest[0]), 0, -1):
        j = J - 1
        if forest[i][j] > mHeight:
            print(f"Hit {forest[i][j]} from {mHeight} at {(i,j)}")
            seen.add((i, j))
            mHeight = forest[i][j]

# Handle Column-wise visibility
for j in range(len(forest[0])):
    print(f"--== Column {j} ==--")
    print("--search-->")
    mHeight = -1
    for i in range(len(forest)):
        if forest[i][j] > mHeight:
            print(f"Hit {forest[i][j]} from {mHeight} at {(i,j)}")
            seen.add((i, j))
            mHeight = forest[i][j]

    print("<--search--")
    mHeight = -1
    for I in range(len(forest), 0, -1):
        i = I - 1
        if forest[i][j] > mHeight:
            print(f"Hit {forest[i][j]} from {mHeight} at {(i,j)}")
            seen.add((i, j))
            mHeight = forest[i][j]

print(len(seen))
