import dieharder
import nist_sts
import testu01
import json
import utilities

from typing import List
from sys import argv, stderr, exit
from os import stat
import argparse


def create_json(args, json_file, file_size: int):
    result = {
        "options": argv,
        "data-size": file_size,
        "randomness-testing-toolkit": {
            "dieharder-settings": dieharder.dieharder_test(args, file_size),
            "dieharder-defaults": dieharder.dieharder_defaults(args),

            "nist-sts-settings": nist_sts.nist_sts_test(args, file_size),
            "nist-sts-defaults": nist_sts.nist_sts_defaults(args),

            "tu01-rabbit-settings": testu01.rabbit(args, file_size), 
            "tu01-rabbit-defaults": testu01.rabbit_defaults(args),
            
            "tu01-smallcrush-settings": testu01.crush(args, "small_crush", file_size),
            "tu01-smallcrush-defaults": testu01.crush_defaults(args, "small_crush"),
            
            "tu01-crush-settings": testu01.crush(args, "crush", file_size),
            "tu01-crush-defaults": testu01.crush_defaults(args, "crush"),
            
            "tu01-alphabit-settings": testu01.alphabit(args, file_size),
            "tu01-alphabit-defaults": testu01.alphabit_defaults(args),

            "tu01-blockalphabit-settings": testu01.block_alphabit(args, file_size),
            "tu01-blockalphabit-defaults": testu01.block_alphabit_defaults(args),
        }
    }
    print(json.dumps(result, indent=4), file=json_file)


def main(args) -> int:
    if args.max_test_size:
        data_size = largest_bytes_per_test(args)
        print("For each test to be executed at least once are {} bytes required".format(data_size))
    elif args.data_file is not None:  
        data = stat(args.data_file).st_size
    else:
        parsed = utilities.parse_size(args.size)
        if parsed is None:
            print("File size string is not in valid format.", file=stderr)
            exit(-1)    
        data_size = parsed

    if data_size == 0:
        print("The data size is 0, please insert a positive number", file=stderr)
        exit(-1)

    with open(args.config_file, "w") as config_file:
        create_json(args, config_file, data_size)


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog = "Configuration calculator for RTT",
        description= "Calculates battery configuration file for RTT and rtt-py"
    )

    # Input size arguments - only one is accepter
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--data-file",
                       type=str,
                       help="Path to file with data to be tested"
    )

    group.add_argument("-s", "--size",
                       type=str,
                       help="Size of data that will be tested. Either integer, or integer followed by a unit (K, M, G, B accepted as powers of two)."
    )

    group.add_argument("-m", "--max-test-size",
                       default=False,
                       action="store_true",
                       help="Creates configuration file where each test is executed at least once. Also prints the number of required bytes."
    )
    

    # Another arguments
    parser.add_argument("-c", "--config-file", 
                        type=str,
                        default="config.json",
                        help="File the configuration will be written to. Defaults to config.json.")
    
    parser.add_argument("-i", "--increased",
                        action="store_true",
                        default=False,
                        help="All tests will be produced with setting one higher than it should be. Used for testing.")
    
    parser.add_argument("-t", "--dieharder-threshold",
                        type=float,
                        default=0.001,
                        help="Sets increase to Dieharder's irregular test. Increased is calculated from mean read bytes. ")
    
    parser.add_argument("-n", "--nist-stream-size",
                        type=int,
                        default=1000000,
                        help="Sets stream size for NIST battery. Defaults to milion.")

    parser.add_argument("-u", "--tu01-threshold",
                        type=float,
                        default=0.01,
                        help="Sets increase to TestU01's irregular test. Increased is calculated from mean read bytes.")

    parser.add_argument("-b", "--tu01-bit-nb",
                        type=int,
                        default=52428800,
                        help="Argument to TestU01's Rabbit, Alphabit and BlockAlphabit batteries. Defaults to 52428800.")

    return parser.parse_args()

# Finds the largest ammount of bytes needed for test execution for current settings.
# For standard settings the result is:
# biggest: Size: 5124001234, battery: crush, test: id: 33
def largest_bytes_per_test(args) -> int:
    biggest = 0
    battery = ""
    biggest_id = ""
    
    # Dieharder
    for test_id in dieharder.TEST_IDS:
        if test_id in dieharder.NTUPLES:
            ntup_min, ntup_max = dieharder.NTUPLES[test_id]
            for ntup in range(ntup_min, ntup_max + 1):
                needed_bytes = dieharder.get_bytes_per_psample(args, test_id, ntup)
                if needed_bytes > biggest:
                    biggest = needed_bytes
                    battery = "dieharder"
                    biggest_id = "id: {}, ntup: {}".format(test_id, ntup)
        else:
            needed_bytes = dieharder.get_bytes_per_psample(args, test_id, None)
            if needed_bytes > biggest:
                biggest = needed_bytes
                battery = "dieharder"
                biggest_id = "id: {}".format(test_id)

    # TestU01
    # small_crush
    for test_id in range(1, 11):
        needed_bytes = testu01.get_bytes_per_repetition(args, "small_crush", test_id)
        if needed_bytes > biggest:
            biggest = needed_bytes
            battery = "small_crush"
            biggest_id = "id: {}".format(test_id)
    # crush
    for test_id in range(1, 97):
        needed_bytes = testu01.get_bytes_per_repetition(args, "crush", test_id)
        if needed_bytes > biggest:
            biggest = needed_bytes
            battery = "crush"
            biggest_id = "id: {}".format(test_id)
    
    # Nist
    if args.nist_stream_size // 8 > biggest:
        biggest = args.nist_stream_size // 8
        battery = "nist"
        biggest_id = "Not specific".format(test_id)
        
    #print("Size: {}, battery: {}, test: {}".format(biggest, battery, biggest_id))
    return biggest



if __name__ == "__main__":
    args = parse_arguments()
    main(args)