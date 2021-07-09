import pandas as pd
import csv


with open('data.csv') as f:
    reader = csv.reader(f)

    fd = list(reader)



fd.pop(0)
newData = []

for i in range(len(fd)):
    num = fd[i][1]

    newData.append(float(num))

sum = 0
print(newData)
for i in newData:
     
    sum += i

mean = sum / len(newData)

print("Mean: " , mean)


n = len(newData)

newData.sort()

if n % 2 == 0:
    median1 = float(newData[n // 2])
    median2 = float(newData[n // 2 - 1])
    median = median1 + median2 / 2
    print(n)
else:
    median = newData[n // 2]    
    print(n)


print(median)