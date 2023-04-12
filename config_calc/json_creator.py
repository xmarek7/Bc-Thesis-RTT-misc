import dieharder
import json
from typing import List
from sys import argv
from os import stat




def create_json(json_file,file_size: int):
    result = {"randomness-testing-toolkit": {
        "dieharder-settings": dieharder.dieharder_test(file_size)
        }
    }
    
    print(json.dumps(result, indent=4), file=json_file)



def main():
    # parse arguments
    if (len(argv) != 5):
        print("Invalid ammount of arguments!")
        return

    input = config = None
    for i in [1, 3]:
        if argv[i] == "-f":
            input = argv[i + 1]
        elif argv[i] == "-c":
            config = argv[i + 1]
    if input is None or config is None:
        print("Arguments are not valid!")
        return
    
    # read file size
    file_size = stat(input).st_size

    # write to JSON config file
    with open(config, "w") as config_file:
        create_json(config_file, file_size)


if __name__ == "__main__":
    main()


