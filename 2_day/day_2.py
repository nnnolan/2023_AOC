with open(r'2_day/input.txt') as f:
    lines = f.readlines()
    # drop \n
    lines = [line.strip() for line in lines]
    red, green, blue = 12, 13, 14
    
import re

possible = []
for line in lines:
    colon = line.find(':')
    space = len('Game ')
    game_number = int(line[space:colon])
    game = line[colon + 2:].rstrip().split('; ')
    answers = []
    for set in game:
        for cube in set.split(', '):
            num = int(cube[:2].strip())
            color = cube[2:].strip()
            if color == 'red' and num > red:
                answers.append(False)
            elif color == 'blue' and num > blue:
                answers.append(False)
            elif color == 'green' and num > green:
                answers.append(False)
            else:
                answers.append(True)

    if all(answers):
        possible.append(game_number)

print(sum(possible))


# part 2, minimum number of cubes

for line in lines:
    colon = line.find(':')
    space = len('Game ')
    game_number = int(line[space:colon])
    game = line[colon + 2:].rstrip().split('; ')
    answers = []
    for set in game:
        for cube in set.split(', '):
            num = int(cube[:2].strip())
            color = cube[2:].strip()
            if color == 'red' and num > red:
                answers.append(False)
            elif color == 'blue' and num > blue:
                answers.append(False)
            elif color == 'green' and num > green:
                answers.append(False)
            else:
                answers.append(True)

    if all(answers):
        possible.append(game_number)


for line in lines:
    
    colon = line.find(':')
    space = len('Game ')
    game_number = int(line[space:colon])
    game = line[colon + 2:].rstrip().split('; ')
    answers = []

    print(g