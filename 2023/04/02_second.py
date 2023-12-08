import os
import pathlib

script_path = pathlib.Path(__file__).parent.resolve()

#input_file = open(os.path.join(script_path, 'sample.txt'))

filename = "_sample.txt"
filename = "_input.txt"
input_file = open(os.path.join(script_path, filename))

cards = {}

for line in input_file:
    title, numbers_string = line.strip().split(":")
    winning_numbers_string, numbers_we_have_string = numbers_string.strip().split("|")
    winning_numbers = winning_numbers_string.split()
    numbers = numbers_we_have_string.split()
    id = int(title[5:])
    card = { "winning_numbers": winning_numbers, "numbers": numbers, "times": 1 }
    cards[id] = card 

times = 0
id = 1
while cards:
    points = 0
    card = cards[id]
    if card["times"] > 0:
        times += 1
        for number in card["numbers"]:
            if number in card["winning_numbers"]:
                points += 1
        for point in range(1,min(points,len(cards))+1):
            cards[id+point]["times"] = cards[id+point]["times"] + 1
        cards[id]["times"] -= 1
    else:
        id += 1
    if id > max(cards.keys()):
        break

print("Times:", times)