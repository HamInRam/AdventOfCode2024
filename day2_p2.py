def safeWithNoErrorCnt(numbers):
    increasing = all(x < y and 1<=abs(x-y)<=3 for x, y in zip(numbers, numbers[1:]))
    decreasing = all(x > y and 1<=abs(x-y)<=3 for x, y in zip(numbers, numbers[1:]))

    return increasing or decreasing

def safeWithErrorCnt(numbers):
    if safeWithNoErrorCnt(numbers):
        return True

    for i in range(len(numbers)):
        temp = numbers[:i] + numbers[i + 1:]
        if safeWithNoErrorCnt(temp): 
            return True

    return False 

res = 0
with open("/Users/ltj623/Desktop/input.txt", "r") as file:
    for line in file:
        numbers = list(map(int, line.strip().split()))
        if safeWithErrorCnt(numbers):
            res += 1

print(res)
