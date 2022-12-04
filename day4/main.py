file1 = open('data.txt', 'r')
Lines = file1.readlines()

count = 0
count2 = 0
for line in Lines:
    line = line.strip()
    line = line.split(',')
    firstPair = line[0].split('-')
    secondPair = line[1].split('-')
    firstPair = [int(i) for i in firstPair]
    secondPair = [int(i) for i in secondPair]
    #print(firstPair, secondPair)
    fullyContains = False
    if firstPair[0] <= secondPair[0] and firstPair[1] >= secondPair[1]:
        fullyContains = True
    if secondPair[0] <= firstPair[0] and secondPair[1] >= firstPair[1]:
        fullyContains = True
    
    if fullyContains:
        count += 1

    overlaps = False
    if firstPair[0] <= secondPair[0] and firstPair[1] >= secondPair[0]:
        overlaps = True
    if secondPair[0] <= firstPair[0] and secondPair[1] >= firstPair[0]:
        overlaps = True

    if overlaps:
        count2 += 1

print(count)
print(count2)
