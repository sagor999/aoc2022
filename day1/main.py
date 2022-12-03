file1 = open('data.txt', 'r')
Lines = file1.readlines()
  
max_calories = 0
calories = []
for line in Lines:
    if not line.strip():
        calories.append(max_calories)
        max_calories = 0
        continue
    cal = int(line)
    max_calories += cal
calories.append(max_calories)
# sort calories
calories.sort(reverse=True)
print(calories[0])
print(calories[0]+calories[1]+calories[2])
