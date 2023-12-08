file = open('input')
#file = open('sample')

totalSum = 0
for line in file:
    digits = list(filter(str.isdigit, line))
    lineSum = digits[0] + digits[-1]
    print("Sum:", lineSum)
    totalSum += int(lineSum)

print("Total:", totalSum)