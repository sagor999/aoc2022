file1 = open('data.txt', 'r')
Lines = file1.readlines()

# static dictionary
myHandScoreDict = {'Rock': 1, 'Paper': 2, 'Scissors': 3}
mapHandToSign = {'X': 'Rock', 'Y': 'Paper', 'Z': 'Scissors', 'A': 'Rock', 'B': 'Paper', 'C': 'Scissors'}
score = 0
for line in Lines:
    line = line.strip()
    line = line.split(" ")
    opHand = mapHandToSign[line[0]]
    myHand = mapHandToSign[line[1]]
    score += myHandScoreDict[myHand]
    if opHand == myHand:
        score += 3
    else:
        if myHand == 'Rock' and opHand == 'Scissors':
            score += 6
        elif myHand == 'Paper' and opHand == 'Rock':
            score += 6
        elif myHand == 'Scissors' and opHand == 'Paper':
            score += 6
print(score)