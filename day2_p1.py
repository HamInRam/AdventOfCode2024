res = 0
with open("/Users/ltj623/Desktop/input.txt", "r") as file:
    for line in file:
        numbers = list(map(int,line.strip().split()))

        if (len(numbers) == len(set(numbers))) and (all(x < y and 1<=abs(x-y)<=3 for x, y in zip(numbers, numbers[1:])) or all(x > y and 1<=abs(x-y)<=3 for x, y in zip(numbers, numbers[1:]))):
            res += 1
print(res)


