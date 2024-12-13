list1 = []
list2 = []

with open("/Users/ltj623/Desktop/input.txt", "r") as file:
    for line in file:
        numbers = line.strip().split()
        list1.append(int(numbers[0]))
        list2.append(int(numbers[1]))

list1.sort()
list2.sort()

total = 0

for i in range(len(list1)):
    total += abs(list1[i] - list2[i])
print(total)