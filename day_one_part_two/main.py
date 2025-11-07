def parser(office_ids):
    split_data = office_ids.split('\n')
    list1 = []
    list2 = []
    for i in split_data:
        sub = i.split('   ')
        list1.append(int(sub[0]))
        list2.append(int(sub[1]))
    list1.sort()
    list2.sort()
    return list1, list2

def problem_two(list1, list2):
    d = {}
    for i in list2:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    s = 0
    for i in list1:
        val = d.get(i, 0)
        s += (i*val)
    return s

with open('day_tone_part_two/input.txt', 'r') as f:
    TEST_INPUT = f.read()
list1, list2 = parser(TEST_INPUT)
s = problem_two(list1, list2)
print(s)