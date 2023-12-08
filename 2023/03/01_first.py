import os
import pathlib

script_path = pathlib.Path(__file__).parent.resolve()

#input_file = open(os.path.join(script_path, 'sample.txt'))

filename = "_sample.txt"
filename = "_input.txt"
input_file = open(os.path.join(script_path, filename))

schema = []
for line in input_file:
    schema.append(line.strip())

schema_xlen = len(schema)
schema_ylen = len(schema[0])

def is_neighbor_symbol(x,y):
    x1 = max(0,x-1)
    x2 = min(schema_xlen-1, x+1)
    y1 = max(0,y-1)
    y2 = min(schema_ylen-1, y+1)

    for xx in range(x1, x2+1):
        for yy in range(y1,y2+1):
            char = schema[xx][yy] 
            if not char.isdigit() and char != ".":
                return True
    return False

sum = 0
for x in range(len(schema)):
    value = ""
    first_digit = False
    last_digit = False
    is_part = False
    for y in range(len(schema[x])):        
        char = schema[x][y]
        if char.isdigit():
            value += char
            if is_neighbor_symbol(x,y):
                is_part = True
            if not first_digit:
                first_digit = True
            if y == len(schema[x])-1 or not schema[x][y+1].isdigit():
                last_digit = True
                #print("Value:", value)
                if is_part:
                    #print ("Is part:", value)
                    sum += int(value)
                else:
                    #print("Is not part:", value)
                    pass
        else:
            value = ""
            first_digit = False            
            last_digit = False
            is_part = False

#sample sum is 4361
print("Sum:", sum)