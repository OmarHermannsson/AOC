import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

for line in input_file:
    if line.startswith('Time:'):
        times = ' '.join(line.strip().split(':')[1].strip().split()).replace(' ', '')
        times = int(times)
    elif line.startswith('Distance'):
        distances = ' '.join(line.strip().split(':')[1].strip().split()).replace(' ', '')
        distances = int(distances)

def get_wins(race_time, target_distance):
    wins = 0
    for hold_time in range(1, race_time):
        travel_time = race_time - hold_time        
        distance_travelled = hold_time * travel_time
        if distance_travelled > target_distance:
            wins += 1
    return wins



wins = get_wins(times, distances)
print("Wins:", wins)