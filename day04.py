import re
from datetime import datetime


'''
with open('/pythonprojects/adventofcode/data/fabric.txt') as f:
    log = [line.strip() for line in f]
'''

TEST_LOG = [
    '[1518-11-01 00:00] Guard #10 begins shift',
    '[1518-11-01 00:05] falls asleep',
    '[1518-11-01 00:25] wakes up',
    '[1518-11-01 00:30] falls asleep',
    '[1518-11-01 00:55] wakes up',
    '[1518-11-01 23:58] Guard #99 begins shift',
    '[1518-11-02 00:40] falls asleep',
    '[1518-11-02 00:50] wakes up',
    '[1518-11-03 00:05] Guard #10 begins shift',
    '[1518-11-03 00:24] falls asleep',
    '[1518-11-03 00:29] wakes up',
    '[1518-11-04 00:02] Guard #99 begins shift',
    '[1518-11-04 00:36] falls asleep',
    '[1518-11-04 00:46] wakes up',
    '[1518-11-05 00:03] Guard #99 begins shift',
    '[1518-11-05 00:45] falls asleep',
    '[1518-11-05 00:55] wakes up'
    ]

#print(', '.join(TEST_LOG[0].split()[0:2]))

test_string = ' '.join(TEST_LOG[0].split()[0:2]).strip('[]')
dt_string = datetime.strptime(test_string, '%Y-%m-%d %H:%M')

test_str_full = ' '.join(TEST_LOG[0].split()).strip('[]').replace(']', '')
#datetime_str = '09-19-1891 13:55'

#datetime_object = datetime.strptime(datetime_str, '%m-%d-%Y %H:%M')

#print(test_string[0])
#print(type(test_string))


#rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
rgx = "([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)"
rgx2 = "([0-9.\+]*)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+) ([a-zA-Z]+) #([0-9]+) ([a-zA-Z]+) ([a-zA-Z]+)"

print([x for x in re.match(rgx, test_string).groups()])
print([x for x in re.match(rgx2, test_str_full).groups()])


'''
Testing the sorting

Getting a tuple and sort by datetime item?

test_string = ' '.join(TEST_LOG[3].split()[0:2]).strip('[]')
dt_string = datetime.strptime(test_string, '%Y-%m-%d %H:%M')
test_string2 = ' '.join(TEST_LOG[6].split()[0:2]).strip('[]')
dt_string2 = datetime.strptime(test_string2, '%Y-%m-%d %H:%M')
test_string3 = ' '.join(TEST_LOG[0].split()[0:2]).strip('[]')
dt_string3 = datetime.strptime(test_string3, '%Y-%m-%d %H:%M')

test_str_full = ' '.join(TEST_LOG[0].split()).strip('[]').replace(']', '')
#datetime_str = '09-19-1891 13:55'

#datetime_object = datetime.strptime(datetime_str, '%m-%d-%Y %H:%M')

#print(test_string[0])
#print(type(test_string))


#rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
rgx = "([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)"
rgx2 = "([0-9.\+]*)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+) ([a-zA-Z]+) #([0-9]+) ([a-zA-Z]+) ([a-zA-Z]+)"

print([x for x in re.match(rgx, test_string).groups()])
print([x for x in re.match(rgx2, test_str_full).groups()])

sep_entry = [x for x in re.match(rgx2, test_str_full).groups()]

date_obj = dt_string, sep_entry[5:9]

dt_strings = [dt_string, dt_string2, dt_string3]
print(sorted(dt_strings))
print(dt_strings)
'''