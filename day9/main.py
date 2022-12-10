file1 = open('data.txt', 'r')
Lines = file1.readlines()

visited_part1 = set()
visited_part2 = set()
Rope = []
for i in range(10):
    Rope.append((0,0))

for line in Lines:
    line = line.strip()
    line = line.split(' ')
    #print(line)
    dir = line[0]
    num = int(line[1])
    mov = (0,0)
    if dir == 'U':
        mov = (0, 1)
    elif dir == 'D':
        mov = (0, -1)
    elif dir == 'L':
        mov = (-1, 0)
    elif dir == 'R':
        mov = (1, 0)
    for i in range(num):
        #print("Current H: ", H)
        Rope[0] = (Rope[0][0]+mov[0], Rope[0][1]+mov[1])
        #print("New H: ", H)
        # check if T need to be updated
        for t in range(1, 10):
            diff = (Rope[t-1][0]-Rope[t][0], Rope[t-1][1]-Rope[t][1])
            #print("Diff: ", diff)
            if abs(diff[0]) > 1 or abs(diff[1]) > 1:
                if abs(diff[0]) == 2:
                    diff = (diff[0]//2, diff[1])
                if abs(diff[1]) == 2:
                    diff = (diff[0], diff[1]//2)
                Rope[t] = (Rope[t][0]+diff[0], Rope[t][1]+diff[1])
            #print("New T: ", T)
        visited_part1.add(Rope[1])
        visited_part2.add(Rope[9])

print(len(visited_part1))
print(len(visited_part2))