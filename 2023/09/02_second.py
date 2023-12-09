import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

history = []

def get_next_value(values):
    changes = []
    for x, val in enumerate(values):
        if x < len(values)-1:
            changes.append(values[x+1] - values[x])
    if len(values) > 0:
        return values[0] - get_next_value(changes)
    else:
        return 0




for line in input_file:
    if len(line) > 1:
        history.append(list(map(int,line.strip().split())))

sum = 0
for line in history:
    sum += get_next_value(line)
    

print("Sum:", sum)