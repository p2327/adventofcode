from typing import List, Iterator
from pathlib import Path
from collections import Counter
from itertools import repeat


data_folder = Path('/pythonprojects/adventofcode/data/')


with open(data_folder / 'box_ids.txt') as f:
    ids = [line.strip() for line in f]


def two_and_threes(codes: List[str]) -> int:
    twos = 0
    threes = 0
    
    for code in codes:
        zeros = list(repeat(0, len(code)))
        counts = dict(zip(code, zeros))
        
        for letter in code:
            if letter in counts.keys():
                counts[letter] += 1

        occurences = set(counts.values())
        
        for number in occurences:
            if number == 2:
                twos += 1
            elif number == 3:
                threes += 1
            else: 
                pass            
    
    return twos * threes


# part 1 answer
print(two_and_threes(ids))


def common_letters


def all_codes(codes: List[int], start: int = 0) -> Iterator[int]:
    """
    Generate all codes by adding the number in a cycle
    Start at 0
    """
    code = start

    while True:
        for code in codes:
            yield code
            # next execution resumes from this point
            frequency = next()
  

def match(s1, s2):
    assert len(s1) == len(s2), 'lenght must be equal'
    ok = False

    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if ok:
                return False
            else:
                ok = True

    return ok