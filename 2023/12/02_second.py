import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

cached = {}

def get_count(rec, par):        
    if rec == "":
        return 1 if par == () else 0
    
    if par == ():
        return 0 if "#" in rec else 1
    
    key = (rec,par)

    if key in cached:
        return cached[key]
    
    count = 0

    if rec[0] in ".?":
        count += get_count(rec[1:], par)

    if rec[0] in "#?":
        if par[0] <= len(rec) and "." not in rec[:par[0]] and (par[0] == len(rec) or rec[par[0]] != "#"):
            count += get_count(rec[par[0] + 1:], par[1:])
    
    cached[key] = count
    return count

sum = 0
for line in input_file:
    rec, par = line.strip().split()
    par = tuple(map(int, par.split(",")))
    frec = ((rec + '?')*5)[:-1]
    fpar = par * 5
    num = get_count(frec, fpar)
    sum += num

print ("Num:", sum)
