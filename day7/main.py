file1 = open('data.txt', 'r')
Lines = file1.readlines()

directories = {'/': []}
curPath = '/'
for line in Lines:
    line = line.strip()
    if line[0] == '$':
        parts = line.split(' ')
        if parts[1] == 'cd':
            if parts[2] == '..':
                path = curPath.split('/')
                curPath = '/'.join(path[:-1])
            else:
                if parts[2] == '/':
                    curPath = '/'
                else:
                    curPath += '/' + parts[2]
        continue
    else:
        parts = line.split(' ')
        if parts[0] == 'dir':
            p = curPath + '/' + parts[1]
            if p not in directories:
                directories[p] = []
            directories[curPath].append(p)
        else:
            fsize = int(parts[0])
            fname = parts[1]
            directories[curPath].append((fname, fsize))

#print(directories)
# calculate the size of each directory
dirSizes = {}
def calcSize(dir):
    size = 0
    for item in directories[dir]:
        if type(item) == tuple:
            size += item[1]
        else:
            size += calcSize(item)
    dirSizes[dir] = size
    return size
calcSize('/')
part1 = 0
for d in dirSizes:
    if dirSizes[d] < 100000:
        part1 += dirSizes[d]

print('Part 1:', part1)

fsTotalSize = 70000000
fsUnusedTarget = 30000000
curUsedSize = dirSizes['/']
curUnusedSize = fsTotalSize - curUsedSize
needToFreeSize = fsUnusedTarget - curUnusedSize
minSize = fsTotalSize
for d in dirSizes:
    if dirSizes[d] >= needToFreeSize:
        if dirSizes[d] < minSize:
            minSize = dirSizes[d]
print('Part 2:', minSize)