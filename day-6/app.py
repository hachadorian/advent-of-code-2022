def parse_transmission(arr):
    for idx in range(len(arr)):
        str = {}
        for i in range(idx, idx + 4):
            if arr[i] not in str:
                str[arr[i]] = arr[i]
            elif arr[i] in str:
                break
        if len(str) == 4:
            return idx + 4
        else:
            str = {}

with open('./input.txt') as file:
    for line in file.readlines():
        print(parse_transmission(list(line)))


def parse_transmission2(arr):
    for idx in range(len(arr)):
        str = {}
        for i in range(idx, idx + 14):
            if arr[i] not in str:
                str[arr[i]] = arr[i]
            elif arr[i] in str:
                break
        if len(str) == 14:
            return idx + 14
        else:
            str = {}

with open('./input.txt') as file:
    for line in file.readlines():
        print(parse_transmission2(list(line)))



