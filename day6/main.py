file1 = open('data.txt', 'r')
Lines = file1.readlines()

foundStartMarker = False
for line in Lines:
    line = line.strip()
    for i in range(len(line)):
        if i < 4:
            continue
        l = line[i-4:i]
        # check if all characters are unique
        if len(set(l)) == 4 and foundStartMarker == False:
            print(f'found start marker at: {i}')
            foundStartMarker = True
            continue
        if i < 14:
            continue
        l = line[i-14:i]
        if len(set(l)) == 14:
            print(f'found message marker at: {i}')
            break