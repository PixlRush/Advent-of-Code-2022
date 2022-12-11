from functools import reduce
from numpy import lcm
# reduce(lcm, [2, 3, 5])

testLogic = lambda x: lambda y: y % x == 0
test = lambda cond, t, f: lambda x: t if cond(x) else f
aOp = lambda x: lambda y: x + y
mOp = lambda x: lambda y: x * y
eOp = lambda x: x * x
modular = lambda x: lambda y: y % x
deWorry = lambda x: x // 3

monkeys = []


class Monkey(object):
    def __init__(self, inv, op, tst):
        self.inv = inv
        self.op = op
        self.tst = tst
        self.red = None  # Modular comes here
        self.activity = 0

    def turn(self):
        acc = list(map(lambda x: (self.red(x), self.tst(x)),
                       map(self.op, self.inv)))
        self.inv = []
        self.activity += len(acc)
        return(acc)

    def accept(self, x):
        self.inv.append(x)


with open("input.txt", 'r') as theFile:
    factors = []
    for theLine in theFile:
        if theLine == "\n":
            continue

        # Handle Items
        theLine = theFile.readline()
        items = list(map(int, theLine.split(": ")[1].split(", ")))

        # Handle Operation
        theLine = theFile.readline()
        op = None
        if theLine.count("old") > 1:

            op = eOp
        else:
            num = int(theLine.strip().split(" ")[-1])
            if "*" in theLine:

                op = mOp(num)
            elif "+" in theLine:

                op = aOp(num)

        # Handle Test
        theLine = theFile.readline()
        factor = int(theLine.strip().split(" ")[-1])
        factors.append(factor)

        checker = testLogic(factor)

        # Handle True
        theLine = theFile.readline()
        yes = int(theLine.strip().split(" ")[-1])

        # Handle True
        theLine = theFile.readline()
        no = int(theLine.strip().split(" ")[-1])

        tst = test(checker, yes, no)

        monkeys.append(Monkey(items, op, tst))

    monkeylcm = reduce(lcm, factors)

    monkeyMod = modular(monkeylcm)
    for monkey in monkeys:
        monkey.red = monkeyMod

for i in range(10000):
    t = 0
    for monkey in monkeys:
        t += 1
        theTurn = monkey.turn()
        for item, target in theTurn:
            monkeys[target].accept(item)

activities = [m.activity for m in monkeys]

activities.sort(reverse=True)
business = activities[0] * activities[1]
print(business)
