from typing import NamedTuple, Iterator, Tuple, List, Dict
import re
from collections import Counter

rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"

Coord = Tuple[int, int]

class Rectangle(NamedTuple):
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

    @staticmethod
    def from_claim(claim: str) -> 'Rectangle':
        id, x_lo, y_lo, width, height = [int(x) for x in re.match(rgx, claim).groups()]
        return Rectangle(id, x_lo, y_lo, x_lo + width, y_lo + height)

    
    def all_squares(self) -> Iterator[Coord]:
        """ 
        Iterte through all the points of a Rectangle (squares)
        """
        for i in range(self.x_lo, self.x_hi):
            for j in range(self.y_lo, self.y_hi):
                yield (i, j)


assert Rectangle.from_claim("#123 @ 3,2: 5x4") == \
    Rectangle(123, 3, 2, 8, 6)

def coverage(rectangles: List[Rectangle]) -> Dict[Coord, int]:
    """
    Counts all the points (squares) in a Rectangle object.
    """
    counts = Counter()
    for rectangle in rectangles:
        for coord in rectangle.all_squares():
            counts[coord] += 1

    return counts


def multi_claimed(claims: List[str]) -> int:
    """
    Generates rectangle instances from a claim, counts the the squares
    as discrete points (using coordinates). If the same square (coordinate)
    appears more than 2 times is added to a list comprehension of all the
    overlapping squares.
    Returns how many square points are overlapping, i.e. they exist in
    more than 2 claims.
    """
    rectangles = [Rectangle.from_claim(claim) for claim in claims]
    counts = coverage(rectangles)

    return len([count for count in counts.values() if count >= 2])


TEST_CLAIMS = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2"]
assert multi_claimed(TEST_CLAIMS) == 4


# solution
with open('C:/Python/projects/adventofcode/data/fabric.txt') as f:
    claims = [line.strip() for line in f]

print(claims)

#print(multi_claimed(claims))


def non_overlapping_claim(claims: List[str]) -> int:
    rectangles = [Rectangle.from_claim(claim) for claim in claims]
    counts = coverage(rectangles)

    # find the rectangle that counts is exactly 1
    # so all of its points (coordS) don't overlap with any other
    # that is ot say counts == 1 is true for al squares (coords) in 
    # the rectangle
    non_overlapping = [
        rectangle for rectangle in rectangles
        if all(counts[coord] == 1 for coord in rectangle.all_squares())
        ]


    assert len(non_overlapping) == 1

    return non_overlapping[0].id


assert non_overlapping_claim(TEST_CLAIMS) == 3


#print(non_overlapping_claim(claims))




