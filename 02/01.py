throws = ["A", "B", "C"]
conv = {"X": "A", "Y": "B", "Z": "C"}
scoreDelta = [3, 6, 0]
score = 0

with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        opp, me = theLine.strip().split()

        # Convert to numbers
        opp = throws.index(opp)
        me = throws.index(conv[me])
        delta = (me - opp) % 3

        # Calculate Score
        score += me + 1 + scoreDelta[delta]

print(score)
