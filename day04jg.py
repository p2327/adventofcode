from collections import Counter
from typing import NamedTuple, Tuple, List
import re

# Find guard with most minutes asleep
# Compute (ID of guard) * (most asleep minute)


TEST_LOG = """[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up""".split("\n")


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


rgx = r"\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] (.*)"

guard_id_rgx = r"Guard #([0-9]+) begins shift"


def find_naps(entries: List[str]) -> List[Nap]:
    naps: List[Nap] = []

    entries = sorted(entries)

    guard_id = sleep = wake = None

    # extract information from each log entry
    for entry in entries:
        year, month, day, hour, minute, comment = re.match(rgx, entry).groups()
        ts = Timestamp(int(year),
                       int(month),
                       int(day),
                       int(hour),
                       int(minute))

        guard = re.match(guard_id_rgx, comment)
        
        # if the id is in the comment (found by regex)
        if guard:
            assert sleep is None and wake is None
            guard_id = int(guard.groups()[0])
        # else save the asleep and wake minutes
        elif "falls asleep" in comment:
            assert guard_id is not None and sleep is None and wake is None
            sleep = int(minute)
        elif "wakes up" in comment:
            assert guard_id is not None and sleep is not None and wake is None
            wake = int(minute)
            naps.append(Nap(guard_id, sleep, wake))
            sleep = wake = None

    return naps
        

print(find_naps(TEST_LOG))