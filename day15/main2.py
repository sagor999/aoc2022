file1 = open('data.txt', 'r')
Lines = file1.readlines()

def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

sensors = []
beacons = []
minx = 100000
maxx = 0
for line in Lines:
    line = line.strip()
    line = line.split('=')
    sx = int(line[1].split(',')[0])
    sy = int(line[2].split(':')[0])
    bx = int(line[3].split(',')[0])
    by = int(line[4])
    d = get_distance(sx, sy, bx, by)
    sensors.append((sx, sy, d))
    beacons.append((bx, by))
    minx = min(minx, sx-d)
    maxx = max(maxx, sx+d)

y = 0
x = 0
minx = 0
maxx = 4000000
while True:
    skip = False
    found = True
    for s in sensors:
        d = get_distance(x, y, s[0], s[1])
        if d <= s[2]:
            found = False
            skip = True
            xdiff = s[0] - x
            ydiff = abs(s[1] - y)
            xdist = max(1, xdiff + (s[2] - ydiff))
            #print('x', x, 'y', y, 's', s, 'd', d, 'xdist', xdist, 'xdiff', xdiff, 'ydiff', ydiff)
            x += xdist
            break
    if found:
        print(x, y)
        print(x*4000000 + y)
        break
    if not skip:
        x += 1
    if x > maxx:
        y += 1
        print(y)
        x = minx
    if y > maxx:
        print('not found')
        break
    