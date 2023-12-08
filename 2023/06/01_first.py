import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

for line in input_file:
    if line.startswith('Time:'):
        times = line.strip().split(':')[1].strip().split()
        times = list(map(str.strip,times))
        times = list(map(int,times))
    elif line.startswith('Distance'):
        distances = line.strip().split(':')[1].strip().split()
        distances = list(map(str.strip,distances))
        distances = list(map(int,distances))

def get_wins(race_time, target_distance):
    wins = 0
    for hold_time in range(1, race_time):
        travel_time = race_time - hold_time        
        distance_travelled = hold_time * travel_time
        if distance_travelled > target_distance:
            wins += 1
    return wins

sum = None
for x in range(len(times)):
    wins = get_wins(times[x], distances[x])
    print("Wins:", wins)
    if sum is not None:
        sum *= wins
    else:
        sum = wins

print("Ans:", sum)