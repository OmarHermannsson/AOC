import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
#filename = '_input.txt'

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


for p in patterns:
    print(p)
    second_line = p[1]
    for i, tile in enumerate(second_line):
        try:
            if second_line[i] == second_line[i+1] and second_line[i-1] == second_line[i+2] and second_line[i-2] == second_line[i+3]:
                print(i,len(second_line[:i+1]))                
        except IndexError:
            pass
