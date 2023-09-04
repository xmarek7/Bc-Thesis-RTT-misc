from utilities import concacenate_test_ids

ALPHABIT_TEST_NAMES = {
    1: "TestU01 Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=2|Sparse=FALSE",
    2: "TestU01 Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=4|Sparse=FALSE",
    3: "TestU01 Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=8|Sparse=FALSE",
    4: "TestU01 Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=16|Sparse=FALSE",
    5: "TestU01 Alphabit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0",
    6: "TestU01 Alphabit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0",
    7: "TestU01 Alphabit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32",
    8: "TestU01 Alphabit swalk_RandomWalk1|N=1|n=819200|r=0|s=32|L0=64|L1=64",
    9: "TestU01 Alphabit swalk_RandomWalk1|N=1|n=163840|r=0|s=32|L0=320|L1=320",
}

BLOCK_ALPHABIT_TEST_NAMES = {
    (1, 1): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=2|Sparse=FALSE|w=1",
    (1, 2): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=2|Sparse=FALSE|w=2",
    (1, 4): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=2|Sparse=FALSE|w=4",
    (1, 8): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=2|Sparse=FALSE|w=8",
    (1, 16): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=2|Sparse=FALSE|w=16",
    (1, 32): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=2|Sparse=FALSE|w=32",
    (2, 1): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=4|Sparse=FALSE|w=1",
    (2, 2): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=4|Sparse=FALSE|w=2",
    (2, 4): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=4|Sparse=FALSE|w=4",
    (2, 8): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=4|Sparse=FALSE|w=8",
    (2, 16): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=4|Sparse=FALSE|w=16",
    (2, 32): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=4|Sparse=FALSE|w=32",
    (3, 1): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=8|Sparse=FALSE|w=1",
    (3, 2): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=8|Sparse=FALSE|w=2",
    (3, 4): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=8|Sparse=FALSE|w=4",
    (3, 8): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=8|Sparse=FALSE|w=8",
    (3, 16): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=8|Sparse=FALSE|w=16",
    (3, 32): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=8|Sparse=FALSE|w=32",
    (4, 1): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=16|Sparse=FALSE|w=1",
    (4, 2): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=16|Sparse=FALSE|w=2",
    (4, 4): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=16|Sparse=FALSE|w=4",
    (4, 8): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=16|Sparse=FALSE|w=8",
    (4, 16): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=16|Sparse=FALSE|w=16",
    (4, 32): "TestU01 Block Alphabit smultin_MultinomialBitsOver|N=1|n=52428800|r=0|s=32|L=16|Sparse=FALSE|w=32",
    (5, 1): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0|w=1",
    (5, 2): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0|w=2",
    (5, 4): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0|w=4",
    (5, 8): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0|w=8",
    (5, 16): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0|w=16",
    (5, 32): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0|w=32",
    (6, 1): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0|w=1",
    (6, 2): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0|w=2",
    (6, 4): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0|w=4",
    (6, 8): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0|w=8",
    (6, 16): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0|w=16",
    (6, 32): "TestU01 Block Alphabit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0|w=32",
    (7, 1): "TestU01 Block Alphabit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32|w=1",
    (7, 2): "TestU01 Block Alphabit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32|w=2",
    (7, 4): "TestU01 Block Alphabit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32|w=4",
    (7, 8): "TestU01 Block Alphabit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32|w=8",
    (7, 16): "TestU01 Block Alphabit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32|w=16",
    (7, 32): "TestU01 Block Alphabit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32|w=32",
    (8, 1): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=819200|r=0|s=32|L0=64|L1=64|w=1",
    (8, 2): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=819200|r=0|s=32|L0=64|L1=64|w=2",
    (8, 4): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=819200|r=0|s=32|L0=64|L1=64|w=4",
    (8, 8): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=819200|r=0|s=32|L0=64|L1=64|w=8",
    (8, 16): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=819200|r=0|s=32|L0=64|L1=64|w=16",
    (8, 32): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=819200|r=0|s=32|L0=64|L1=64|w=32",
    (9, 1): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=163840|r=0|s=32|L0=320|L1=320|w=1",
    (9, 2): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=163840|r=0|s=32|L0=320|L1=320|w=2",
    (9, 4): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=163840|r=0|s=32|L0=320|L1=320|w=4",
    (9, 8): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=163840|r=0|s=32|L0=320|L1=320|w=8",
    (9, 16): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=163840|r=0|s=32|L0=320|L1=320|w=16",
    (9, 32): "TestU01 Block Alphabit swalk_RandomWalk1|N=1|n=163840|r=0|s=32|L0=320|L1=320|w=32",
}

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


RABBIT_BYTES_PER_REPETITION = {
    1:6553584,
    2:6553600,
    3:6553600,
    4:6553600,
    5:3060,
    6:4194304,
    7:131072,
    8:6553200,
    9:6553440,
    10:6553600,
    11:6553600,
    12:6553600,
    13:6553600,
    14:6553600,
    15:6553600,
    16:6553600,
    17:6553600,
    18:6553596,
    19:6553596,
    20:5245668,
    21:6553600,
    22:6553600,
    23:6553600,
    24:6553600,
    25:6553600,
    26:6552968,
}

RABBIT_TEST_NAMES = {
    1: "TestU01 Rabbit smultin_MultinomialBitsOver|N=6|n=8738112|r=0|s=32|L=38|Sparse=TRUE",
    2: "TestU01 Rabbit snpair_ClosePairsBitMatch|N=1|n=819200|r=0|t=2",
    3: "TestU01 Rabbit snpair_ClosePairsBitMatch|N=1|n=409600|r=0|t=4",
    4: "TestU01 Rabbit svaria_AppearanceSpacings|N=1|Q=1638400|K=1638400|r=0|s=30|L=15",
    5: "TestU01 Rabbit scomp_LinearComp|N=1|n=24480|r=0|s=32",
    6: "TestU01 Rabbit scomp_LempelZiv|N=1|n=33554432|r=0|s=32|k=25",
    7: "TestU01 Rabbit sspectral_Fourier1|N=1|n=1048576|r=0|s=32|k=20",
    8: "TestU01 Rabbit sspectral_Fourier3|N=12700|n=4096|r=0|s=32|k=12",
    9: "TestU01 Rabbit sstring_LongestHeadRun|N=1|n=60|r=0|s=32|L=873792",
    10: "TestU01 Rabbit sstring_PeriodsInStrings|N=1|n=1638400|r=0|s=31",
    11: "TestU01 Rabbit sstring_HammingWeight|N=1|n=1638400|r=0|s=32|L=32",
    12: "TestU01 Rabbit sstring_HammingCorr|N=1|n=1638400|r=0|s=32|L=32",
    13: "TestU01 Rabbit sstring_HammingCorr|N=1|n=819200|r=0|s=32|L=64",
    14: "TestU01 Rabbit sstring_HammingCorr|N=1|n=409600|r=0|s=32|L=128",
    15: "TestU01 Rabbit sstring_HammingIndep|N=1|n=1638400|r=0|s=32|L=16|d=0",
    16: "TestU01 Rabbit sstring_HammingIndep|N=1|n=819200|r=0|s=32|L=32|d=0",
    17: "TestU01 Rabbit sstring_HammingIndep|N=1|n=409600|r=0|s=32|L=64|d=0",
    18: "TestU01 Rabbit sstring_AutoCor|N=1|n=52428737|r=0|s=32|d=1",
    19: "TestU01 Rabbit sstring_AutoCor|N=1|n=52428738|r=0|s=32|d=2",
    20: "TestU01 Rabbit sstring_Run|N=1|n=10485760|r=0|s=32",
    21: "TestU01 Rabbit smarsa_MatrixRank|N=1|n=51200|r=0|s=32|L=32|k=32",
    22: "TestU01 Rabbit smarsa_MatrixRank|N=1|n=512|r=0|s=32|L=320|k=320",
    23: "TestU01 Rabbit smarsa_MatrixRank|N=1|n=50|r=0|s=32|L=1024|k=1024",
    24: "TestU01 Rabbit swalk_RandomWalk1|N=1|n=409600|r=0|s=32|L0=128|L1=128",
    25: "TestU01 Rabbit swalk_RandomWalk1|N=1|n=51200|r=0|s=32|L0=1024|L1=1024",
    26: "TestU01 Rabbit swalk_RandomWalk1|N=1|n=5234|r=0|s=32|L0=10016|L1=10016",
}

CRUSH_TEST_NAMES = {
    1: "TestU01 Small Crush smarsa_BirthdaySpacings|N=1|n=5000000|r=0|d=1073741824|t=2|p=1",
    2: "TestU01 Small Crush sknuth_Collision|N=1|n=5000000|r=0|d=65536|t=2|Sparse=TRUE",
    3: "TestU01 Small Crush sknuth_Gap|N=1|n=200000|r=22|Alpha=0|Beta=0.00390625",
    4: "TestU01 Small Crush sknuth_SimpPoker|N=1|n=400000|r=24|d=64|k=64",
    5: "TestU01 Small Crush sknuth_CouponCollector|N=1|n=500000|r=26|d=16",
    6: "TestU01 Small Crush sknuth_MaxOft|N=1|n=2000000|r=0|d=100000|t=6",
    7: "TestU01 Small Crush svaria_WeightDistrib|N=1|n=200000|r=27|k=256|Alpha=0|Beta=0.125",
    8: "TestU01 Small Crush smarsa_MatrixRank|N=1|n=20000|r=20|s=10|L=60|k=60",
    9: "TestU01 Small Crush sstring_HammingIndep|N=1|n=500000|r=20|s=10|L=300|d=0",
    10: "TestU01 Small Crush swalk_RandomWalk1|N=1|n=1000000|r=0|s=30|L0=150|L1=150",
    1: "TestU01 Crush smarsa_SerialOver|N=1|n=500000000|r=0|d=4096|t=2|Sparse=FALSE",
    2: "TestU01 Crush smarsa_SerialOver|N=1|n=300000000|r=0|d=64|t=4|Sparse=FALSE",
    3: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=0|d=1048576|t=2|Sparse=TRUE",
    4: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=10|d=1048576|t=2|Sparse=TRUE",
    5: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=0|d=1024|t=4|Sparse=TRUE",
    6: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=20|d=1024|t=4|Sparse=TRUE",
    7: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=0|d=32|t=8|Sparse=TRUE",
    8: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=25|d=32|t=8|Sparse=TRUE",
    9: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=0|d=4|t=20|Sparse=TRUE",
    10: "TestU01 Crush smarsa_CollisionOver|N=10|n=10000000|r=28|d=4|t=20|Sparse=TRUE",
    11: "TestU01 Crush smarsa_BirthdaySpacings|N=5|n=20000000|r=0|d=2147483648|t=2|p=1",
    12: "TestU01 Crush smarsa_BirthdaySpacings|N=5|n=20000000|r=0|d=2097152|t=3|p=1",
    13: "TestU01 Crush smarsa_BirthdaySpacings|N=5|n=20000000|r=0|d=65536|t=4|p=1",
    14: "TestU01 Crush smarsa_BirthdaySpacings|N=3|n=20000000|r=0|d=512|t=7|p=1",
    15: "TestU01 Crush smarsa_BirthdaySpacings|N=3|n=20000000|r=7|d=512|t=7|p=1",
    16: "TestU01 Crush smarsa_BirthdaySpacings|N=3|n=20000000|r=14|d=256|t=8|p=1",
    17: "TestU01 Crush smarsa_BirthdaySpacings|N=3|n=20000000|r=22|d=256|t=8|p=1",
    18: "TestU01 Crush snpair_ClosePairs|N=10|n=2000000|r=0|t=2|p=0|m=30|Torus=TRUE",
    19: "TestU01 Crush snpair_ClosePairs|N=10|n=2000000|r=0|t=3|p=0|m=30|Torus=TRUE",
    20: "TestU01 Crush snpair_ClosePairs|N=5|n=2000000|r=0|t=7|p=0|m=30|Torus=TRUE",
    21: "TestU01 Crush snpair_ClosePairsBitMatch|N=4|n=4000000|r=0|t=2",
    22: "TestU01 Crush snpair_ClosePairsBitMatch|N=2|n=4000000|r=0|t=4",
    23: "TestU01 Crush sknuth_SimpPoker|N=1|n=40000000|r=0|d=16|k=16",
    24: "TestU01 Crush sknuth_SimpPoker|N=1|n=40000000|r=26|d=16|k=16",
    25: "TestU01 Crush sknuth_SimpPoker|N=1|n=10000000|r=0|d=64|k=64",
    26: "TestU01 Crush sknuth_SimpPoker|N=1|n=10000000|r=24|d=64|k=64",
    27: "TestU01 Crush sknuth_CouponCollector|N=1|n=40000000|r=0|d=4",
    28: "TestU01 Crush sknuth_CouponCollector|N=1|n=40000000|r=28|d=4",
    29: "TestU01 Crush sknuth_CouponCollector|N=1|n=10000000|r=0|d=16",
    30: "TestU01 Crush sknuth_CouponCollector|N=1|n=10000000|r=26|d=16",
    31: "TestU01 Crush sknuth_Gap|N=1|n=100000000|r=0|Alpha=0|Beta=0.125",
    32: "TestU01 Crush sknuth_Gap|N=1|n=100000000|r=27|Alpha=0|Beta=0.125",
    33: "TestU01 Crush sknuth_Gap|N=1|n=5000000|r=0|Alpha=0|Beta=0.00390625",
    34: "TestU01 Crush sknuth_Gap|N=1|n=5000000|r=22|Alpha=0|Beta=0.00390625",
    35: "TestU01 Crush sknuth_Run|N=1|n=500000000|r=0|Up=TRUE",
    36: "TestU01 Crush sknuth_Run|N=1|n=500000000|r=15|Up=FALSE",
    37: "TestU01 Crush sknuth_Permutation|N=1|n=50000000|r=0|t=10|Sparse=FALSE",
    38: "TestU01 Crush sknuth_Permutation|N=1|n=50000000|r=15|t=10|Sparse=FALSE",
    39: "TestU01 Crush sknuth_CollisionPermut|N=5|n=10000000|r=0|t=13|Sparse=TRUE",
    40: "TestU01 Crush sknuth_CollisionPermut|N=5|n=10000000|r=15|t=13|Sparse=TRUE",
    41: "TestU01 Crush sknuth_MaxOft|N=10|n=10000000|r=0|d=100000|t=5",
    42: "TestU01 Crush sknuth_MaxOft|N=5|n=10000000|r=0|d=100000|t=10",
    43: "TestU01 Crush sknuth_MaxOft|N=1|n=10000000|r=0|d=100000|t=20",
    44: "TestU01 Crush sknuth_MaxOft|N=1|n=10000000|r=0|d=100000|t=30",
    45: "TestU01 Crush svaria_SampleProd|N=1|n=10000000|r=0|t=10",
    46: "TestU01 Crush svaria_SampleProd|N=1|n=10000000|r=0|t=30",
    47: "TestU01 Crush svaria_SampleMean|N=10000000|n=20|r=0",
    48: "TestU01 Crush svaria_SampleCorr|N=1|n=500000000|r=0|k=1",
    49: "TestU01 Crush svaria_AppearanceSpacings|N=1|Q=10000000|K=400000000|r=0|s=30|L=15",
    50: "TestU01 Crush svaria_AppearanceSpacings|N=1|Q=10000000|K=100000000|r=20|s=10|L=15",
    51: "TestU01 Crush svaria_WeightDistrib|N=1|n=2000000|r=0|k=256|Alpha=0|Beta=0.125",
    52: "TestU01 Crush svaria_WeightDistrib|N=1|n=2000000|r=8|k=256|Alpha=0|Beta=0.125",
    53: "TestU01 Crush svaria_WeightDistrib|N=1|n=2000000|r=16|k=256|Alpha=0|Beta=0.125",
    54: "TestU01 Crush svaria_WeightDistrib|N=1|n=2000000|r=24|k=256|Alpha=0|Beta=0.125",
    55: "TestU01 Crush svaria_SumCollector|N=1|n=20000000|r=0|g=10",
    56: "TestU01 Crush smarsa_MatrixRank|N=1|n=1000000|r=0|s=30|L=60|k=60",
    57: "TestU01 Crush smarsa_MatrixRank|N=1|n=1000000|r=20|s=10|L=60|k=60",
    58: "TestU01 Crush smarsa_MatrixRank|N=1|n=50000|r=0|s=30|L=300|k=300",
    59: "TestU01 Crush smarsa_MatrixRank|N=1|n=50000|r=20|s=10|L=300|k=300",
    60: "TestU01 Crush smarsa_MatrixRank|N=1|n=2000|r=0|s=30|L=1200|k=1200",
    61: "TestU01 Crush smarsa_MatrixRank|N=1|n=2000|r=20|s=10|L=1200|k=1200",
    62: "TestU01 Crush smarsa_Savir2|N=1|n=20000000|r=0|m=1048576|t=30",
    63: "TestU01 Crush smarsa_GCD|N=1|n=100000000|r=0|s=30",
    64: "TestU01 Crush smarsa_GCD|N=1|n=40000000|r=10|s=20",
    65: "TestU01 Crush swalk_RandomWalk1|N=1|n=50000000|r=0|s=30|L0=90|L1=90",
    66: "TestU01 Crush swalk_RandomWalk1|N=1|n=10000000|r=20|s=10|L0=90|L1=90",
    67: "TestU01 Crush swalk_RandomWalk1|N=1|n=5000000|r=0|s=30|L0=1000|L1=1000",
    68: "TestU01 Crush swalk_RandomWalk1|N=1|n=1000000|r=20|s=10|L0=1000|L1=1000",
    69: "TestU01 Crush swalk_RandomWalk1|N=1|n=500000|r=0|s=30|L0=10000|L1=10000",
    70: "TestU01 Crush swalk_RandomWalk1|N=1|n=100000|r=20|s=10|L0=10000|L1=10000",
    71: "TestU01 Crush scomp_LinearComp|N=1|n=120000|r=0|s=1",
    72: "TestU01 Crush scomp_LinearComp|N=1|n=120000|r=29|s=1",
    73: "TestU01 Crush scomp_LempelZiv|N=10|n=33554432|r=0|s=30|k=25",
    74: "TestU01 Crush sspectral_Fourier3|N=50000|n=16384|r=0|s=30|k=14",
    75: "TestU01 Crush sspectral_Fourier3|N=50000|n=16384|r=20|s=10|k=14",
    76: "TestU01 Crush sstring_LongestHeadRun|N=1|n=1000|r=0|s=30|L=10000020",
    77: "TestU01 Crush sstring_LongestHeadRun|N=1|n=300|r=20|s=10|L=10000020",
    78: "TestU01 Crush sstring_PeriodsInStrings|N=1|n=300000000|r=0|s=30",
    79: "TestU01 Crush sstring_PeriodsInStrings|N=1|n=300000000|r=15|s=15",
    80: "TestU01 Crush sstring_HammingWeight2|N=100|n=100000000|r=0|s=30|L=1000000",
    81: "TestU01 Crush sstring_HammingWeight2|N=30|n=100000000|r=20|s=10|L=1000000",
    82: "TestU01 Crush sstring_HammingCorr|N=1|n=500000000|r=0|s=30|L=30",
    83: "TestU01 Crush sstring_HammingCorr|N=1|n=50000000|r=0|s=30|L=300",
    84: "TestU01 Crush sstring_HammingCorr|N=1|n=10000000|r=0|s=30|L=1200",
    85: "TestU01 Crush sstring_HammingIndep|N=1|n=300000000|r=0|s=30|L=30|d=0",
    86: "TestU01 Crush sstring_HammingIndep|N=1|n=100000000|r=20|s=10|L=30|d=0",
    87: "TestU01 Crush sstring_HammingIndep|N=1|n=30000000|r=0|s=30|L=300|d=0",
    88: "TestU01 Crush sstring_HammingIndep|N=1|n=10000000|r=20|s=10|L=300|d=0",
    89: "TestU01 Crush sstring_HammingIndep|N=1|n=10000000|r=0|s=30|L=1200|d=0",
    90: "TestU01 Crush sstring_HammingIndep|N=1|n=1000000|r=20|s=10|L=1200|d=0",
    91: "TestU01 Crush sstring_Run|N=1|n=1000000000|r=0|s=30",
    92: "TestU01 Crush sstring_Run|N=1|n=1000000000|r=20|s=10",
    93: "TestU01 Crush sstring_AutoCor|N=10|n=1000000021|r=0|s=30|d=1",
    94: "TestU01 Crush sstring_AutoCor|N=5|n=1000000001|r=20|s=10|d=1",
    95: "TestU01 Crush sstring_AutoCor|N=10|n=1000000020|r=0|s=30|d=30",
    96: "TestU01 Crush sstring_AutoCor|N=5|n=1000000010|r=20|s=10|d=10",
}

SMALL_CRUSH_TEST_NAMES = {
    1: "TestU01 Small Crush smarsa_BirthdaySpacings|N=1|n=5000000|r=0|d=1073741824|t=2|p=1",
    2: "TestU01 Small Crush sknuth_Collision|N=1|n=5000000|r=0|d=65536|t=2|Sparse=TRUE",
    3: "TestU01 Small Crush sknuth_Gap|N=1|n=200000|r=22|Alpha=0|Beta=0.00390625",
    4: "TestU01 Small Crush sknuth_SimpPoker|N=1|n=400000|r=24|d=64|k=64",
    5: "TestU01 Small Crush sknuth_CouponCollector|N=1|n=500000|r=26|d=16",
    6: "TestU01 Small Crush sknuth_MaxOft|N=1|n=2000000|r=0|d=100000|t=6",
    7: "TestU01 Small Crush svaria_WeightDistrib|N=1|n=200000|r=27|k=256|Alpha=0|Beta=0.125",
    8: "TestU01 Small Crush smarsa_MatrixRank|N=1|n=20000|r=20|s=10|L=60|k=60",
    9: "TestU01 Small Crush sstring_HammingIndep|N=1|n=500000|r=20|s=10|L=300|d=0",
    10: "TestU01 Small Crush swalk_RandomWalk1|N=1|n=1000000|r=0|s=30|L0=150|L1=150",
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

def get_test_name(battery: str, test_id: int) -> str:
    if battery == "crush":
        return CRUSH_TEST_NAMES[test_id]
    elif battery == "small_crush":
        return SMALL_CRUSH_TEST_NAMES[test_id]
    elif battery == "rabbit":
        return RABBIT_TEST_NAMES[test_id]
    elif battery == "alphabit":
        return ALPHABIT_TEST_NAMES[test_id]
    raise ValueError("Unknown battery!")

def is_irregular(battery: str, test_id: int) -> bool:
    return (battery == "crush" and (27 <= test_id <= 34 or test_id in {55, 91, 92})) \
            or (battery == "small_crush" and (test_id == 3 or test_id == 5)) \
            or (battery == "rabbit" and test_id == 20)


def get_bytes_per_repetition(args, battery: str, test_id: int) -> int:
    if battery == "crush":
        needed_bytes = CRUSH_BYTES_PER_REPETITION[test_id]
    elif battery == "small_crush":
        needed_bytes = SMALL_CRUSH_BYTES_PER_REPETITION[test_id]
    elif battery == "rabbit":
        needed_bytes = RABBIT_BYTES_PER_REPETITION[test_id] * 8
    else:
        raise ValueError("Uknown battery: {}".format(battery))

    if is_irregular(battery, test_id):
        return int(needed_bytes * (1 + args.tu01_threshold))
    return needed_bytes


def get_bits_per_repetition(args, battery: str, test_id: int) -> int:
    if battery == "rabbit":
        needed_bytes = RABBIT_BYTES_PER_REPETITION[test_id] * 8
    else:
        raise ValueError("Uknown battery: {}".format(battery))

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
            
        if repetitions > 1 or ((is_irregular(battery, test_id) or (battery == "crush" and test_id == 64)) and repetitions != 0):
            test = {
                "test-id": test_id,
                "repetitions": repetitions
            }
    # crush 64 is treated separately - it has low variance in consumed data 
            if is_irregular(battery, test_id) or (battery == "crush" and test_id == 64):
                test["comment"] = "WARNING - this test reads irregular ammount of bytes."
            result["test-specific-settings"].append(test)
    
    result["defaults"]["test-ids"] = concacenate_test_ids(result["defaults"]["test-ids"])
    result["omitted-tests"] = concacenate_test_ids(result["omitted-tests"])
    return result

            
def rabbit(args, file_size: int):
    default_repetitions = (file_size * 8) // args.tu01_bit_nb
    result = {
        "defaults" : {
            "test-ids" : [],
            "repetitions": default_repetitions,
            "bit-nb": str(args.tu01_bit_nb)
        },
        "test-specific-settings": [],
        "omitted-tests": []
    }

    for test_id in range(1, 27):
        if test_id == 5:
            result["omitted-tests"].append(test_id)
            continue
        
        # TODO - changed bit_nb
        repetitions = (file_size * 8 // get_bytes_per_repetition(args, "rabbit", test_id)) + (1 if args.increased else 0)

        if repetitions == 0:
            result["omitted-tests"].add(test_id)
        else:
            result["defaults"]["test-ids"].append(test_id)

        if repetitions != default_repetitions or is_irregular("rabbit", test_id):
            test = {
                "test-id": test_id,
                "repetitions": repetitions
            }

            if is_irregular("rabbit", test_id):
                test["comment"] = "WARNING - this test reads irregular ammount of bytes."
            
            result["test-specific-settings"].append(test)

    result["defaults"]["test-ids"] = concacenate_test_ids(result["defaults"]["test-ids"])
    result["omitted-tests"] = concacenate_test_ids(result["omitted-tests"])
    return result


def rabbit_defaults(args):
    result = {
        "defaults": {
            "test-ids": ["1-26"],
            "bit-nb": str(args.tu01_bit_nb) 
        }, 
        "test-specific-defaults": [],
    }

    for test_id in range(1, 27):
        bytes_per_repetiton = get_bytes_per_repetition(args, "rabbit", test_id)
        result["test-specific-defaults"].append({
                "test-id": test_id,
                "test-name": get_test_name("rabbit", test_id),
                "bytes-per-repetiton": bytes_per_repetiton,
                #"arguments:": get_params("rabbit", test_id)
            })
            
    return result

def alphabit(args, file_size: int):
    repetitions = (file_size * 8) // args.tu01_bit_nb

    result = {
        "defaults":{
            "test-ids": ["1-9"],
            "repetitions": repetitions,
            "bit-nb": str(args.tu01_bit_nb),
            "bit-r": "0",
            "bit-s": "32"
        },
        "ommited-tests": []
    }

    if repetitions == 0:
        result["defaults"]["test-ids"] = []
        result["ommited-tests"]: ["1-9"]

    return result

def alphabit_defaults(args):
    result = {
        "defaults": {
            "test-ids": ["1-9"],
            "bit-nb": str(args.tu01_bit_nb),
            "bit-r": "0",
            "bit-s": "32"
        }, 
        "test-specific-defaults": [],
    }

    for test_id in range(1, 10):
        result["test-specific-defaults"].append({
                "test-id": test_id,
                "test-name": get_test_name("alphabit", test_id),
                "bytes-per-repetiton": str(args.tu01_bit_nb // 8),
            })
            
    return result


def block_alphabit(args, file_size: int):
    repetitions = (file_size * 8) // args.tu01_bit_nb
    result = {
        "defaults":{
            "test-ids": ["1-9"],
            "repetitions": repetitions,
            "bit-nb": str(args.tu01_bit_nb),
            "bit-r": "0",
            "bit-s": "32"
        },
        "test-specific-settings": []
    }
    if repetitions == 0:
        result["defaults"]["test-ids"] = []
        result["ommited-tests"]: ["1-9"]
        return result

    for test_id in range(1, 10):
        test = {
            "test-id": test_id,
            "variants": [],
            "omitted-variants": []
        }
        for bit_w in [1, 2, 4, 8, 16, 32]:
            test["variants"].append({
                "bit-w": str(bit_w),
                "repetitions": repetitions
            })
        result["test-specific-settings"].append(test)
    return result


def block_alphabit_defaults(args):
    defaults = {"test-ids": [
                    "1-9"
                ],
                "repetitions": 819,
                "bit-nb": "52428800",
                "bit-r": "0",
                "bit-s": "32",
                "test-specific-defaults": []}
    for test_id in range(1, 10):
        test = {"test-id": test_id,
                }
        
        test["variants"] = []
        for bit_w in [1, 2, 4, 8, 16, 32]:
            test["variants"].append({
                "bit-w" : bit_w,
                "test-name": BLOCK_ALPHABIT_TEST_NAMES[(test_id, bit_w)],
                "bytes-per-repetition": str(args.tu01_bit_nb // 8)
            })
    
        defaults["test-specific-defaults"].append(test)
    return defaults





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
                "test-name": get_test_name(battery, test_id),
                "bytes-per-repetiton": bytes_per_repetiton,
                "arguments:": get_params(battery, test_id)
            })
            
    return result