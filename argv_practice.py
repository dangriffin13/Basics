
import sys

def print_script_name():
    print("The name of the script is {}".format(sys.argv[0]))


def print_args():
    i = 1
    while i <= len(sys.argv)-1:
        print("Arg ", i, ":", sys.argv[i])
        i += 1


if __name__ == "__main__":
    print_script_name()
    if len(sys.argv) > 1:
        print_args()

