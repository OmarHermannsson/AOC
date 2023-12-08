
import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
#filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

element = None

class Element:
    def __init__(self, element_str):
        self.id = element_str[:3]
        self.left, self.right = element_str[6:].strip('()').replace(' ','').split(',')
    def __repr__(self):
        return self.id
    def __str__(self):
        return self.id


element_table = {}

for i, line in enumerate(input_file):
    if i == 0:
        instructions = list(line)
    elif i > 1:
        element = Element(line)
        element_table[element.id] = element
    
    if i == 2:
        first = element.id
    
print(element_table)

cnt = 0
mod = len(instructions)
next = first

print ("First:", first)
while True:
    instruction = instructions[cnt%mod]
    next = element_table[str(next)]
    cnt += 1
    if str(next) == 'ZZZ':
        break
    #print(next,end=', ')


print("Steps:", cnt)