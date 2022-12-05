import re
from queue import LifoQueue

class Instruction:
    def __init__(self, amount, from_stack, to_stack) -> None:
        self.amount = amount
        self.from_stack = from_stack
        self.to_stack = to_stack

crates = {
    1: LifoQueue(),
    2: LifoQueue(), 
    3: LifoQueue(),
    4: LifoQueue(), 
    5: LifoQueue(), 
    6: LifoQueue(), 
    7: LifoQueue(), 
    8: LifoQueue(), 
    9: LifoQueue() 
}

#     [H]         [H]         [V]    
#     [V]         [V] [J]     [F] [F]
#     [S] [L]     [M] [B]     [L] [J]
#     [C] [N] [B] [W] [D]     [D] [M]
# [G] [L] [M] [S] [S] [C]     [T] [V]
# [P] [B] [B] [P] [Q] [S] [L] [H] [B]
# [N] [J] [D] [V] [C] [Q] [Q] [M] [P]
# [R] [T] [T] [R] [G] [W] [F] [W] [L]
#  1   2   3   4   5   6   7   8   9 
# not sure how to parse text and get this dataset

one = ['R', 'N', 'P', 'G']
two = ['T', 'J', 'B', 'L', 'C', 'S', 'V', 'H']
three = ['T', 'D', 'B', 'M', 'N', 'L']
four = ['R', 'V', 'P', 'S', 'B']
five = ['G', 'C', 'Q', 'S', 'W', 'M', 'V', 'H']
six = ['W', 'Q', 'S', 'C', 'D', 'B', 'J']
seven = ['F', 'Q', 'L']
eight = ['W', 'M', 'H', 'T', 'D', 'L', 'F', 'V']
nine = ['L', 'P', 'B', 'V', 'M', 'J', 'F']

letters = [one, two, three, four, five, six, seven, eight, nine]
for idx in range(len(letters)):
    for letter in letters[idx]:
        crates[idx + 1].put(letter)

def parse_instruction(str):
    instructions = re.findall(r'\d+', str)
    for idx in range(len(instructions)):
        num = int(instructions[idx])
        instructions[idx] = num
    return Instruction(instructions[0], instructions[1], instructions[2])

def execute_instruction(instruction: Instruction):
    for itr in range(0, instruction.amount):
        item_to_remove = crates[instruction.from_stack].get()
        crates[instruction.to_stack].put(item_to_remove)

with open('./input.txt') as file:
    for line in file.readlines():
        execute_instruction(parse_instruction(line))

str_9000 = ""
for key in crates:
    str_9000 += crates[key].get()

print(str_9000)

# part 2

crates_9001 = {
    1: one,
    2: two, 
    3: three,
    4: four, 
    5: five, 
    6: six, 
    7: seven, 
    8: eight, 
    9: nine 
}

# not most efficient maybe used doubly linked list
def execute_9001(instruction: Instruction):
    index = len(crates_9001[instruction.from_stack]) - instruction.amount
    stack = crates_9001[instruction.from_stack][index:]
    crates_9001[instruction.from_stack] = crates_9001[instruction.from_stack][:index]
    crates_9001[instruction.to_stack].extend(stack)

with open('./input.txt') as file:
    for line in file.readlines():
        execute_9001(parse_instruction(line))

str_9001 = ""
for key in crates_9001:
    arr = crates_9001[key]
    str_9001 += (arr[len(arr) - 1])

print(str_9001)
