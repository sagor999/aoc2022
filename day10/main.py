file1 = open('data.txt', 'r')
Lines = file1.readlines()

X = 1
instr = []
for line in Lines:
    line = line.strip()
    if line == "noop":
        instr.append(0)
    else:
        line = line.split(' ')
        num = int(line[1])
        instr.append(0)
        instr.append(num)

# Part 1
#signal = 0
#for i in range(1, 221):
#    if i == 20 or i == 60 or i == 100 or i == 140 or i == 180 or i == 220:
#        signal = signal + X*i
#        #print("total signal: ", signal)
#    op = instr.pop(0)
#    X = X + op

# Part 2
for i in range(1, 241):
    pixel = (i-1) % 40
    diff = abs(pixel - X)
    if diff <= 1:
        print("#", end="")
    else:
        print(" ", end="")
    op = instr.pop(0)
    X = X + op
    if i % 40 == 0:
        print("")
