import re

with open ('./day-two/day-two.txt') as f:
    lines = [l.strip() for l in f.readlines()]

pattern = r'Game \d+: '

lines = [re.sub(pattern, '', l) for l in lines]
lines = [l.split('; ') for l in lines]

cubes_dict = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def getPossible():
    result = 0

    for l in range(len(lines)):
        increment = l + 1

        for subset in lines[l]:
            cubes = subset.split(', ')
            for cube in cubes:
                [count, key] = cube.split(' ')

                if cubes_dict.get(key) < int(count):
                    print(key, count)
                    increment = 0

        result = result + increment
    
    return result


def getFewest():
    sums = []

    for l in range(len(lines)):
        fewest_dict = {
                'red': 0,
                'green': 0,
                'blue': 0,
            }
                    
        for subset in lines[l]:
            cubes = subset.split(', ')

            for cube in cubes:
                [count, key] = cube.split(' ')

                if fewest_dict.get(key) < int(count):
                    fewest_dict[key] = int(count)

        temp = 1
        for value in fewest_dict.values():
            temp = temp * int(value)
        
        sums.append(temp)

    result = 0
    for n in sums:
        result = result + n

    return result


first_result = getPossible()
second_result = getFewest()

print(first_result)
print(second_result)
