from typing import NamedTuple, Iterator, Tuple, Dict, List
from collections import Counter
import re

"""
Day 03

Plan:
    - take claims and convert to rectangles
    - for each rectangle iterate over the square it has (from coords)
    - add one to the count and return all the counts (that overlaps more than 2)

"""

claim = '#123 @ 3,2: 5x4'
rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9+])"

Coord = Tuple[int, int]


class Rectangle(NamedTuple):
    id: int
    x_lo = int
    y_lo = int
    x_hi = int
    y_hi = int

    """
    When you need a utility function that doesn't access 
    any properties of a class but makes sense that it belongs 
    to the class, we use static functions.
    """

    @staticmethod
    def from_claim(claim: str) -> 'Rectangle':
        id, x_lo, y_lo, width, height = [int(x) for x in re.match(rgx, claim).groups()]
        return Rectangle(id, x_lo, y_lo, x_lo + width, y_lo + height)

    # gives all the coordinates
    def all_squares(self) -> Iterator[Coord]:
        for i in range(self.x_lo, self.x_hi):
            for j in range(self.y_lo, self.y_hi):
                yield(i, j)


assert Rectangle.from_claim(claim) == \
    Rectangle(123, 3, 2, 8, 6)


def coverage(rectangles: List[Rectangle]) -> Dict[Coord, int]:
    counts = Counter()
    for r in rectangles:
        for coord in r.all_squares():
            counts[coord] += 1

    return counts


# takes claims and convert them to rectangles
def multi_claimed(claims: List[str]) -> int:
    rectangles = [Rectangle.from_claim(claim) for claim in claims]
    counts = coverage(rectangles)

    return len([count for count in counts.values() if count >= 2])


# unit tests
TEST_CLAIMS = [
    "#1 @ 1,3: 4x4",
    "#2 @ 3,1: 4x4",
    "#3 @ 5,5: 2x2"
]


assert multi_claimed(TEST_CLAIMS == 4)


# solution
with open('../data/fabric.txt') as f:
    claims = [line.strip() for line in f]


print(multi_claimed(claims))
