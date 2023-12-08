import os
import pathlib

script_path = pathlib.Path(__file__).parent.resolve()

#input_file = open(os.path.join(script_path, 'sample.txt'))

filename = "_sample.txt"
filename = "_input.txt"
input_file = open(os.path.join(script_path, filename))

cards = []

sum = 0
for card in input_file:
    title, numbers_string = card.strip().split(":")
    winning_numbers_string, numbers_we_have_string = numbers_string.strip().split("|")
    winning_numbers = winning_numbers_string.split()
    numbers = numbers_we_have_string.split()
    points = 0
    for number in numbers:
        if number in winning_numbers:
            if points == 0:
                points = 1
            else:
                points *= 2
    sum += points
    #print (title, points)

print ("Sum:", sum)
