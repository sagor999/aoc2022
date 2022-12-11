file1 = open('data.txt', 'r')
Lines = file1.readlines()

class Monkey:
    def __init__(self):
        self.items = []
        self.op = ('none', '0')
        self.test = 1
        self.test_true = 0
        self.test_false = 0
        self.num_inspected = 0

monkeys = []
for line in Lines:
    line = line.strip()
    #print(line)
    if line == '':
        continue
    items = line.split(' ')
    if items[0] == 'Monkey':
        monkeys.append(Monkey())
        continue
    if items[0] == 'Starting':
        items = line.split(': ')
        items = items[1].split(', ')
        for item in items:
            monkeys[-1].items.append(int(item))
        continue
    if items[0] == 'Operation:':
        items = line.split(' = ')
        items = items[1].split(' ')
        monkeys[-1].op = (items[1], items[2])
        continue
    if items[0] == 'Test:':
        monkeys[-1].test = int(items[3])
        continue
    if items[1] == 'true:':
        monkeys[-1].test_true = int(items[5])
        continue
    if items[1] == 'false:':
        monkeys[-1].test_false = int(items[5])
        continue
    print('Error')

def calcWorry(item, op):
    val = 0
    if op[1] == 'old':
        val = int(item)
    else:
        val = int(op[1])
    if op[0] == '+':
        return int(item) + val
    if op[0] == '*':
        return int(item) * val
    print('Error: ' + op)

for round in range(20):
    for monkey in monkeys:
        for item in monkey.items:
            monkey.num_inspected += 1
            #print("Monkey inspects item: " + str(item))
            item = calcWorry(item, monkey.op)
            #print("Monkey performs operation: " + str(item))
            item = item//3
            #print("Monkey divides by 3: " + str(item))
            if item % monkey.test == 0:
                #print("Monkey tests: true, throw it to monkey ", monkey.test_true)
                monkeys[monkey.test_true].items.append(item)
            else:
                #print("Monkey tests: false, throw it to monkey ", monkey.test_false)
                monkeys[monkey.test_false].items.append(item)
        monkey.items = []

inspections = []
for monkey in monkeys:
    inspections.append(monkey.num_inspected)

sorted_inspections = sorted(inspections, reverse=True)
monkey_business = sorted_inspections[0] * sorted_inspections[1]
print(monkey_business)