with open ('day-one.txt') as f:
    lines = [l.strip() for l in f.readlines()]

def getNums():
    result = 0 

    for line in lines:
        num = 0; left = 0; right = len(line) - 1

        while (left <= right):
            if (line[left].isnumeric()):
                num = line[left]
                break
            left = left + 1

        while(right >= left):
            if (line[right].isnumeric()):
                num = num + line[right]
                break
            right = right - 1

        result = result + int(num)

    return result

def modifyLines():
    global lines

    string_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(lines)):
        for n in string_nums:
            if n in lines[i]:
                lines[i] = lines[i].replace(n, n[0] + str(string_nums.index(n) + 1) + n[-1])


first_result = getNums()

modifyLines()
second_result = getNums()

print(first_result, second_result)