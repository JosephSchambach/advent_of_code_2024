def parser(input_str):
    raw = input_str.split('\n')
    lines = []
    for row in raw:
        line = []
        line_vals = row.split(' ')
        for i in line_vals:
            line.append(int(i))
        lines.append(line)
    return lines

def descending(line):
    for i in range(1,len(line)):
        diff = line[i-1] - line[i]
        if diff > 3:
            return 0
        elif diff < 1:
            return 0
    return 1

def ascending(line):
    for i in range(1,len(line)):
        diff = line[i] - line[i-1]
        if diff > 3:
            return 0
        elif diff < 1:
            return 0 
    return 1

def processor(line):
    if line[0] < line[1]:
        val = ascending(line)
    else:
        val = descending(line)
    return val 

with open('day_two/input.txt', 'r') as f:
    TEST_INPUT = f.read()
lines = parser(TEST_INPUT)
s = 0
for line in lines:
    s += processor(line)
print(s)