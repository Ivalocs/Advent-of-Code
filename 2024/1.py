input = open('input.txt', 'r')
A = []
B = []
for line in input.readlines():
    numbers = [int(x) for x in line.rstrip().split(' ') if x != '']
    A.append(numbers[0])
    B.append(numbers[1])

A.sort()
B.sort()

# Part 1
ans = 0
for i in range(len(A)):
    ans += abs(A[i] - B[i])
print(ans)

# Part 2
i = 0
j = 0
ans_2 = 0
while (i < len(B)):
    counter_1 = 1
    counter_2 = 0
    while (i+1 < len(A) and A[i] == A[i+1]):
        counter += 1
        i += 1
    while (j < len(B) and B[j] <= A[i]):
        if (B[j] == A[i]):
            counter_2 += 1
        j += 1
    ans_2 += A[i] * counter_1 * counter_2
    i += 1

print(ans_2)
input.close()
