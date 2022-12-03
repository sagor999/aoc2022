file1 = open('data.txt', 'r')
Lines = file1.readlines()

count = 0
count2 = 0
group = []
for line in Lines:
    content = line.strip()
    first_half = content[:len(content)//2]
    second_half = content[len(content)//2:]
    unique_first_half = set(first_half)
    unique_second_half = set(second_half)
    # find common characters
    common = unique_first_half.intersection(unique_second_half)
    # convert character a through z to 1 through 26 and  A through Z to 27 through 52
    common = [ord(c) - 38 if c.isupper() else ord(c) - 96 for c in common]
    count += sum(common)

    group.append(content)
    if len(group) == 3:
        print(group)
        common = set(group[0]).intersection(set(group[1]), set(group[2]))
        common = [ord(c) - 38 if c.isupper() else ord(c) - 96 for c in common]
        count2 += sum(common)
        group = []

print(count)
print(count2)