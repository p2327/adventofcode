#import pandas as pd
from typing import List, Iterator
from pathlib import Path

data_folder = Path('/Users/pietro.pravettoni/developer/adventofcode/data/')

'''
with open(data_folder / 'frequencies.txt') as raw_data:
    frequencies = []
    lines = raw_data.read().splitlines()
    for i in lines:
        frequencies.append(int(i))
'''

with open(data_folder / 'frequencies.txt') as f:
    frequencies = [int(line.strip()) for line in f]

#print(sum(frequencies))

'''
def calibrate_device(f: list, first=0, last=1) -> int:
    #first = 0
    #last = 1
    partial_sum = f[first] + f[last]
    next_partial = partial_sum + f[last+1]

    while last < len(f):
        if partial_sum == next_partial:
            print(partial_sum)
            return partial_sum
        else:
            return calibrate_device(f, first+1, last+1) 
'''

def all_frequencies(numbers: List[int], start: int = 0) -> Iterator[int]:
    """
    Generate all frequencies by adding the number in a cycle
    Start at 0
    """
    frequency = start

    while True:
        for number in numbers:
            yield frequency
            # next execution resumes from this point
            frequency += number

def first_repeat_frequency(numbers: List[int], start: int = 0) -> int:
    seen = set()
    
    for frequency in all_frequencies(numbers, start):
        if frequency in seen:
            return frequency
        else:
            seen.add(frequency)

'''
tests = [
    [+1, -1],
    [+3, +3, +4, -2, -4 ],
    [-6, +3, +8, +5, -6 ],
    [+7, +7, -2, -7, -4]
]
'''

# test against the examples
assert first_repeat_frequency([1, -1]) == 0
assert first_repeat_frequency([+3, +3, +4, -2, -4 ]) == 10
assert first_repeat_frequency([-6, +3, +8, +5, -6 ]) == 5
assert first_repeat_frequency([+7, +7, -2, -7, -4]) == 14


print(first_repeat_frequency(frequencies))


