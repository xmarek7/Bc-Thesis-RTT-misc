import json
from typing import Optional
from utilities import concacenate_test_ids


BYTES_PER_PSAMPLE = {  0:   153600,    1: 4000020,     2: 5120000,     3: 2400000,
                       4:   1048583,   8: 256004,      9: 5120000,    10: 96000,
                      11:  64000,     12: 48000,      13: 9228911,    15: 400000,
                      16:  5407134,   17: 80000000,  100: 400000,    101: 400000,
                     102: 400000,    204: 40000,     205: 614400000, 206: 51200000,
                     207: 452168105, 208: 116933538, 209: 260000000}


NTUPLES = {200: (1, 12), 201: (2, 5), 202: (2,5), 203: (0,32)}


def get_bytes_per_psample(test_id: int, ntup: Optional[int]) -> Optional[int]:
    if test_id == 200 and 1 <= ntup <= 12:
        return ntup * 800000 + 4
    elif test_id == 201 and 2 <= ntup <= 5:
        return ntup * 40000
    elif test_id == 202 and 2 <= ntup <= 5:
        return ntup * 400000
    elif test_id == 203 and 0 <= ntup <= 32:
        return (ntup + 1) * 4000000
    elif ntup is None:
        return BYTES_PER_PSAMPLE[test_id]
    raise ValueError("Invalid test id or combination of test id and ntuples")


def calculate_psamples(test_id: int, ntup: Optional[int], file_size: int) -> int:
    if test_id == 0:
        return (file_size - 24) // get_bytes_per_psample(test_id, ntup)
    return file_size // get_bytes_per_psample(test_id, ntup)


def dieharder_variant(test_id: int, ntup: int, file_size: int):
    result = {}
    psamples = calculate_psamples(test_id, ntup, file_size)
    if psamples == 0:
        return None
    result["psamples"] = psamples
    result["arguments"] = "-n {}".format(ntup)
    if test_id == 201:
        result["arguments"] += " -t 10000"
    return result

def dieharder_test(file_size: int):
    test_ids = []
    result = {"defaults": {"psamples": 100}, "test-specific-settings": []}
    for test_id in [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 15, 16, 17, 100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209]:
        test = {"test-id": test_id}
        if test_id in {200, 201, 202, 203}:
            test["variants"] = []
            ntup_min, ntup_max = NTUPLES[test_id]
            for ntup in range(ntup_min, ntup_max):
                variant = dieharder_variant(test_id, ntup, file_size)
                if variant is not None:
                    test["variants"].append(variant)
        else:
            psamples = calculate_psamples(test_id, None, file_size)
            if psamples > 0:
                test["psamples"] = psamples

        if test_id in {13, 16, 207, 208}:
            test["comment"] = "WARNING - Test with irregular read bytes."

        if (test.get("psamples", None) is not None and test["psamples"] > 0) or len(test.get("variants", [])) > 0:
            result["test-specific-settings"].append(test)
            test_ids.append(test_id)
    result["defaults"]["test-ids"] = concacenate_test_ids(test_ids)
    return result


