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

TEST_IDS = [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 15, 16, 17, 100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209]

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


def dieharder_variant(test_id: int, ntup: int, file_size: int, psample_offset: bool):
    psamples = calculate_psamples(test_id, ntup, file_size) + (1 if psample_offset else 0)
    if psamples == 0:
        return None
    result = {}
    result["psamples"] = psamples 
    result["arguments"] = "-n {}".format(ntup)
    if test_id == 201:
        result["arguments"] += " -t 10000"
    return result


def dieharder_test(file_size: int, psample_offset: bool):
    test_ids = []
    result = {"defaults": {"psamples": 100}, "test-specific-settings": []}
    omitted_tests = []
    for test_id in TEST_IDS:
        test = {"test-id": test_id}
        if test_id in {200, 201, 202, 203}:
            test["variants"] = []
            omitted_variants = []
            ntup_min, ntup_max = NTUPLES[test_id]
            for ntup in range(ntup_min, ntup_max + 1):
                variant = dieharder_variant(test_id, ntup, file_size, psample_offset)
                if variant is None:
                    if test.get("omitted-variants") is None:
                        test["omitted-variants"] = [ntup]
                    else:
                        test["omitted-variants"].append(ntup)
                else:
                    test["variants"].append(variant)
        else:
            psamples = calculate_psamples(test_id, None, file_size) + (1 if psample_offset else 0)
            if psamples > 0:
                test["psamples"] = psamples
            else:
                omitted_tests.append(test_id)

        if test_id in {13, 16, 207, 208}:
            test["comment"] = "WARNING - Test with irregular read bytes."

        if (test.get("psamples", None) is not None and test["psamples"] > 0) or len(test.get("variants", [])) > 0:
            result["test-specific-settings"].append(test)
            test_ids.append(test_id)
        
    # No test set for execution
    if len(omitted_tests) > 0:
        result["omitted-tests"] = concacenate_test_ids(omitted_tests)
    if len(test_ids) == 0:
        return result
    result["defaults"]["test-ids"] = concacenate_test_ids(test_ids)
    return result


def dieharder_defaults():
    defaults = {"test-ids": concacenate_test_ids(TEST_IDS),
                "test-specific-defaults": []}
    for test_id in TEST_IDS:
        test = {
                    "test-id": test_id,
                    "psamples": 100
                }
        
        if test_id in {200, 201, 202, 203}:
            ntup_min, ntup_max = NTUPLES[test_id]
            test["ntup-range"] = "{} - {}".format(ntup_min, ntup_max)
            test["variants"] = []
            for ntup in range(ntup_min, ntup_max + 1):
                test["variants"].append({
                    "ntup" : ntup,
                    "bytes-per-psamples": get_bytes_per_psample(test_id, ntup)
                })
        else:
            test["bytes-per-psample"] = get_bytes_per_psample(test_id, None)

        if test_id in {201, 204}:
            test["psamples"] = 1000
        if test_id in {205, 206, 207, 208, 209}:
            test["psamples"] = 1
        defaults["test-specific-defaults"].append(test)
    return defaults