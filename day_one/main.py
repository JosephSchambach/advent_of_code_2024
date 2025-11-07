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

def problem_one(list1, list2):
    s = 0
    for i in range(len(list1)):
        s += abs(list1[i] - list2[i])
    return s
    
with open('day_one/input.txt', 'r') as f:
    TEST_INPUT = f.read()
list1, list2 = parser(TEST_INPUT)
s = problem_one(list1, list2)
print(s)