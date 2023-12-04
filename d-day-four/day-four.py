import re

with open ('./d-day-four/day-four.txt') as f:
    lines = [l.strip() for l in f.readlines()]

pattern = r'Card \d+: '

lines = [re.sub(pattern, '', l) for l in lines]

print(lines)

def getPoints():
    result = 0

    dict = {key: 1 for key in range(len(lines))}

    for i in range(len(lines)):
        [winning, mine] = lines[i].split(' | ')
        mine = set(mine.split(' '))
        
        temp = 0
        count = 0
        for n in winning.split(' '):
            if n and n in mine:
                temp = 1 if temp == 0 else temp * 2
                count += 1
        result += temp

        for j in range(i + 1, i + count + 1):
            dict[j] = dict[j] + dict[i]
    
    print('Result 1: ', result)    
    print('Result 2: ', sum(dict.values()))



getPoints()