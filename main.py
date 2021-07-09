numbers = [23,25,26,30,35,23,46,55]

"""
mean
"""
sum = 0

for i in numbers:
     
    sum += i

mean = sum / len(numbers)

print("Mean: " , mean)


"""

median

"""

length = len(numbers)
for i in range(length):
    for j in range(length - i):
        a = numbers[j]
        if a != numbers[-1]:
            b = numbers[j + 1]
            if a > b:
                numbers[j] = b
                numbers[j + 1] = a


half = round(len(numbers) / 2)
median = 0
if len(numbers) % 2 == 0:
    first = numbers[half]
    second = numbers[half + 1]

    median = first + second / 2
else:
    median = numbers[half]

print(median)


