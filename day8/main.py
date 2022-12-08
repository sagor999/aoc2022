file1 = open('data.txt', 'r')
Lines = file1.readlines()

trees = []
i = 0
for line in Lines:
    line = line.strip()
    trees.append([])
    for char in line:
        h = int(char)
        trees[i].append(h)
    i += 1
#print(trees)

visibleTrees = 0
for x in range(0, len(trees)):
    for y in range(0, len(trees[x])):
        if x == 0 or y == 0 or x == len(trees) - 1 or y == len(trees[x]) - 1:
            visibleTrees += 1
            continue
        treeHeight = trees[x][y]
        #print("checking x, y: ", x, y, trees[x][y])
        # check up
        visible = True
        xn = x-1
        while xn >= 0:
            if trees[xn][y] >= treeHeight:
                visible = False
                break
            xn -= 1
        if visible:
            visibleTrees += 1
            #print("visible from up")
            continue
        # check down
        visible = True
        xn = x+1
        while xn < len(trees):
            if trees[xn][y] >= treeHeight:
                visible = False
                break
            xn += 1
        if visible:
            visibleTrees += 1
            #print("visible from down")
            continue
        # check left
        visible = True
        yn = y-1
        while yn >= 0:
            if trees[x][yn] >= treeHeight:
                visible = False
                break
            yn -= 1
        if visible:
            visibleTrees += 1
            #print("visible from left")
            continue
        # check right
        visible = True
        yn = y+1
        while yn < len(trees[x]):
            if trees[x][yn] >= treeHeight:
                visible = False
                break
            yn += 1
        if visible:
            visibleTrees += 1
            #print("visible from right")
            continue
        #print("not visible", x, y, treeHeight)

print("visible trees: ", visibleTrees)

maxScenicScore = 0
for x in range(0, len(trees)):
    for y in range(0, len(trees[x])):
        if x == 0 or y == 0 or x == len(trees) - 1 or y == len(trees[x]) - 1:
            continue
        treeHeight = trees[x][y]
        # check up
        seeUp = 0
        xn = x-1
        while xn >= 0:
            if trees[xn][y] >= treeHeight:
                seeUp += 1
                break
            seeUp += 1
            xn -= 1
        # check down
        seeDown = 0
        xn = x+1
        while xn < len(trees):
            if trees[xn][y] >= treeHeight:
                seeDown += 1
                break
            seeDown += 1
            xn += 1
        # check left
        seeLeft = 0
        yn = y-1
        while yn >= 0:
            if trees[x][yn] >= treeHeight:
                seeLeft += 1
                break
            seeLeft += 1
            yn -= 1
        # check right
        seeRight = 0
        yn = y+1
        while yn < len(trees[x]):
            if trees[x][yn] >= treeHeight:
                seeRight += 1
                break
            seeRight += 1
            yn += 1
        # calculate score
        score = seeUp * seeDown * seeLeft * seeRight
        if score > maxScenicScore:
            maxScenicScore = score

print("max scenic score: ", maxScenicScore) 