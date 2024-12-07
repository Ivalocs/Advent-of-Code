input = open('input.txt', 'r')
A = []
B = []
for line in input.readlines():
    numbers = [int(x) for x in line.rstrip().split(' ') if x != '']
    A.append(numbers[0])
    B.append(numbers[1])

A.sort()
B.sort()
ans = 0
for i in range(len(A)):
    ans += abs(A[i] - B[i])

print(ans)
