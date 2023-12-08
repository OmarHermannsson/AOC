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

def is_possible(limits, colors):
    """ returns false if any color value is beyond the given limit, otherwise returns true"""
    possible = True
    if colors[0] > limits[0] or colors[1] > limits[1] or colors[2] > limits[2]: possible = False
    return possible
    

sum = 0 # holds the sum of the game ids that are possible
limits = (12,13,14) # the limits for the color values we use to determine if the game results were actually possible

for line in input_file:
    i, g = line.strip().split(":")
    id = int(i[5:])
    possible = True
    for game_set in g.strip().split(";"):
        colors = get_colors(game_set.strip())
        if not is_possible(limits, colors):
            possible = False
    if possible:
        sum += id

print ("Sum:", sum)