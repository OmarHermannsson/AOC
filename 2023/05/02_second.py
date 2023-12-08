import sys
import os

script_path = os.path.dirname(os.path.abspath(__file__))

filename = '_sample.txt'
filename = '_input.txt'

input_file = open(os.path.join(script_path, filename))

class maprange:
    def __init__(self, destination, source, len):
        self.destination = int(destination)
        self.source = int(source)
        self.len = int(len)
        self.end = self.source + self.len

    def isInRange(self, value):
        value = int(value)
        if value >= self.source and value < self.end:
            return True
        else:
            return False
        
    def getDestination(self, src):
        src = int(src)
        offset = src - self.source
        return self.destination + offset
        
class mapranges:
    def __init__(self, name):
        self.name = name
        self.ranges = []

    def addRange(self, mrange):
        self.ranges.append(mrange)

    def getDestination(self, src):
        for mrange in self.ranges:
            if mrange.isInRange(src):
                return mrange.getDestination(src)
        return src


all_mappranges = {}
for line in input_file:
    if line.startswith('seeds:'):
        seeds = line.split(':')[1].strip().split()
    elif line.startswith('seed-to-soil'):
        current_maprange = 'seed-to-soil'
        all_mappranges[current_maprange] = mapranges(current_maprange)
    elif line.startswith('soil-to-fertilizer'):
        current_maprange = 'soil-to-fertilizer'
        all_mappranges[current_maprange] = mapranges(current_maprange)
    elif line.startswith('fertilizer-to-water'):
        current_maprange = 'fertilizer-to-water'
        all_mappranges[current_maprange] = mapranges(current_maprange)
    elif line.startswith('water-to-light'):
        current_maprange = 'water-to-light'
        all_mappranges[current_maprange] = mapranges(current_maprange)
    elif line.startswith('light-to-temperature'):
        current_maprange = 'light-to-temperature'
        all_mappranges[current_maprange] = mapranges(current_maprange)
    elif line.startswith('temperature-to-humidity'):
        current_maprange = 'temperature-to-humidity'
        all_mappranges[current_maprange] = mapranges(current_maprange)
    elif line.startswith('humidity-to-location'):
        current_maprange = 'humidity-to-location'
        all_mappranges[current_maprange] = mapranges(current_maprange)
    elif line == "\n":
        pass
    else:
        try:
            dst,src,mlen = line.split()
        except:
            print("ERROR:", line)
        new_range = maprange(dst,src,mlen)
        all_mappranges[current_maprange].addRange(new_range)

lowest_location = None
for range in all_mappranges['humidity-to-location'].ranges:
    if lowest_location is None:
        lowest_location = range
    else:
        lowest_location = min(lowest_location.destination, range.destination)

print (lowest_location)
    


sys.exit()


lowest = None
for seed in range(0,len(seeds),2):
    
    seed_min = int(seeds[seed])
    seed_max = int(seeds[seed])+int(seeds[seed+1])

    seedv = seed_min
    while seedv <= seed_max:
        soil = all_mappranges['seed-to-soil'].getDestination(seedv)
        fertilizer = all_mappranges['soil-to-fertilizer'].getDestination(soil)
        water = all_mappranges['fertilizer-to-water'].getDestination(fertilizer)
        light = all_mappranges['water-to-light'].getDestination(water)
        temperature = all_mappranges['light-to-temperature'].getDestination(light)
        humidity = all_mappranges['temperature-to-humidity'].getDestination(temperature)
        location = all_mappranges['humidity-to-location'].getDestination(humidity)
        if lowest is not None:
            lowest = min(lowest, location)
        else:
            lowest = location
        seedv += 1

    #print (seed, soil, fertilizer, water, light, temperature, humidity, location)

print("Lowest:", lowest)