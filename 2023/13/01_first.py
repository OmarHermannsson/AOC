import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))


patterns = []
pattern = []

for line in input_file:
    if line.strip() == "":
        patterns.append(pattern.copy())
        pattern = []
    else:
        pattern.append(line.strip())
patterns.append(pattern.copy())

def find_h_line(pattern):
    l0 = len(pattern[0])
    candidates = dict.fromkeys(range(l0), 0)
    for line in pattern:        
        for x, _ in enumerate(line):
            if x == 0:
                continue
            l1 = len(line[:x])
            l2 = len(line[x:])
            ml = min(l1,l2)
            if line[x-ml:x] == line[x:ml+x][::-1]:
                #print("M:", line, x+1)
                candidates[x] += 1
    for c in candidates:
        if candidates[c] == len(pattern):
            #print("V:", c)
            return c
    return 0

def find_v_line(pattern):
    l0 = len(pattern)
    for x, _ in enumerate(pattern):
        if x == 0:
            continue
        l1 = len(pattern[:x])
        l2 = len(pattern[x:])
        ml = min(l1,l2)
        if pattern[x-ml:x] == pattern[x:ml+x][::-1]:
            #print("H:", x)
            return 100*x
    return 0

def find_line(pattern):
    sum = find_h_line(pattern)
    sum += find_v_line(pattern)
    return sum

sum = 0
for pattern in patterns:
    print("Pattern:", pattern)
    sum += find_line(pattern)
    
print("Sum:", sum)