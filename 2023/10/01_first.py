import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_sample2.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))


class Pipe:    
    def __init__(self, x, y, pipe_type):
        self.pipe_types = ['|','-','L','J','7','F','.','S']
        self.used = 0
        self.x = x
        self.y = y
        self.distance = 0
        if pipe_type in self.pipe_types:
            self.pipe_type = pipe_type
        else:
            raise ValueError(f"'{pipe_type}' is not a valid pipe type")
        
    def get_next_pipes(self):
        pipes = []
        x  = self.x
        y = self.y
        if self.pipe_type == '|':
            pipes.append((x,y-1))
            pipes.append((x,y+1))
        elif self.pipe_type == '-':
            pipes.append((x-1,y))
            pipes.append((x+1,y))
        elif self.pipe_type == 'L':
            pipes.append((x,y-1))
            pipes.append((x+1,y))
        elif self.pipe_type == 'J':
            pipes.append((x,y-1))
            pipes.append((x-1,y))
        elif self.pipe_type == '7':
            pipes.append((x-1,y))
            pipes.append((x,y+1))
        elif self.pipe_type == 'F':
            pipes.append((x+1,y))
            pipes.append((x,y+1))
        elif self.pipe_type == '.':
            pass
        elif self.pipe_type == 'S':
            pass
        return pipes
    
    def __str__(self):
        return self.pipe_type
    
    def __repr__(self):
        return self.pipe_type

start = None
tile_grid = []
for y, line in enumerate(input_file):
    grid_line = []
    for x, char in enumerate(line.strip()):
        p = Pipe(x,y,char)        
        if char == 'S':
            start = (x,y)
            #p.used = True
        grid_line.append(p)

    tile_grid.append(grid_line)
    

def get_neighbors(x,y):
    neighbors = []
    x1 = max(0, x-1)
    x2 = min(len(tile_grid[0]), x+1)
    y1 = max(0,y-1)
    y2 = min(len(tile_grid), y+1)

    if x1 < x:
        neighbors.append((x1,y))
    if y1 < y:
        neighbors.append((x,y1))
    if x2 > x:
        neighbors.append((x2,y))
    if y2 > y:
        neighbors.append((x,y2))
    return neighbors

def get_next(x,y):
    tile = tile_grid[y][x]
    for n in tile.get_next_pipes():
        nx, ny = n
        ntile = tile_grid[ny][nx]
        if ntile.used == 0:
            return ntile



loops = []
x, y = start
start_pipe = tile_grid[y][x]
neighbors = get_neighbors(x,y)


for n in neighbors:
    x,y = n
    tile = tile_grid[y][x]
    if tile.pipe_type == '.' or tile.pipe_type == 'S':
        continue
    nexts = tile.get_next_pipes()
    if nexts is not None and start in nexts:
        loops.append((tile))


print(loops)


for lx, loop in enumerate(loops):
    next = loop
    continue_loop = True
    start_pipe.used = 0
    next.used = lx + 1
    next.distance = distance = 1
    print (next, next.distance)
    while continue_loop:
        distance += 1
        nexts = next.get_next_pipes()
        for n in nexts:
            x, y = n
            p = tile_grid[y][x]            
            if p.pipe_type == 'S':
                if p.used > 0:
                    continue_loop = False
                    break
                p.used = 1
            elif p.used == lx:
                if p.distance == 0:
                    p.distance = distance
                else:
                    p.distance = min(p.distance, distance)
                p.used = lx+1
                print(p, p.distance)
                next = p
            #tile_grid[y][x] = p

max_pipe = 0
for line in tile_grid:
    for col in line:
        max_pipe = max(max_pipe, col.distance)

print("Answer:", max_pipe)
#print(tile_grid)
#print(start)

    