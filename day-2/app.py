selection_points = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

def outcome(home, away):
    sum = selection_points[home]
    if(home == 'X' and away == 'A' or
    home == 'Y' and away =='B' or
    home == 'Z' and away == 'C'):
        sum += 3
    elif home == 'X' and away == 'C':
        sum += 6
    elif home == 'Y' and away == 'A':
        sum += 6
    elif home == 'Z' and away == 'B':
        sum += 6
    return sum
    
point_total = 0
with open('./input.txt') as file:
    for line in file.readlines():
        selections = line.split()
        point_total += outcome(selections[1], selections[0])

print(point_total)

loss_points = {
    'A': 3,
    'B': 1,
    'C': 2
}

win_points = {
    'A': 2,
    'B': 3,
    'C': 1
}

draw_points = {
    'A': 1,
    'B': 2,
    'C': 3
}

def outcome2(opponent_pick, outcome):
    sum = 0
    if outcome == 'X':
        sum += loss_points[opponent_pick]
    elif outcome == 'Y':
        sum += draw_points[opponent_pick] + 3
    elif outcome == 'Z':
        sum += win_points[opponent_pick] + 6
    return sum

point_total2 = 0
with open('./input.txt') as file:
    for line in file.readlines():
        selections = line.split()
        point_total2 += outcome2(selections[0], selections[1])

print(point_total2)
