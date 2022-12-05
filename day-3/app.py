import string

class ElfGroup:
    def __init__(self) -> None:
        self.group = []

def split_list(str):
    characters = list(str)
    middle_point = int((len(characters) - 1) / 2)
    first_compartment = characters[:middle_point]
    second_compartment = characters[middle_point:]
    second_compartment.pop()
    return (set(first_compartment), set(second_compartment))

def get_priority_score(str):
    sum = 0
    compartments = split_list(str)
    for el in compartments[0]:
        if el in compartments[1]:
            if el.isupper():
                sum += int(string.ascii_uppercase.index(el) + 27)
            else:
                sum += int(string.ascii_lowercase.index(el) + 1)
            break
    return sum

priority_sum = 0
with open('./input.txt') as file:
    for line in file.readlines():
        priority_sum += get_priority_score(line)

print(priority_sum)

# part 2
badge_sum = 0
with open('./input.txt') as file:
    group_of_elves = ElfGroup()
    for idx, line in enumerate(file.readlines(), 1):
        if idx % 3 == 0:
            characters = list(line.strip())
            group_of_elves.group.append(set(characters))
            group_of_elves.group.sort(key=len, reverse=True)
            print(group_of_elves.group)
            for char in group_of_elves.group[0]:
                if char in group_of_elves.group[1] and char in group_of_elves.group[2]:
                    if char.isupper():
                        badge_sum += int(string.ascii_uppercase.index(char) + 27)
                    else:
                        badge_sum += int(string.ascii_lowercase.index(char) + 1)
                    break
            group_of_elves = ElfGroup()
        else:
            characters = list(line.strip())
            group_of_elves.group.append(set(characters))
            
print(badge_sum)


