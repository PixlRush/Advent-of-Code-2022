throws = ["A", "B", "C"]
conv = {"X": "A", "Y": "B", "Z": "C"}
score = 0

with open("input.txt", 'r') as theFile:
    theLine = theFile.readline()
    while theLine:
        opp, me = theLine.strip().split()

        # Convert to numbers
        opp = throws.index(opp)
        me = throws.index(conv[me])
        delta = (me - opp) % 3

        # Calculate Win
        if delta == 0:  # Tie
            score += 3
        elif delta == 1:  # Player Win
            score += 6

        # Calculate Shape
        score += me + 1
        theLine = theFile.readline()

print(score)
