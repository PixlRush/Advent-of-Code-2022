forest = []

# Ingest the File
with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        forest.append([int(x) for x in theLine.strip()])

maxScenic = -1

for i in range(len(forest)):
    for j in range(len(forest[i])):
        print(f"Inspecting {(i,j)}")
        scenic = 1  # Empty Product
        height = forest[i][j]

        # Rows
        # -->
        dist = 0
        for s in range(j+1, len(forest[i])):
            dist += 1
            if forest[i][s] >= height:
                break
        print(f"{dist} * ", end='')
        scenic *= dist
        # <--
        dist = 0
        for s in range(j-1, -1, -1):
            dist += 1
            if forest[i][s] >= height:
                break
        print(f"{dist} * ", end='')
        scenic *= dist

        # Columns
        # -->
        dist = 0
        for s in range(i+1, len(forest)):
            dist += 1
            if forest[s][j] >= height:
                break
        print(f"{dist} * ", end='')
        scenic *= dist

        dist = 0
        for s in range(i-1, -1, -1):
            dist += 1
            if forest[s][j] >= height:
                break
        print(f"{dist} = ", end='')
        scenic *= dist
        print(f"{scenic}")

        # New Max
        if scenic > maxScenic:
            print(f"New best of {scenic} from {maxScenic}")
            maxScenic = scenic


print(maxScenic)
