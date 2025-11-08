def memory_parser(records, pattern):
    import re
    matches = []
    for record in records:
        matched = re.findall(pattern, record)
        for i in matched:
            i_1 = int(i[0])
            i_2 = int(i[1])
            matches.extend([i_1, i_2])
    return matches

def problem_three(matches):
    val = 0
    for i in range(0, len(matches),2):
        one = matches[i]
        two = matches[i+1]
        mul = one*two
        val += mul
    return val

def splitter(input_str, val_to_split, val_to_remove):
    data = input_str.split(val_to_split)
    records = []
    for record in data:
        splits = record.split(val_to_remove)
        records.append(splits[0])
    return records

with open('day_three_part_two/input.txt', 'r') as f:
    TEST_INPUT = f.read()
records = splitter(TEST_INPUT, 'do()', "don't()")
matches = memory_parser(records, r'mul\((\d+),(\d+)\)')
val = problem_three(matches)
print(val)