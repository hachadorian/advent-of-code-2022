class Elf:
    def __init__(self) -> None:
        self.items = []
    
    def total(self):
        return sum(self.items)

highest = -1

with open('./input.txt') as file:
    newElf = Elf()
    for line in file.readlines():
        if len(line) != 1:
            newElf.items.append(int(line))
        else:
            if(newElf.total() > highest):
                highest = newElf.total()        
            newElf = Elf()

print(highest)
