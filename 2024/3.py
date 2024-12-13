import re

def Part_1(lines):
    ans = 0
    for line in lines:
        operations = re.findall("mul\([0-9]+,[0-9]+\)", line)
        for operation in operations:
            numbers = re.findall("[0-9]+", operation)
            ans += int(numbers[0]) * int(numbers[1])
    return ans

def Part_2(lines):
    ans = 0
    flag = True
    for line in lines:
        iterator = re.finditer("mul\([0-9]+,[0-9]+\)|do\(\)|don't\(\)", line)
        for operation in iterator:
            if operation.group() == "do()":
                flag = True
            elif operation.group() == "don't()":
                flag = False
            else:
                numbers = re.findall("[0-9]+", operation.group())
                ans += int(flag) * int(numbers[0]) * int(numbers[1])
    return ans

input = open('input.txt', 'r')
lines = input.readlines()
ans_1 = Part_1(lines)
ans_2 = Part_2(lines)

print(ans_1)
print(ans_2)
input.close()
