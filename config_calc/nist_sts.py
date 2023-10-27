TEST_NAMES = {
    1: "NIST Statistical Testing Suite Frequency (monobits) test",
    2: "NIST Statistical Testing Suite Test For Frequency Within A Block",
    3: "NIST Statistical Testing Suite Cumulative Sum (Cusum) Test",
    4: "NIST Statistical Testing Suite Runs Test",
    5: "NIST Statistical Testing Suite Test for the Longest Run of Ones in a Block",
    6: "NIST Statistical Testing Suite Random Binary Matrix Rank Test",
    7: "NIST Statistical Testing Suite Discrete Fourier Transform (Spectral) Test",
    8: "NIST Statistical Testing Suite Non-overlapping (Aperiodic) Template Matching Test",
    9: "NIST Statistical Testing Suite Overlapping (Periodic) Template Matching Test",
    10: "NIST Statistical Testing Suite Maurer's Universal Statistical Test",
    11: "NIST Statistical Testing Suite Approximate Entropy Test",
    12: "NIST Statistical Testing Suite Random Excursions Test",
    13: "NIST Statistical Testing Suite Random Excursions Variant Test",
    14: "NIST Statistical Testing Suite Serial Test",
    15: "NIST Statistical Testing Suite Linear Complexity Test",
}

def nist_sts_test(args, file_size: int):
    # no test set for execution
    if file_size < args.nist_stream_size:
        return {
            "defaults":{
                "test-ids": []
            },
            "omitted-test":["1-15"],
            "comment": "Set NIST Stream Size it too big for the data size."
        }
    return {
        "defaults":{
            "test-ids": ["1-15"],
            "stream-size": str(args.nist_stream_size),
            "stream-count": str((file_size * 8) // args.nist_stream_size)
        },
        "test-specific-settings" : []
    }

def nist_sts_defaults(args):
    defaults = {"test-ids": ["1-15"],
                "test-specific-defaults": []}
    for test_id in range(1, 16):
        test = {"test-id": test_id,
                "test-name": TEST_NAMES[test_id],}
        
        test["bytes-per-stream"] = str(args.nist_stream_size // 8)

        defaults["test-specific-defaults"].append(test)
    return defaults