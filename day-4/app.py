def generate_tuples(str):
    pairs = str.strip().split(',')
    first_section = [int(x) for x in pairs[0].split('-')]
    second_section = [int(x) for x in pairs[1].split('-')]
    return (first_section, second_section)

def check_ranges(tuple):
    if tuple[0][0] <= tuple[1][0] and tuple[0][1] >= tuple[1][1]:
        return True
    elif tuple[0][0] >= tuple[1][0] and tuple[0][1] <= tuple[1][1]:
        return True
    return False

pair_count = 0
with open('./input.txt') as file:
    for line in file.readlines():
        section_tuple = generate_tuples(line)
        if check_ranges(section_tuple):
            pair_count += 1

print(pair_count)

# part 2

overlap_count = 0
def check_overlap(tuple):
    if tuple[0][0] <= tuple[1][1] and tuple[1][0] <= tuple[0][1]:
        return True
    return False

with open('./input.txt') as file:
    for line in file.readlines():
        section_tuple = generate_tuples(line)
        if check_overlap(section_tuple):
            overlap_count += 1

print(overlap_count)