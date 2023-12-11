import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
#filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))


class Pipe:    
    def __init__(self, x, y, pipe_type):
        self.pipe_types = ['|','-','L','J','7','F','.','S']
        self.x = x
        self.y = y
        if pipe_type in self.pipe_types:
            self.pipe_type = pipe_type
        else:
            raise ValueError(f"'{pipe_type}' is not a valid pipe type")
        
    def get_next_pipes(self):
        pipes = []
        if self.pipe_type == '|':
            pipes.append((x,y-1))
            pipes.append((x,y+1))
        elif self.pipe_type == '-':
            pipes.append((x-1,y))
            pipes.append((x+2,y))
        elif self.pipe_type == 'L':
            pipes.append((x,y-1))
            pipes.append((x+1,y))
        elif self.pipe_type == 'J':
            pipes.append((x,y-1))
            pipes.append((x-1,y))
        elif self.pipe_type == '7':
            pipes.append((x-1,y))
            pipes.append((x,y-1))
        elif self.pipe_type == 'F':
            pipes.append((x+1,y))
            pipes.append((x,y-1))
        elif self.pipe_type == '.':
            pass
        elif self.pipe_type == 'S':
            pass
    
    def __str__(self):
        return self.pipe_type
    
    def __repr__(self):
        return self.pipe_type

start = None
tile_grid = {}
for y, line in enumerate(input_file):
    for x, char in enumerate(line.strip()):
        tile_grid[(x,y)] = Pipe(x,y,char)
        if char == 'S':
            start = (x,y)

def get_neighbors(x,y):
    neighbors = []
    x1 = max(0, x-1)
    x2 = min(len(tile_grid[0]), x+1)
    y1 = max(0,y-1)
    y2 = min(len(tile_grid), y+1)

    if x1 < x:
        neighbors.append(x1,y)
    if y1 < y:
        neighbors.append(x,y1)
    if x2 > x:
        neighbors.append(x2,y)
    if y2 > y:
        neighbors.append(x,y2)
    

loops = []

#print(tile_grid)
#print(start)

    