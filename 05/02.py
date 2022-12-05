import re

with open("input.txt", 'r') as theFile:
    # Ingest Rows
    rows = []
    for theLine in theFile:
        if "1" in theLine:  # No need to ingest the number row
            continue
        if theLine == "\n":  # Blank line to separate modes
            break
        # Default Ingest Behaviour
        rows.append([theLine[i] for i in range(1, len(theLine), 4)])
        continue

    # Build Stacks
    stacks = [list() for i in range(len(rows[0]))]
    for row in rows:
        i = 0
        for box in row:
            if box != " ":
                stacks[i].insert(0, box)
            i += 1

    # Maneuvering
    for theLine in theFile:
        number, source, dest = list(map(int, re.findall("[0-9]+", theLine)))
        source = stacks[source-1]
        dest = stacks[dest-1]
        # Use accumulator to hold boxes
        claw = []
        for i in range(number):
            claw.insert(0, source.pop())
        dest += claw

    code = ""
    for stack in stacks:
        code = code + stack[-1]

    print(code)
