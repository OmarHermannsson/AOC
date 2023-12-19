import os
import itertools

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

galaxy_map = []
for line in input_file:
    galaxy_line = []
    for col in line.strip():
        galaxy_line.append(col)
        #print(col, end='')
    galaxy_map.append(galaxy_line)
    #print("")
        
expanded_galaxy_map = []

# Find columns and rows that have no galaxies
no_gal_row = []
no_gal_col = []

for y, line in enumerate(galaxy_map):
    has_galaxy = False
    for x, char in enumerate(line):
        if char == '#':
            has_galaxy = True
    if not has_galaxy:
        no_gal_row.append(y)

for x in range(len(galaxy_map[0])):
    has_galaxy = False
    for y in range(len(galaxy_map)):
        if galaxy_map[y][x] == '#':
            has_galaxy = True
    if not has_galaxy:
        no_gal_col.append(x)

for y, line in enumerate(galaxy_map):
    galaxy_line = []
    for x, char in enumerate(line):
        galaxy_line.append(char)
        if x in no_gal_col:
            pass
            #for _ in range(1000000):
                #galaxy_line.append(char)
    expanded_galaxy_map.append(galaxy_line)
    if y in no_gal_row:
        pass
        #for _ in range(1000000):
            #expanded_galaxy_map.append(galaxy_line)

galaxies = []

for y, line in enumerate(expanded_galaxy_map):
    for x, char in enumerate(line):
        if char == "#":
            galaxies.append((x,y))

print("No_gal_row:", no_gal_row)
print("No_gal_col:", no_gal_col)
#print("Galaxies:", galaxies)

exp_galaxies = []
for g in galaxies:
    gx, gy = g
    nx = gx
    ny = gy
    for xp in no_gal_col:
        if gx >= xp:
            nx += 999999
    for yp in no_gal_row:
        if gy >= yp:
            ny += 999999
    exp_galaxies.append((nx,ny))

def get_distance(x,y):
    sum = 0
    sum += abs(x[0] - y[0])
    sum += abs(x[1] - y[1])
    return sum

sum = 0
galaxy_pairs = []
for n1 in range(len(exp_galaxies)):
    for n2 in exp_galaxies[n1+1:]:
        xg = exp_galaxies[n1]
        yg = n2
        dist = get_distance(xg, yg)
        sum += dist
        galaxy_pairs.append((xg, yg))
        #print(f"{xg},{yg} - {dist}")

print("Sum:", sum)

        