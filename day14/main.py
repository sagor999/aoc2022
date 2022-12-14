file1 = open('data.txt', 'r')
Lines = file1.readlines()


lowest_rock = 0
map = []
for i in range(1000):
    map.append([0] * 1000)

for line in Lines:
    line = line.strip()
    line = line.split(' -> ')
    positions = []
    for l in line:
        c = l.split(',')
        x = int(c[0])
        y = int(c[1])
        if y > lowest_rock:
            lowest_rock = y
        positions.append((x, y))
    
    for i in range(len(positions)-1):
        p1 = positions[i]
        p2 = positions[i+1]
        #print(p1, p2)
        # trace line between p1 and p2
        if p1[0] == p2[0]:
            # vertical line
            min_y = min(p1[1], p2[1])
            max_y = max(p1[1], p2[1])
            for y in range(min_y, max_y+1):
                map[p1[0]][y] = 1
                #print("setting", p1[0], y, "to 1")
        else:
            # horizontal line
            min_x = min(p1[0], p2[0])
            max_x = max(p1[0], p2[0])
            for x in range(min_x, max_x+1):
                map[x][p1[1]] = 1
                #print("setting", x, p1[1], "to 1")

def simulateSand(x, y):
    #print("simulating sand at", x, y)
    if y > lowest_rock+1:
        #return -2 # part 1
        return 0 # part 2
    if map[x][y] >= 1:
        return 0
    
    r = simulateSand(x, y+1)
    if r < 0:
        return r
    elif r == 0:
        r = simulateSand(x-1, y+1)
        if r < 0:
            return r
        elif r == 0:
            r = simulateSand(x+1, y+1)
            if r < 0:
                return r
            elif r == 0:
                if map[x][y] == 0:
                    map[x][y] = 2
                    return -1
                else:
                    return 0

num_sands = 0
while True:
    r = simulateSand(500, 0)
    #if r == -2: # part 1
    if r == 0: # part 2
        break
    num_sands += 1

print(num_sands)