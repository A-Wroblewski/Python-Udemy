inputs = int(input())

numbers = [int(input()) for _ in range(inputs)]

current_highest = 0
highest_registered = 0

for i in range(len(numbers)):
    if numbers[i] == numbers[i - 1]:
        current_highest += 1

    else:
        current_highest = 1

    if current_highest > highest_registered:
        highest_registered = current_highest

print(highest_registered)
