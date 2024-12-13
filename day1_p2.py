list1 = []
list2 = []

with open("/Users/ltj623/Desktop/input.txt", "r") as file:
    for line in file:
        numbers = line.strip().split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

total = 0
h = {}

for i, num in enumerate(list1):
    if num not in h:
        h[num] = num * list2.count(num)
    total += h[num]

print(total)