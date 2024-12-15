input = open('input.txt', 'r')
lines = [list(line.rstrip()) for line in input.readlines()]

# 0 -> up, 1 -> right, 2 -> down, 3 -> left
start = (0, 0)

for i in range(0, len(lines)):
    for j in range(0, len(lines[0])):
        if lines[i][j] == '^':
            start = (i, j)
            break


def Part_1(x, y, lines):
    states = [[[False for i in range(len(lines[0]))] for j in range(len(lines))] for k in range(4)]
    ans = 0
    curx = x
    cury = y
    direction = 0
    is_cycle = False
    while True:
        if states[direction][curx][cury] == True:
            is_cycle = True
            break
        new_place = True
        for i in range(0, 4):
            new_place = new_place and not (states[i][curx][cury])
        ans += int(new_place)
        states[direction][curx][cury] = True
        newx = curx
        newy = cury
        if direction == 0:
            if newx == 0:
                break
            newx -= 1
        if direction == 2:
            if newx == len(lines)-1:
                break
            newx += 1
        if direction == 3:
            if newy == 0:
                break
            newy -= 1
        if direction == 1:
            if newy == len(lines[0])-1:
                break
            newy += 1
        if lines[newx][newy] == '#':
            direction = (direction + 1) % 4
        else:
            curx = newx
            cury = newy
    return (ans, is_cycle)


def Part_2(lines):
    ans = 0
    for i in range(len(lines)):
        for j in range(len(lines[0])):
            if (lines[i][j] == '.'):
                lines[i][j] = '#'
                ans += int(Part_1(start[0], start[1], lines)[1])
                lines[i][j] = '.'
    return ans


print(Part_1(start[0], start[1], lines)[0])
print(Part_2(lines))


