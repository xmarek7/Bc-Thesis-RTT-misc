from typing import List


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