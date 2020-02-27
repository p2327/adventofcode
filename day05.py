from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0

    while count < len(polymer):
        for pair in pairs(polymer):
            if same_type(pair[0], pair[1]) and pair[0] != pair[1]:
                to_delete.add(pair[2], pair[2]+1)
            else:
                count += 1

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce(TEST) == "dabCBAcaDA"







'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            to_delete.add(pair[2]+1)
                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''


'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            to_delete.add(pair[2]+1)
                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''

'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            for pair in pairs(reduced):
                if same_type(pair[0], pair[1]) and pair[0] != pair[1]:
                    return alchreduce(reduced)
                else:
                    return reduced

            
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            to_delete.add(pair[2]+1)
                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''


'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            
            if any([same_type(pair[0], pair[1]) and pair[0] != pair[1] for pair in pairs(reduced)]):
                return alchreduce(reduced)
            else:
                return reduced
    
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            to_delete.add(pair[2]+1)
                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''



'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            
            if any([same_type(pair[0], pair[1]) and pair[0] != pair[1] for pair in pairs(reduced)]):
                return alchreduce(reduced)
            else:
                return reduced
    
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            # check for identycal triplets
            if same_type(polymer[pair[2]], polymer[pair[2]+2]):
                pass
            else:
                to_delete.add(pair[2]+1)
                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''


'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            
            if any([same_type(pair[0], pair[1]) and pair[0] != pair[1] for pair in pairs(reduced)]):
                return alchreduce(reduced)
            else:
                return reduced
    
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            # check for identycal triplets
            if same_type(polymer[pair[2]], polymer[pair[2]+1]) or same_type(polymer[pair[2]], polymer[pair[2]+2]):
                pass
            else:
                to_delete.add(pair[2]+1)
                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''


'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            
            if any([same_type(pair[0], pair[1]) and pair[0] != pair[1] for pair in pairs(reduced)]):
                return alchreduce(reduced)
            else:
                return reduced
    
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            if same_type(polymer[pair[2]], polymer[pair[2]+1]):
                to_delete.add(pair[2]+1)
            else:
                pass                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''
'''
from typing import Tuple


TEST = 'dabAcCaCBAcCcaDA'


def pairs(polymer: str) -> Tuple[str, str]:
    """ Generates all adjacent character pairs"""
    it = iter(polymer)
    prev = next(it)

    for index, char in enumerate(it):
        yield (prev, char, index)
        prev = char


def same_type(s1: str, s2: str) -> bool:
    """A and a are the same type"""
    return s1.lower() == s2.lower()


def alchreduce(polymer: str) -> str:
    to_delete = set()
    monomers = list(polymer)
    count = 0
    

    for pair in pairs(polymer):
        count += 1
            
        if count >= len(polymer) - 1:
            reduced = ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)
            
            if any([same_type(pair[0], pair[1]) and pair[0] != pair[1] for pair in pairs(reduced)]):
                return alchreduce(reduced)
            else:
                return reduced
    
        elif same_type(pair[0], pair[1]) and pair[0] != pair[1]:
            to_delete.add(pair[2])
            if same_type(polymer[pair[2]], polymer[pair[2]+1]):
                to_delete.add(pair[2]+1)
            else:
                pass                
        else:
            pass

    return ''.join(unit for i, unit in enumerate(monomers) if i not in to_delete)


assert alchreduce("abAB") == "abAB"
assert alchreduce("dabAcCaCBAcCcaDA") == "dabCBAcaDA"
'''