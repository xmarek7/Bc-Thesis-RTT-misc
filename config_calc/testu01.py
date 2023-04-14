from utilities import concacenate_test_ids

SMALLCRUSH_READ_BYTES = {
    1: 41943040,   2: 41943040, 3: 209715200, 4: 104857600,
    5: 104857600,  6: 52428800, 7: 209715200, 8: 31457280,
    9: 125829120, 10: 20971520
}

CRUSH_READ_BYTES = {
    1: 2002780160,
    2: 1205862400, 

    3: 408944640,
    4: 408944640,
    5: 408944640,
    6: 408944640,
    7: 408944640,
    8: 408944640,
    9: 408944640,
    10: 408944640,

    11: 807403520,
    12: 1205862400,
    13: 1604321280,
    14: 1688207360,
    15: 1688207360,
    16: 1929379840,
    17: 1929379840,

    18: 167772160,
    19: 241172480,
    20: 283115520,
    
    21: 136314880,
    22: 136314880,

    23: 2569011200,
    24: 2569011200,
    25: 2569011200,
    26: 2569011200,

    27: 1342177280,
    28: 1342177280,
    29: 1981808640,
    30: 1981808640,

    31: 3208642560,
    32: 3208642560,
    33: 5127536640,
    34: 5127536640,

    35: 2002780160,
    36: 2002780160,

    37: 2002780160,
    38: 2002780160,

    39: 2600468480,
    40: 2600468480,

    41: 2002780160,
    42: 2002780160,
    43: 807403520,
    44: 1205862400,

    45: 408944640,
    46: 1205862400,

    47: 807403520,

    48: 2002780160,
    
    49: 828375040,
    50: 880803840,
    
    51: 2055208960,
    52: 2055208960,
    53: 2055208960,
    54: 2055208960,
    
    55: 1656750080,
    
    56: 482344960,
    57: 1447034880,
    58: 608174080,
    59: 1803550720,
    60: 387973120,
    61: 1153433600,
    
    62: 2401239040,
    
    63: 807403520,
    64: 325058560,
    
    65: 608174080,
    66: 367001600,
    67: 681574400,
    68: 408944640,
    69: 671088640,
    70: 408944640,
    
    71: 10485760,
    72: 10485760,
    
    73: 52428800,
    
    74: 115343360,
    75: 335544320,
    
    76: 1342177280,
    77: 1205862400,
    
    78: 1205862400,
    79: 1205862400,
    
    80: 1342177280,
    81: 1205862400,
    
    82: 2002780160,
    83: 2002780160,
    84: 1604321280,
    
    85: 2401239040,
    86: 2401239040,
    87: 2401239040,
    88: 2401239040,
    89: 3208642560,
    90: 964689920,
    
    91: 534773760,
    92: 1604321280,
    
    93: 1342177280,
    94: 2002780160,
    95: 1342177280,
    96:  2002780160 
}

def crush(file_size: int):
    test_ids = []
    for test_id in range(1, 97):
        if file_size >= CRUSH_READ_BYTES[test_id]:
            test_ids.append(test_id)
    if test_ids == []:
        return {}
    return {
        "defaults" : {
            "test-ids" : concacenate_test_ids(test_ids),
            "repetitions" : 1
        }
    }


def smallcrush(file_size: int):
    test_ids = []
    for test_id in range(1, 11):
        if file_size >= SMALLCRUSH_READ_BYTES[test_id]:
            test_ids.append(test_id)
    if test_ids == []:
        return {}
    return {
        "defaults" : {
            "test-ids" : concacenate_test_ids(test_ids),
            "repetitions" : 1
        }
    }


def rabbit(file_size: int):
    return {
        "defaults" : {
            "test-ids" : ["1-26"],
            "repetitions": 1,
            "bit-nb": str(file_size)
        }
    }


def alphabit(file_size: int):
    return{
        "defaults":{
            "test-ids": ["1-9"],
            "repetitions": 1,
            "bit-nb": str(file_size),
            "bit-r": 0,
            "bit-s": 32
        }
    }


def block_alphabit(file_size: int):
    return {
        "defaults":{
            "test-ids": ["1-9"],
            "repetitions": 1,
            "bit-nb": str(file_size),
            "bit-r": 0,
            "bit-s": 32
        },
        "test-specific-settings":[
            {
                "test-id": test_id,
                "variants": [{"bit-w": str(bit_w)} for bit_w in [1, 2, 4, 8, 16, 32]]
            } for test_id in range(1, 10)
        ]
    }