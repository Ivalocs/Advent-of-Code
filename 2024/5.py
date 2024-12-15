from functools import cmp_to_key
import re

input = open('input.txt', 'r')

graph = {}

def Part_1(orderings):
    ans = 0
    for order in orderings:
        numbers = re.findall("[0-9]+", order)
        is_correct = True
        for i in range(0, len(numbers)):
            for j in range(0, i):
                a = numbers[j]
                b = numbers[i]
                if (b in graph) and (a in graph[b]):
                    is_correct = False
            for j in range(i+1, len(numbers)):
                a = numbers[i]
                b = numbers[j]
                if (b in graph) and (a in graph[b]):
                    is_correct = False
        if is_correct:
            ans += int(numbers[len(numbers) // 2])
    return ans

def Compare(a, b):
    if a in graph and b in graph[a]:
        return -1
    if b in graph and a in graph[b]:
        return 1
    return 0

def Part_2(orderings):
    ans = 0
    interested = []
    for order in orderings:
        numbers = re.findall("[0-9]+", order)
        is_correct = True
        for i in range(0, len(numbers)):
            for j in range(0, i):
                a = numbers[j]
                b = numbers[i]
                if (b in graph) and (a in graph[b]):
                    is_correct = False
            for j in range(i+1, len(numbers)):
                a = numbers[i]
                b = numbers[j]
                if (b in graph) and (a in graph[b]):
                    is_correct = False
        if not is_correct:
            interested.append(numbers)
    for order in interested:
        sorted_ordering = sorted(order, key=cmp_to_key(Compare))
        ans += int(sorted_ordering[len(order) // 2])
    return ans

lines = input.readlines()
idx = -1
for line in lines:
    idx += 1
    if line == '\n':
        break
    numbers = re.findall("[0-9]+", line)
    if numbers[1] not in graph:
        graph[numbers[1]] = set()
    if numbers[0] in graph:
        graph[numbers[0]].add(numbers[1])
    else:
        graph[numbers[0]] = set([numbers[1]])

orderings = lines[idx+1:]
print(Part_1(orderings))
print(Part_2(orderings))
   
