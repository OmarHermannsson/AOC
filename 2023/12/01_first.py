import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

def getCharPower(stringLength, charRange):
    charpowers = []
    for x in range(0, stringLength):
            charpowers.append(len(charRange)**(stringLength - x - 1))
    return charpowers

def Generator(stringLength, charRange):
    workbench = []
    results = []
    charpowers = getCharPower(stringLength, charRange)
    for x in range(0, stringLength):
            while len(workbench) < len(charRange)**stringLength:
                    for char in charRange:
                            for z in range(0, charpowers[x]):
                                    workbench.append(char)
            results.append(workbench)
            workbench = []
    results = ["".join(result) for result in list(zip(*results))]
    return results

def get_combinations(num):
    return Generator(num, '.#')

def get_counts(rec):
    counts = []
    count = 0
    for x, char in enumerate(rec):
        if char == '#':
            count += 1
        elif char == '.':
            if rec[max(0,x-1)] == '#':
                counts.append(count)
            count = 0
    if count > 0:
         counts.append(count)
    count_str = ','.join(map(str,counts))
    return count_str

def get_possible(rec, par):
    arrangements = 0
    possible = []
    lrec = list(rec)
    wildcards = [i for i,x in enumerate(lrec) if x=='?']
    combinations = get_combinations(len(wildcards))
    for c in combinations:
        for i, w in enumerate(wildcards):
            lrec[w] = c[i]
        if get_counts(lrec) == par:
            possible.append(lrec.copy())
            arrangements += 1
    return possible, arrangements
            

sum = 0
for line in input_file:
    rec, par = line.strip().split()
    all, num = get_possible(rec, par)
    sum += num

print ("Num:", sum)
