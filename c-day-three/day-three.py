with open ('./c-day-three/day-three.txt') as f:
    lines = [l.strip() for l in f.readlines()]

dummy = '.' * len(lines[0])
lines.append(dummy)
lines.insert(0, dummy)

# [{ index, line }]
def getLookup():
    lookup = []

    for i in range(1, len(lines) - 1):
        temp = {}
        for j in range(i - 1, i + 2):
            for k in range(len(lines[j])):
                current = lines[j][k]
                if not current.isnumeric() and current != '.':
                    temp[k] = j
        lookup.append(temp)
    
    return lookup

def getAdjacentSum():
    lookup = getLookup()
    result = 0

    for i in range(1, len(lines) - 1):
        j = 0
        num = ''
        indexes = []

        while (j < len(lines[i])):
            current = lines[i][j]

            if current.isnumeric():
                num += current
                indexes.append(j)
                    
            if not current.isnumeric() or j == len(lines[i]) - 1:
                if num != '' and len(indexes) > 0:
                    valid_indexes = [indexes[0] - 1, *indexes, indexes[-1] + 1]

                    for indx in valid_indexes:
                        if indx in lookup[i - 1].keys():
                            result += int(num)
                            break
            
                num = ''
                indexes = []
            
            j += 1
    
    return result

def getGearSum():
    global lines
    lines = [''.join('.' if not (c.isnumeric() or c == '*' or c == '.') else c for c in s) for s in lines]
    lookup = getLookup()

    # { line: { index: [num, num] }}
    dict = {}
    for i in range(1, len(lines) - 1):
        j = 0
        num = ''
        indexes = []

        while (j < len(lines[i])):
            current = lines[i][j]

            if current.isnumeric():
                num += current
                indexes.append(j)
                    
            if not current.isnumeric() or j == len(lines[i]) - 1:
                if num != '' and len(indexes) > 0:
                    valid_indexes = [indexes[0] - 1, *indexes, indexes[-1] + 1]

                    for indx in valid_indexes:
                        if indx in lookup[i - 1].keys():
                            line = lookup[i - 1].get(indx)

                            if line in dict:
                                if indx in dict[line]:
                                    dict[line][indx].append(int(num))
                                else:
                                    dict[line][indx] = [int(num)]
                            else:
                                dict[line] = { indx: [int(num)] }
            
                num = ''
                indexes = []

            j += 1

    result = 0
    for d in dict.values():
        for list in d.values():
            if len(list) > 1:
                result = result + (list[0] * list[-1])

    return result 
    


print('Solution 1: ', getAdjacentSum())
print('Solution 2: ', getGearSum())

