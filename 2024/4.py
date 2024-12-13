input = open('input.txt', 'r')
lines = input.readlines()

MOVEMENTS = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
MAS_MOVEMENTS = [(1, 1), (-1, 1)]

def Part_1():
    ans = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] != 'X':
                continue
            for x, y in MOVEMENTS:
                s = 'X'
                for k in range(1, 4):
                    xx = i + k * x
                    yy = j + k * y
                    if (xx >= 0 and yy >= 0 and xx < len(lines) and yy < len(lines[xx])):
                        s += lines[xx][yy]
                if (s == 'XMAS'):
                    ans += 1
    return ans

def Part_2():
    ans = 0
    for i in range(0, len(lines)):
        for j in range(0, len(lines[i])):
            if lines[i][j] != 'A':
                continue
            found = True
            for x, y in MAS_MOVEMENTS:
                s = ''
                for k in range(-1, 2):
                    xx = i + k * x
                    yy = j + k * y
                    if (xx >= 0 and yy >= 0 and xx < len(lines) and yy < len(lines[xx])):
                        s += lines[xx][yy]
                if (s != 'SAM' and s != 'MAS'):
                    found = False
            if found:
                ans += 1
    return ans

print(Part_1())
print(Part_2())
   
