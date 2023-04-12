from typing import List


def concacenate_test_ids(test_ids: List[int]) -> List[str]:
    concat = []
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


######################################################################
# Unsed things
######################################################################


def concacenate_test_ids_unused(test_ids: List[int]) -> str:
    concat = []
    first = test_ids[0]
    last = test_ids[0]
    for test_id in test_ids[1:]:
        if (test_id != last + 1):
            if first != last:
                concat.append("\"{}-{}\"".format(first, last))
            else:
                concat.append("\"{}\"".format(last))
            first = test_id
        last = test_id
    if first != last:
                concat.append("\"{}-{}\"".format(first, last))
    else:
        concat.append("\"{}\"".format(last))
    return "[" + ",".join(concat) + "]"



def make_line_unused(content: str, offset: int) -> str:
    return (offset * 4 * " " ) + content + "\n"


