import os
import pathlib

path = pathlib.Path(__file__).parent.resolve()

file = open(os.path.join(path, '../1/input'))


def digitafy(line):
    text = ""
    for x in range(len(line)):
        if line[x].isdigit: text += line[x]
        if line[x:].startswith("one"): text += "1"
        if line[x:].startswith("two"): text += "2"
        if line[x:].startswith("three"): text += "3"
        if line[x:].startswith("four"): text += "4"
        if line[x:].startswith("five"): text += "5"
        if line[x:].startswith("six"): text += "6"
        if line[x:].startswith("seven"): text += "7"
        if line[x:].startswith("eight"): text += "8"
        if line[x:].startswith("nine"): text += "9"
    return text


totalSum = 0
for line in file:
    digits = list(filter(str.isdigit, digitafy(line)))
    try:
        lineSum = digits[0] + digits[-1]
    except IndexError:
        print ("digits:", digits)
        print ("line:", line)
    print("Sum:", lineSum)
    totalSum += int(lineSum)

print("Total:", totalSum)