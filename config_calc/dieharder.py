import json
from typing import Optional
from utilities import concacenate_test_ids


BYTES_PER_PSAMPLE = {  0:   153600,    1: 4000020,     2: 5120000,     3: 2400000,
                       4:   1048583,   8: 256004,      9: 5120000,    10: 96000,
                      11:  64000,     12: 48000,      13: 9225522,    15: 400000,
                      16:  5402336,   17: 80000000,  100: 400000,    101: 400000,
                     102: 400000,    204: 40000,     205: 614400000, 206: 51200000,
                     207: 452016414, 208: 116881518, 209: 260000000}

NTUPLES = {200: (1, 12), 201: (2, 5), 202: (2,5), 203: (0,32)}

TEST_IDS = [0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 13, 15, 16, 17, 100, 101, 102, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209]

def get_bytes_per_psample(args, test_id: int, ntup: Optional[int]) -> Optional[int]:
    # test with ntuples
    if test_id == 200 and 1 <= ntup <= 12:
        return ntup * 800000 + 4
    elif test_id == 201 and 2 <= ntup <= 5:
        return ntup * 40000
    elif test_id == 202 and 2 <= ntup <= 5:
        return ntup * 400000
    elif test_id == 203 and 0 <= ntup <= 32:
        return (ntup + 1) * 4000000
    # tests with irregular length
    elif test_id in {13, 16, 207, 208}:
        return int(BYTES_PER_PSAMPLE[test_id] * (1 + args.dieharder_threshold))
    # rest of tests
    elif test_id in {0, 1, 2, 3, 4, 8, 9, 10, 11, 12, 15, 17, 100, 101, 102, 204, 205, 206, 209} and ntup is None:
        return BYTES_PER_PSAMPLE[test_id]
    raise ValueError("Invalid test id or combination of test id and ntuples")


def calculate_psamples(args, test_id: int, ntup: Optional[int], file_size: int) -> int:
    if test_id == 0:
        psamples = (file_size - 24) // get_bytes_per_psample(args, test_id, ntup)
    else:
        psamples = file_size // get_bytes_per_psample(args, test_id, ntup)
    return psamples + (1 if args.increased else 0)


def dieharder_variant(args, test_id: int, ntup: int, file_size: int):
    psamples = calculate_psamples(args, test_id, ntup, file_size)
    if psamples == 0:
        return None
    result = {}
    result["arguments"] = "-n {}".format(ntup)
    if test_id == 201:
        result["arguments"] += " -t 10000"
    result["psamples"] = psamples 
    return result


def dieharder_test(args, data_size: int):
    result = {"defaults": {
                    "psamples": 100,
                    "test-ids": []},
              "test-specific-settings": [],
              "omitted-tests": []}
    for test_id in TEST_IDS:
        if test_id in {200, 201, 202, 203}:
            dieharder_test_with_variants(args, test_id, result, data_size)
        else:
            dieharder_no_variant_test(args, test_id, result, data_size)
    result["defaults"]["test-ids"] = concacenate_test_ids(result["defaults"]["test-ids"])
    result["omitted-tests"] = concacenate_test_ids(result["omitted-tests"])
    return result


def dieharder_no_variant_test(args, test_id, result, data_size: int):
    psamples = calculate_psamples(args, test_id, None, data_size)
    if psamples > 0:
        result["defaults"]["test-ids"].append(test_id)
        result["test-specific-settings"].append({
            "test-id": test_id,
            "psamples": psamples
        })  
        if test_id in {13, 16, 207, 208}:
            result["test-specific-settings"][-1]["comment"] = "WARNING - this test reads irregular ammount of bytes."
    else:
        result["omitted-tests"].append(test_id)


def dieharder_test_with_variants(args, test_id, result, data_size: int):
    test = {
        "test-id": test_id,
        "variants": [],
        "omitted-variants": []
    }
    ntup_min, ntup_max = NTUPLES[test_id]
    for ntup in range(ntup_min, ntup_max + 1):
                variant = dieharder_variant(args, test_id, ntup, data_size)
                if variant is None:
                    test["omitted-variants"].append("-n {}".format(ntup))
                else:
                    test["variants"].append(variant)

    if len(test["variants"]) == 0:
        result["omitted-tests"].append(test_id)
    else:
        result["defaults"]["test-ids"].append(test_id)
        result["test-specific-settings"].append(test)


def dieharder_defaults(args):
    defaults = {"test-ids": concacenate_test_ids(TEST_IDS),
                "test-specific-defaults": []}
    for test_id in TEST_IDS:
        test = {"test-id": test_id,
                "psamples": 100}
        
        if test_id in {200, 201, 202, 203}:
            ntup_min, ntup_max = NTUPLES[test_id]
            test["ntup-range"] = "{} - {}".format(ntup_min, ntup_max)
            test["variants"] = []
            for ntup in range(ntup_min, ntup_max + 1):
                test["variants"].append({
                    "ntup" : ntup,
                    "bytes-per-psamples": get_bytes_per_psample(args, test_id, ntup)
                })
        else:
            test["bytes-per-psample"] = get_bytes_per_psample(args, test_id, None)

        if test_id in {201, 204}:
            test["psamples"] = 1000
        if test_id in {205, 206, 207, 208, 209}:
            test["psamples"] = 1
        defaults["test-specific-defaults"].append(test)
    return defaults