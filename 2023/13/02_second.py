import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample3.txt'
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
    sum = 0
    old_hsum = find_h_line(pattern)
    old_vsum = find_v_line(pattern)
    new_vsum_dict = {}
    times = 0
    for y, line in enumerate(pattern):
        for x, _ in enumerate(line):
            #new_pattern = pattern.copy()
            new_pattern = list(map(list, pattern))
            new_pattern[y][x] = "." if pattern[y][x] == "#" else "#"
            new_hsum = find_h_line(new_pattern)
            new_vsum = find_v_line(new_pattern)
            if new_hsum != old_hsum and new_hsum > 0:
                sum += new_hsum
                times += 1
                return new_hsum
            if new_vsum != old_vsum and new_vsum > 0:
                new_vsum_dict[int(new_vsum/100)] = True
                return new_vsum
                #sum += new_vsum
                #times += 1
            #sum += new_hsum
            #sum += new_vsum
            #if sum > 0:
            #    return sum
    
    if len(new_vsum_dict) == 1:
        sum += next(iter(new_vsum_dict))
        times += 1

    if times != 1:
        print("Times:", times, pattern, new_vsum_dict.keys(), old_hsum+old_vsum)
    if len(new_vsum_dict.keys()) > 1:
        print("Dict:", times, pattern, new_vsum_dict.keys())
    return old_hsum+old_vsum

sum = 0
for pattern in patterns:
    #print("Pattern:", pattern)
    sum += find_line(pattern)
    
print("Sum:", sum)

#42996