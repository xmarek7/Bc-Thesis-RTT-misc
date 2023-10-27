from typing import List, Optional
from re import compile, fullmatch

KILO = 1024
MEGA = KILO ** 2
GIGA = KILO ** 3
TERA = KILO ** 4

def parse_size(input: str) -> Optional[int]:
    if input.isnumeric():
        return int(input)
    regex = compile("^[0-9]+[kKmMgGtT]$")
    if regex.fullmatch(input) is None:
        return None

    unit = input[-1]
    if unit in "kK":
        power = KILO
    elif unit in "mM":
        power = MEGA
    elif unit in "gG":
        power = GIGA
    else:
        power = TERA
    return int(input[:-1]) * power
    

def concacenate_test_ids(test_ids: List[int]) -> List[str]:
    concat = []
    if len(test_ids) == 0:
         return []
    first = test_ids[0]
    last = test_ids[0]
    for test_id in test_ids[1:]:
        if (test_id != last + 1):
            if first != last:
                concat.append("{}-{}".format(first, last))
            else:
                concat.append("{}".format(last))
            first = test_id
        last = test_id

    if first != last:
                concat.append("{}-{}".format(first, last))
    else:
        concat.append("{}".format(last))
    return concat