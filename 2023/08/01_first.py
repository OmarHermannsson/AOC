
import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

element = None

class Element:
    def __init__(self, element_str):
        self.id = element_str[:3]
        self.left, self.right = element_str[6:].strip('()\n').replace(' ','').split(',')
    def __repr__(self):
        return self.id
    def __str__(self):
        return self.id
    def get_next(self, token):
        if token == 'L':
            return self.left
        if token == 'R':
            return self.right
        else:
            raise ValueError(f"{token} invalid value")


element_table = {}

for i, line in enumerate(input_file):
    if i == 0:
        instructions = list(line.strip())
    elif i > 1 and len(line)>1:
        element = Element(line)
        element_table[element.id] = element
    
    if i == 2:
        first = element.id

    #if element is not None and (element.id == element.left == element.right):
    #    print ("LAST?:", element)
    
cnt = 0
mod = len(instructions)
next = 'AAA'
last = 'ZZZ'

while True:
    instruction = instructions[cnt%mod]
    next = element_table[next].get_next(instruction)
    cnt += 1
    #if cnt%10000 == 0:
    #    print("Count:", cnt, " - instruction:", instruction, " - mod:", cnt%mod, " - next:", next, " - last:", last)
    if next == last:
        break

print("Steps:", cnt)