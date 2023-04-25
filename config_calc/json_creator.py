import dieharder
import nist_sts
import testu01
import json
from typing import List
from sys import argv
from os import stat
import argparse




def create_json(args, json_file, file_size: int):
    result = {"randomness-testing-toolkit": {
        "options": argv, # TODO
        "dieharder-settings": dieharder.dieharder_test(file_size, False),
        "dieharder-defaults": dieharder.dieharder_defaults(),
        "nist-sts-settings": nist_sts.nist_sts_test(file_size),
        "tu01-rabbit-settings": testu01.rabbit(file_size),
        "tu01-smallcrush-settings": testu01.smallcrush(file_size),
        "tu01-crush-settings": testu01.crush(file_size),
        "tu01-alphabit-settings": testu01.alphabit(file_size),
        "tu01-blockalphabit-settings": testu01.block_alphabit(file_size)
        }
    }
    print(json.dumps(result, indent=4), file=json_file)


def main(args):
    data_size = args.size if args.data_file is None else stat(args.data_file).st_size
    
    with open(args.config_file, "w") as config_file:
        create_json(args, config_file, data_size)




def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog = "Configuration calcutor for RTT",
        description= "Calculates configuration file for RTT and rtt-py"
    )
    # Input size arguments
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--data-file",
                       type=str,
                       help="Path to file with data to be tested"
    )
    group.add_argument("-s", "--size",
                       type=int,
                       help="Direct size of data that will be tested. Only accepts integers so far."
    )

    # Another arguments
    parser.add_argument("-c", "--config-file", 
                        type=str,
                        default="config.json",
                        help="File the configuration will be written to. Defaults to config.json.")
    
    parser.add_argument("-i", "--dieharder-increased",
                        action="store_true",
                        default=False,
                        help="All Dieharder tests will be produced with psamples increased by one. Used for testing.")
    
    parser.add_argument("-t", "--dieharder-threshold",
                        type=float,
                        default=0.1,
                        help="Sets increase to Dieharder's irregular test. Increased is calculated from mean read bytes.")

    return parser.parse_args()



if __name__ == "__main__":
    args = parse_arguments()
    main(args)