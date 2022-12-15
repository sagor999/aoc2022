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

y = 2000000
nump = 0
for x in range(minx, maxx+1):
    for s in sensors:
        d = get_distance(x, y, s[0], s[1])
        if d <= s[2]:
            beacon_exists = False
            for b in beacons:
                if get_distance(x, y, b[0], b[1]) == 0:
                    beacon_exists = True
                    break
            if not beacon_exists:
                nump += 1
            break 

print(nump)
    