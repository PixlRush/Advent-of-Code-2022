throws = ["A", "B", "C"]
conv = {"X": -1, "Y": 0, "Z": 1}
score = 0

with open("input.txt", 'r') as theFile:
    theLine = theFile.readline()
    while theLine:
        opp, outcome = theLine.strip().split()
        outcome = conv[outcome]

        # Score the outcome
        score += (outcome + 1) * 3

        # Determine your shape
        opp = throws.index(opp)
        me = (opp + outcome) % 3

        # Score your shape
        score += me + 1
        theLine = theFile.readline()

print(score)
