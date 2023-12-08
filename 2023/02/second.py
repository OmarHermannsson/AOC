import os
import pathlib

script_path = pathlib.Path(__file__).parent.resolve()

#input_file = open(os.path.join(script_path, 'sample.txt'))
input_file = open(os.path.join(script_path, 'input.txt'))

def get_colors(game_set):
    """ Returns the color values within the given game set (red,green,blue)
    input is in the form of one to three sets of <int> <color> seperated by a comma """
    red = 0
    green = 0
    blue = 0
    colors = game_set.split(',')
    for color in colors:
        try:
            amount, label = color.split()
        except ValueError:
            print ("ERR:", color)
        amount_int = int(amount)
        if label == "red": red += amount_int
        if label == "green": green += amount_int
        if label == "blue": blue += amount_int
    return (red,green,blue)

sum = 0 # holds the sum of the game ids that are possible
limits = (12,13,14) # the limits for the color values we use to determine if the game results were actually possible

for line in input_file:
    i, g = line.strip().split(":")
    id = int(i[5:])
    rmax = gmax = bmax = 0
    for game_set in g.strip().split(";"):
        colors = get_colors(game_set.strip())
        if colors[0] > rmax: rmax = colors[0]
        if colors[1] > gmax: gmax = colors[1]
        if colors[2] > bmax: bmax = colors[2]
    power = rmax * gmax * bmax
    sum += power

print ("Sum:", sum)