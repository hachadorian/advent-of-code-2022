class Elf:
    def __init__(self) -> None:
        self.items = []
    
    def total(self):
        return sum(self.items)

highest = -1

with open('./input.txt') as file:
    new_elf = Elf()
    for line in file.readlines():
        if len(line) != 1:
            new_elf.items.append(int(line))
        else:
            if(new_elf.total() > highest):
                highest = new_elf.total()        
            new_elf = Elf()

print(highest)

# part 2 probably a better way to do it but lazy

elves = []

with open('./input.txt') as file:
    new_elf = Elf()
    for line in file.readlines():
        if len(line) != 1:
            new_elf.items.append(int(line))
        else:
            elves.append(new_elf.total())        
            new_elf = Elf()

elves.sort(reverse=True)
print(sum(elves[:3]))