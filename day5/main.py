file1 = open('data.txt', 'r')
Lines = file1.readlines()

instructions = False
stacks = []
for line in Lines:
    line = line.strip('\n')
    if line == '':
        instructions = True
        #print(stacks)
        continue
    
    if not instructions:
        # split the line every 4 characters
        line = [line[i:i+4] for i in range(0, len(line), 4)]
        i = 0
        if len(stacks) == 0:
            for _ in line:
                stacks.append([])
        if line[0][1] == '1':
            continue
        for l in line:
            ch = l[1]
            if ch != ' ':
                if stacks[i] == None:
                    stacks[i] = []
                stacks[i].append(l[1])
            i+=1
    else:
        line = line.split(' ')
        quantity = int(line[1])
        fr = int(line[3])-1
        to = int(line[5])-1
        #print(f"Moving {quantity} from {fr} to {to}")
        #part1
        #for i in range(quantity):
        #    stacks[to].insert(0, stacks[fr].pop(0))
        #part2
        temp = []
        for i in range(quantity):
            temp.append(stacks[fr].pop(0))
        for i in range(quantity):
            stacks[to].insert(0, temp.pop())
        #print(stacks)

for s in stacks:
    print(s[0], end='')
print()

