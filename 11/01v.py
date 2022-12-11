testLogic = lambda x: lambda y: deWorry(y) % x == 0
test = lambda cond, t, f: lambda x: t if cond(x) else f
aOp = lambda x: lambda y: x + y
mOp = lambda x: lambda y: x * y
eOp = lambda x: x * x
deWorry = lambda x: x // 3

monkeys = []


class Monkey(object):
    def __init__(self, inv, op, tst):
        self.inv = inv
        self.op = op
        self.tst = tst
        self.activity = 0

    def turn(self):
        acc = list(map(lambda x: (deWorry(x), self.tst(x)),
                       map(self.op, self.inv)))
        self.inv = []
        self.activity += len(acc)
        return(acc)

    def accept(self, x):
        self.inv.append(x)


with open("input.txt", 'r') as theFile:
    for theLine in theFile:
        if theLine == "\n":
            continue

        # Handle Items
        theLine = theFile.readline()
        items = list(map(int, theLine.split(": ")[1].split(", ")))
        print(f"Items: {items}")

        # Handle Operation
        theLine = theFile.readline()
        op = None
        if theLine.count("old") > 1:
            print("Operator: squared")
            op = eOp
        else:
            num = int(theLine.strip().split(" ")[-1])
            if "*" in theLine:
                print(f"Operator: *= {num}")
                op = mOp(num)
            elif "+" in theLine:
                print(f"Operator: += {num}")
                op = aOp(num)

        # Handle Test
        theLine = theFile.readline()
        factor = int(theLine.strip().split(" ")[-1])
        print(f"Test Logic: divisible by {factor}")
        checker = testLogic(factor)

        # Handle True
        theLine = theFile.readline()
        yes = int(theLine.strip().split(" ")[-1])
        print(f"Test True: pass to {yes}")

        # Handle True
        theLine = theFile.readline()
        no = int(theLine.strip().split(" ")[-1])
        print(f"Test false: pass to {no}")

        tst = test(checker, yes, no)

        monkeys.append(Monkey(items, op, tst))

for i in range(20):
    print(f"== Round {i} ==")
    t = 0
    for monkey in monkeys:
        print(f"= Turn {t} =")
        t += 1
        theTurn = monkey.turn()
        print(theTurn)
        for item, target in theTurn:
            monkeys[target].accept(item)

activities = [m.activity for m in monkeys]
print(activities)
activities.sort(reverse=True)
business = activities[0] * activities[1]
print(business)
