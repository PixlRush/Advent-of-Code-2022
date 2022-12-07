pwd = ''
filesystem = dict()
dirs = []

print("--== Ingesting File Tree ==--")
with open("input.txt", 'r') as theFile:
    for theLine in theFile:  # Ingest File Tree
        # Command Mode
        if theLine[0] == "$":
            # Command cd
            if "cd" in theLine:
                print(f"{pwd} -> ", end='')
                if "/" in theLine:
                    pwd = ''
                elif ".." in theLine:
                    pwd = "/".join(pwd.split("/")[:-1])
                elif pwd is '':
                    _, _, target = theLine.split()
                    pwd = f"{target}"
                else:
                    _, _, target = theLine.split()
                    pwd = f"{pwd}/{target}"
                print(f"{pwd}")

        # Parsing Mode
        else:
            first, last = theLine.split()
            if first == "dir":
                # Add directory named last to pwd
                print(f"new folder {last}")
                dirname = last if pwd == '' else f"{pwd}/{last}"
                filesystem[dirname] = None  # Will Calc Later
                dirs.append(dirname)
                pass
            else:
                # Make file with size last
                print(f"file {last} with size {first}")
                dirname = last if pwd == '' else f"{pwd}/{last}"
                filesystem[dirname] = int(first)
                pass

print("\n--== Calculating Directory Size ==--")
# Handle the / directory
filesystem["/"] = 0
dirs.append("/")
for k in filesystem:
    if filesystem[k] is not None and k is not "/":
        filesystem["/"] += filesystem[k]

allDirsCalced = False  # Flag for search termination
# Continue until all calculated
while not allDirsCalced:
    allDirsCalced = True
    # For dirs still needing to be calculated
    for d in [k for k in dirs if filesystem[k] is None]:
        if allDirsCalced:  # Not All Done
            allDirsCalced = False
        print(f"searching {d}")
        acc = 0
        dnamesize = len(d)
        # Pass over keys
        depFlag = False
        for name in filesystem:
            # Flag to break early if dependancy occurs
            if depFlag:
                break
            if name[:dnamesize] == d \
               and name[dnamesize:].count("/") < 2 \
               and name != d:
                print(f"hit {name} ({filesystem[name]})")
                if filesystem[name] is None:
                    depFlag = True
                    print("!!! Dependancy Found")
                    continue
                else:
                    acc += filesystem[name]
        if not depFlag:
            print(f"Size Determined {acc}")
            filesystem[d] = acc


print("\n--== Making Output ==--")
# Give output
output = 0
for d in dirs:
    if filesystem[d] <= 100000:
        print(f"directory {d} at size {filesystem[d]}")
        output += filesystem[d]

print(output)
