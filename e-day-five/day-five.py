import re

with open ('./e-day-five/day-five.txt') as f:
    lines = [l.strip() for l in f.readlines()]

# seed => soil => fertilizer => water => light => temp => humidity => location

seeds = [int(l) for l in lines[0].split(': ')[-1].split(' ') if l]

maps: list[list[str]] = []
temp = []

for i in range(1, len(lines)):
    line = lines[i]

    if not line:
        continue

    if line.endswith(' map:'):
        if len(temp) > 0:
            maps.append(temp)
            temp = []
    else:
        parsed_line = [int(l) for l in line.split(' ') if l]
        temp.append(parsed_line)

        if i + 1 == len(lines):
            maps.append(temp)



def getPairs(chunk: list[list[str]], source: list[str]):
    dict = {}
    for line in chunk:
        destination_start = line[0]
        source_start = line[1]
        values_range = line[-1]
        
        for value in source:
           source_difference = value - source_start
           source_in_range = source_difference <= values_range

           target_destination = destination_start + source_difference
           target_in_range = target_destination <= target_destination + values_range

           if source_difference > 0 and source_in_range:
               if target_in_range:
                   dict[value] = target_destination
                   continue
           else:
               dict[value] = dict[value] if value in dict else value 
             
    return dict

def getResult():
    source = seeds
    for map in maps:
        temp = getPairs(map, source)
        source = [l for l in temp.values()]
    
    return min(source)

print(getResult())






