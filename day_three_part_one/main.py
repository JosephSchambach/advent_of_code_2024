def memory_parser(TEST_INPUT, pattern):
    import re
    matches = re.findall(pattern, TEST_INPUT)
    return matches

def problem_three(matches):
    val = 0
    for match in matches:
        mul = int(match[0])*int(match[1])
        val += mul
    return val

with open('day_three_part_one/input.txt', 'r') as f:
    TEST_INPUT = f.read()
matches = memory_parser(TEST_INPUT, r'mul\((\d+),(\d+)\)')
mul = problem_three(matches)
print(mul)