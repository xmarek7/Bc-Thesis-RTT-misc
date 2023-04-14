from utilities import concacenate_test_ids

SMALLCRUSH_READ_BYTES = {
    1: 41943040,   2: 41943040, 3: 209715200, 4: 104857600,
    5: 104857600,  6: 52428800, 7: 209715200, 8: 31457280,
    9: 125829120, 10: 20971520
}

def smallcrush(file_size: int):
    test_ids = []
    for test_id in range(1, 11):
        if file_size >= SMALLCRUSH_READ_BYTES[test_id]:
            test_ids.append(test_id)
    return {
        "defaults":{
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


