
import os
from math import lcm

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample3.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

element = None

starts = []
ends = []

class Element:
    def __init__(self, element_str):
        self.id = element_str[:3]
        self.left, self.right = element_str[6:].strip('()\n').replace(' ','').split(',')
        if self.id.endswith('A'):
            starts.append(self.id)
        #elif self.id.endswith('Z'):
        #    ends.append(self.id)
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
    
cnt = 0
mod = len(instructions)
nexts = starts

print("Starts:", starts)
#print("Ends:  ", ends)

while True:
    instruction = instructions[cnt%mod]
    currents = nexts
    #nexts = []
    end = True
    for i, n in enumerate(currents):
        next = element_table[n].get_next(instruction)
        if not next.endswith('Z'):
            end = False
        else:
            ends.append(cnt+1)
        nexts[i] = next

    cnt += 1

    if end:
        break
    if len(ends) == len(starts):
        break

print("Ends:", ends)

ret = 1
for x in ends:
    ret = lcm(ret, x)

print("Steps:", ret)