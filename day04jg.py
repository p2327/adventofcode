from typing import NamedTuple, Tuple




# Find guard with most minutes asleep
# Compute (ID of guard) * (most asleep minute)

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


class Timestamp(NamedTuple):
    year: int
    month: int
    day: int
    hour: int
    minute: int


class Nap(NamedTuple):
    guard_id: int
    # minute guard falls asleep
    sleep: int 
    # minute guard wakes up
    wake: int


rgx = r"[([0-9]{4}"

def find_naps(entries: List[str]) -> List[Nap]:
    entries = sorted(entries)



def parse_line(line: str) -> Tuple:
