import functools

file1 = open('data.txt', 'r')
Lines = file1.readlines()

data = []

def processLine(line):
    c = 0
    res = []
    while True:
        if line[c] == '[':
            l, nc = processLine(line[c+1:])
            res.append(l)
            c = c + nc + 1
        elif line[c] == ']':
            return res, c+1
        elif line[c] == ',':
            c += 1
        else:
            next_break = c
            while next_break < len(line) and line[next_break] != '[' and line[next_break] != ']' and line[next_break] != ',':
                next_break += 1
            
            res.append(int(line[c:next_break]))
            c = next_break
        
        if c >= len(line):
            break

    return res, c

for line in Lines:
    line = line.strip()
    if line == '':
        continue

    r, c = processLine(line[1:])
    data.append(r)
    

#print(data)

def compareLists(l1, l2):
    #print("Comparing", l1, l2)
    i = 0
    while True:
        # if the left list runs out of items first, then it is correct
        if i >= len(l1) and i < len(l2):
            #print("Correct")
            return True
        # if the right list runs out of items first, then it is incorrect
        elif i < len(l1) and i >= len(l2):
            #print("Incorrect")
            return False
        # if both lists run out of items at the same time, then they are equal
        elif i >= len(l1) and i >= len(l2):
            #print("Equal")
            return None
        f = l1[i]
        s = l2[i]
        #print("Compare", f, s)
        # if f and s both are lists, then compare them
        if isinstance(f, int) and isinstance(s, int):
            if f < s:
                #print("Correct")
                return True
            elif f > s:
                #print("Incorrect")
                return False
        else:
            if isinstance(f, int):
                f = [f]
            if isinstance(s, int):
                s = [s]
            r = compareLists(f, s)
            if r == None:
                i += 1
                continue
            elif r:
                #print("Correct")
                return True
            else:
                #print("Incorrect")
                return False
        i += 1

sum = 0
i = 0
while i < len(data):
    first = data[i]
    second = data[i+1]
    i += 2
    r = compareLists(first, second)
    if r:
        index = i/2
        sum += index

print(sum)

# part 2

data.append([[2]])
data.append([[6]])

def sort_compare(l1, l2):
    r = compareLists(l1, l2)
    if r == True:
        return -1
    elif r == False:
        return 1
    else:
        return 0

data.sort(key=functools.cmp_to_key(sort_compare))

first_index = 0
second_index = 0
for d in data:
    if d == [[2]]:
        first_index = data.index(d)+1
    if d == [[6]]:
        second_index = data.index(d)+1

res = first_index*second_index
print(res)