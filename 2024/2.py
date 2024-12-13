from copy import deepcopy

def Check(a, b, c):
    if (c == True):
        return (b > a) and (b - a >= 1) and (b - a <= 3)
    else:
        return (a > b) and (a - b >= 1) and (a - b <= 3)


input = open('input.txt', 'r').read().strip()
# Part 1
safe_reports = 0
for line in input.split('\n'):
    numbers = [int(x) for x in line.rstrip().split(' ')]
    is_increasing = True
    is_safe = True
    for i in range(1, len(numbers)):
        if (i == 1):
            if (numbers[i] == numbers[i-1]):
                is_safe = False
            if (numbers[i] < numbers[i-1]):
                is_increasing = False
        is_safe = is_safe and Check(numbers[i-1], numbers[i], is_increasing)
    if (is_safe):
        safe_reports += 1

print(safe_reports)


def O_N_N_Code(numbers_origin):
    for i in range(0, len(numbers_origin)):
        numbers = deepcopy(numbers_origin)
        numbers.pop(i)
        is_increasing = True
        is_safe = True
        for i in range(1, len(numbers)):
            if (i == 1):
                if (numbers[i] == numbers[i-1]):
                    is_safe = False
                if (numbers[i] < numbers[i-1]):
                    is_increasing = False
            is_safe = is_safe and Check(numbers[i-1], numbers[i], is_increasing)
        if (is_safe):
            return True
    return False


ans = 0
for line in input.split('\n'):
    numbers = [int(x) for x in line.rstrip().split(' ')]
    if (O_N_N_Code(numbers) != O_N_Code(numbers)):
        print(O_N_N_Code(numbers))
        print(O_N_Code(numbers))
        print(numbers)
        ans += 1
print(ans)
    
