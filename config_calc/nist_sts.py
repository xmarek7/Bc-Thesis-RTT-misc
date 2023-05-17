def nist_sts_test(args, file_size: int):
    # no test set for execution
    if file_size < args.nist_stream_size:
        return {"comment": "Given NIST stream size is too big."}
    return {
        "defaults":{
            "test-ids": ["1-15"],
            "stream-size": str(args.nist_stream_size),
            "stream-count": str((file_size * 8) // args.nist_stream_size)
        },
        "test-specific-settings" : []
    }