def nist_sts_test(file_size: int):
    # no test set for execution
    if file_size < 131072:
        return {}
    return {
        "defaults":{
            "test-ids": ["1-15"],
            "stream-size": "1000000",
            "stream-count": str(file_size // 131072)
        },
        "test-specific-settings" : []
    }