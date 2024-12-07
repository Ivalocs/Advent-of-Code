import re

input = open('input.txt', 'r')
ans = 0
for line in input.readlines():
    operations = re.findall("mul\([0-9]+,[0-9]+\)", line)
    for operation in operations:
        numbers = re.findall("[0-9]+", operation)
        ans += int(numbers[0]) * int(numbers[1])

print(ans)
