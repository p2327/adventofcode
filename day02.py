from typing import List, Tuple
from pathlib import Path
from collections import deque
from itertools import repeat

"""
Part 1: find boxes with similar ids

Tasks:
    - count the boxes that have exactly 2 repeated letters in their id
    - do the same for 3 repeats

Hint: multiple occurences of repeats count only once
Hint: if an id contains 2s and 3s repeats it counts  towards both totals
"""


data_folder = Path('/Users/pietro.pravettoni/developer/adventofcode/data/')


with open(data_folder / 'box_ids.txt') as f:
    ids = [line.strip() for line in f]


def two_and_threes(codes: List[str]) -> int:
    """
    Counts the letter repetition in a box id string (codes).
    Adds two and three repeats to a total count.
    Multiplies the total to find the boxes checksum
    """
    twos = 0
    threes = 0

    for code in codes:
        # set an hash table to keep count for each letter
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


"""
Part 2: identify the boxes that contain prototype fabric

Tasks:
    - Identify box ids which differs by just one letter
    - Return the common letters

Hint: only two boxes are the correct ones
"""

test_ids = [
    'abcde',
    'fghij',
    'klmno',
    'pqrst',
    'fguij',
    'axcye',
    'wvxyz'
]


def identify(ids: List[str]) -> Tuple[Tuple[str], str]:
    """
    Takes a list of box ids and return the position of 
    the two that differ by one letter
    """
    ids_queue = deque(ids)
    prototype_ids = ()
    current_id = []

    current_id = ids_queue.popleft()

    def match(box_id):
        nonlocal ids
        nonlocal prototype_ids
        nonlocal current_id
        nonlocal ids_queue
        # difference counter
        diff_count = 0

        # compare the current id versus all the boxes ids
        for id in ids:
            for c1, c2 in zip(box_id, id):
                if c1 != c2:
                    diff_count += 1
                else:
                    diff_count += 0

            if diff_count == 1:
                prototype_ids += (box_id, id)
                # the commented gives the right answer but changes
                # sequence order so the answer is not valid
                # equal_letters = ''.join(set(box_id).intersection(id))
                equal_letters = box_id.replace(list(set(box_id).difference(id))[0], '')
                return prototype_ids, equal_letters
            else:
                # onto then next
                pass
            # reset the counter for the next id
            diff_count = 0
        # process the next id if not succesful
        return match(ids_queue.popleft())

    return match(current_id)


print(identify(ids))
