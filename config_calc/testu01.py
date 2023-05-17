from utilities import concacenate_test_ids

CRUSH_BYTES_PER_REPETITION = {
    1: 2000000000,
    2: 1200000000,
    3: 400000000,
    4: 400000000,
    5: 400000000,
    6: 400000000,
    7: 400000000,
    8: 400000000,
    9: 400000000,
    10: 400000000,
    11: 800000000,
    12: 1200000000,
    13: 1600000000,
    14: 1680000000,
    15: 1680000000,
    16: 1920000000,
    17: 1920000000,
    18: 160000000,
    19: 240000000,
    20: 280000000,
    21: 128000000,
    22: 128000000,
    23: 2560000000,
    24: 2560000000,
    25: 2560000000,
    26: 2560000000,
    27: 1333326306,
    28: 1333331101,
    29: 1974653548,
    30: 1974640110,
    31: 3200051704,
    32: 3199995653,
    33: 5120635483,
    34: 5119635549,
    35: 2000000000,
    36: 2000000000,
    37: 2000000000,
    38: 2000000000,
    39: 2600000000,
    40: 2600000000,
    41: 2000000000,
    42: 2000000000,
    43: 800000000,
    44: 1200000000,
    45: 400000000,
    46: 1200000000,
    47: 800000000,
    48: 2000000000,
    49: 820000000,
    50: 880000000,
    51: 2048000000,
    52: 2048000000,
    53: 2048000000,
    54: 2048000000,
    55: 1653334290,
    56: 480000000,
    57: 1440000000,
    58: 600000000,
    59: 1800000000,
    60: 384000000,
    61: 1152000000,
    62: 2400000000,
    63: 800000000,
    64: 320000800, # irregular, but treated as regular
    65: 600000000,
    66: 360000000,
    67: 680000000,
    68: 400000000,
    69: 668000000,
    70: 400000000,
    71: 480000,
    72: 480000,
    73: 44739280,
    74: 109400000,
    75: 327800000,
    76: 1333336000,
    77: 1200002400,
    78: 1200000000,
    79: 1200000000,
    80: 1333360000,
    81: 1200000000,
    82: 2000000000,
    83: 2000000000,
    84: 1600000000,
    85: 2400000000,
    86: 2400000000,
    87: 2400000000,
    88: 2400000000,
    89: 3200000000,
    90: 960000000,
    91: 533332642,
    92: 1599996811,
    93: 1333333400,
    94: 2000000020,
    95: 1333333400,
    96: 2000000040,
}

SMALL_CRUSH_BYTES_PER_REPETITION = {
    1: 40000000,
    2: 40000000,
    3: 205131120,
    4: 102400000,
    5: 98735996,
    6: 48000000,
    7: 204800000,
    8: 28800000,
    9: 120000000,
    10: 20000000,
}


CRUSH_PARAMS = {
    1: "--params 1 500000000 0 4096 2",
    2: "--params 1 300000000 0 64 4",
    3: "--params 10 10000000 0 1048576 2",
    4: "--params 10 10000000 10 1048576 2",
    5: "--params 10 10000000 0 1024 4",
    6: "--params 10 10000000 20 1024 4",
    7: "--params 10 10000000 0 32 8",
    8: "--params 10 10000000 25 32 8",
    9: "--params 10 10000000 0 4 20",
    10: "--params 10 10000000 28 4 20",
    11: "--params 5 20000000 0 2147483648 2 1",
    12: "--params 5 20000000 0 2097152 3 1",
    13: "--params 5 20000000 0 65536 4 1",
    14: "--params 3 20000000 0 512 7 1",
    15: "--params 3 20000000 7 512 7 1",
    16: "--params 3 20000000 14 256 8 1",
    17: "--params 3 20000000 22 256 8 1",
    18: "--params 10 2000000 0 2 0 30",
    19: "--params 10 2000000 0 3 0 30",
    20: "--params 5 2000000 0 7 0 30",
    21: "--params 4 4000000 0 2",
    22: "--params 2 4000000 0 4",
    23: "--params 1 40000000 0 16 16",
    24: "--params 1 40000000 26 16 16",
    25: "--params 1 10000000 0 64 64",
    26: "--params 1 10000000 24 64 64",
    27: "--params 1 40000000 0 4",
    28: "--params 1 40000000 28 4",
    29: "--params 1 10000000 0 16",
    30: "--params 1 10000000 26 16",
    31: "--params 1 100000000 0 0 0.125",
    32: "--params 1 100000000 27 0 0.125",
    33: "--params 1 5000000 0 0 0.00390625",
    34: "--params 1 5000000 22 0 0.00390625",
    35: "--params 1 500000000 0 1",
    36: "--params 1 500000000 15 0",
    37: "--params 1 50000000 0 10",
    38: "--params 1 50000000 15 10",
    39: "--params 5 10000000 0 13",
    40: "--params 5 10000000 15 13",
    41: "--params 10 10000000 0 100000 5",
    42: "--params 5 10000000 0 100000 10",
    43: "--params 1 10000000 0 100000 20",
    44: "--params 1 10000000 0 100000 30",
    45: "--params 1 10000000 0 10",
    46: "--params 1 10000000 0 30",
    47: "--params 10000000 20 0",
    48: "--params 1 500000000 0 1",
    49: "--params 1 10000000 400000000 0 30 15",
    50: "--params 1 10000000 100000000 20 10 15",
    51: "--params 1 2000000 0 256 0 0.125",
    52: "--params 1 2000000 8 256 0 0.125",
    53: "--params 1 2000000 16 256 0 0.125",
    54: "--params 1 2000000 24 256 0 0.125",
    55: "--params 1 20000000 0 10",
    56: "--params 1 1000000 0 30 60 60",
    57: "--params 1 1000000 20 10 60 60",
    58: "--params 1 50000 0 30 300 300",
    59: "--params 1 50000 20 10 300 300",
    60: "--params 1 2000 0 30 1200 1200",
    61: "--params 1 2000 20 10 1200 1200",
    62: "--params 1 20000000 0 1048576 30",
    63: "--params 1 100000000 0 30",
    64: "--params 1 40000000 10 20",
    65: "--params 1 50000000 0 30 90 90",
    66: "--params 1 10000000 20 10 90 90",
    67: "--params 1 5000000 0 30 1000 1000",
    68: "--params 1 1000000 20 10 1000 1000",
    69: "--params 1 500000 0 30 10000 10000",
    70: "--params 1 100000 20 10 10000 10000",
    71: "--params 1 120000 0 1",
    72: "--params 1 120000 29 1",
    73: "--params 10 25 0 30",
    74: "--params 50000 14 0 30",
    75: "--params 50000 14 20 10",
    76: "--params 1 1000 0 30 10000020",
    77: "--params 1 300 20 10 10000020",
    78: "--params 1 300000000 0 30",
    79: "--params 1 300000000 15 15",
    80: "--params 100 100000000 0 30 1000000",
    81: "--params 30 100000000 20 10 1000000",
    82: "--params 1 500000000 0 30 30",
    83: "--params 1 50000000 0 30 300",
    84: "--params 1 10000000 0 30 1200",
    85: "--params 1 300000000 0 30 30 0",
    86: "--params 1 100000000 20 10 30 0",
    87: "--params 1 30000000 0 30 300 0",
    88: "--params 1 10000000 20 10 300 0",
    89: "--params 1 10000000 0 30 1200 0",
    90: "--params 1 1000000 20 10 1200 0",
    91: "--params 1 1000000000 0 30",
    92: "--params 1 1000000000 20 10",
    93: "--params 10 1000000021 0 30 1",
    94: "--params 5 1000000001 20 10 1",
    95: "--params 10 1000000020 0 30 30",
    96: "--params 5 1000000010 20 10 10",
}

SMALL_CRUSH_PARAMS = {
    1: "--params 1 5000000  0 1073741824 2 1",
    2: "--params 1 5000000  0 65536 2",
    3: "--params 1  200000 22 0.0 0.00390625",
    4: "--params 1  400000 24 64 64",
    5: "--params 1  500000 26 16",
    6: "--params 1 2000000  0 100000 6",
    7: "--params 1  200000 27 256 0.0 0.125",
    8: "--params 1   20000 20 10 60 60",
    9: "--params 1  500000 20 10 300 0",
    10: "--params 1 1000000  0 30 150 150",
}

def get_params(battery: str, test_id: int,)  -> str:
    if battery == "crush":
        return CRUSH_PARAMS[test_id]
    elif battery == "small_crush":
        return SMALL_CRUSH_PARAMS[test_id]
    raise ValueError("Battery must be crush or small_crush.")


def is_irregular(battery: str, test_id: int) -> bool:
    return (battery == "crush" and (27 <= test_id <= 34 or test_id in {55, 91, 92})) \
            or (battery == "small_crush" and (test_id == 3 or test_id == 5))


def get_bytes_per_repetition(args, battery: str, test_id: int) -> int:
    needed_bytes = CRUSH_BYTES_PER_REPETITION[test_id] if battery == "crush" else SMALL_CRUSH_BYTES_PER_REPETITION[test_id]
    if is_irregular(battery, test_id):
        return int(needed_bytes * (1 + args.tu01_threshold))
    return needed_bytes


def crush(args, battery: str, file_size: int):
    if battery not in {"crush", "small_crush"}:
        raise ValueError("Battery in crush must be either crush, or small_crush!")
    result = {
        "defaults": {
            "test-ids": [],
            "repetitions": 1,
        },
        "test-specific-settings": [],
        "omitted-tests": []
    }

    min_id, max_id = 1, (96 if battery == "crush" else 10)
    for test_id in range(min_id, max_id + 1):
        repetitions = (file_size // get_bytes_per_repetition(args, battery, test_id)) + (1 if args.increased else 0)
        if repetitions == 0:
            result["omitted-tests"].append(test_id)
        else:
            result["defaults"]["test-ids"].append(test_id)
            
        if repetitions > 1 or (is_irregular(battery, test_id) and repetitions != 0):
            test = {
                "test-id": test_id,
                "repetitions": repetitions
            }
            if is_irregular(battery, test_id):
                test["comment"] = "WARNING - this test reads irregular ammount of bytes."
            result["test-specific-settings"].append(test)
    
    result["defaults"]["test-ids"] = concacenate_test_ids(result["defaults"]["test-ids"])
    result["omitted-tests"] = concacenate_test_ids(result["omitted-tests"])
    return result

            
def rabbit(file_size: int):
    return {
        "defaults" : {
            "test-ids" : ["1-26"],
            "repetitions": 1,
            "bit-nb": str(file_size)
        }
    }


def alphabit(args, file_size: int):
    return{
        "defaults":{
            "test-ids": ["1-9"],
            "repetitions": 1,
            "bit-nb": str(file_size * 8),
            "bit-r": "0",
            "bit-s": "32"
        }
    }


def block_alphabit(args, file_size: int):
    result = {
        "defaults":{
            "test-ids": ["1-9"],
            "repetitions": 1,
            "bit-nb": str(file_size * 8),
            "bit-r": "0",
            "bit-s": "32"
        },
        "test-specific-settings": []
    }
    for test_id in range(1, 10):
        test = {
            "test-id": test_id,
            "variants": [],
            "omitted-variants": []
        }
        for bit_w in [1, 2, 4, 8, 16, 32]:
            repetitions = 1
            test["variants"].append({
                "bit-w": str(bit_w),
                "repetitions": repetitions
            })
        result["test-specific-settings"].append(test)
    return result


def crush_defaults(args, battery: str):
    if battery not in {"crush", "small_crush"}:
        raise ValueError("Battery in crush must be either crush, or small_crush!")
    result = {
        "defaults": {
            "test-ids": ["1-96"] if battery == "crush" else ["1-10"],
        },
        "test-specific-defaults": [],
    }

    min, max = 1, (96 if battery == "crush" else 10)
    for test_id in range(min, max + 1):
        bytes_per_repetiton = get_bytes_per_repetition(args, battery, test_id)
        result["test-specific-defaults"].append({
                "test-id": test_id,
                "bytes-per-repetiton": bytes_per_repetiton,
                "arguments:": get_params(battery, test_id)
            })
            


    return result