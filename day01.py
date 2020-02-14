from typing import List, Iterator
from pathlib import Path

data_folder = Path('/Users/pietro.pravettoni/developer/adventofcode/data/')


with open(data_folder / 'frequencies.txt') as f:
    frequencies = [int(line.strip()) for line in f]

# solution 1
print(sum(frequencies))


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


# test against the examples
assert first_repeat_frequency([1, -1]) == 0
assert first_repeat_frequency([+3, +3, +4, -2, -4]) == 10
assert first_repeat_frequency([-6, +3, +8, +5, -6]) == 5
assert first_repeat_frequency([+7, +7, -2, -7, -4]) == 14


# solution 2
print(first_repeat_frequency(frequencies))
