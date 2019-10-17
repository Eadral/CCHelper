from colorama import init, Fore
init(autoreset=True)
import os
import operator
from utils import remove_space
import sys


def diff(file_lhs, file_rhs):
    lhs_out = remove_space(open(file_lhs, encoding="utf-8").readlines())
    rhs_out = remove_space(open(file_rhs, encoding="utf-8").readlines())

    if operator.eq(lhs_out, rhs_out):
        print(Fore.GREEN + "same")
    else:
        print(Fore.RED + "different")
        length = min(len(lhs_out), len(rhs_out))
        for k in range(length):
            if lhs_out[k] != rhs_out[k]:
                print(Fore.RED + "different line {}:{} != {}:{}".format(file_lhs, k+1, file_rhs, k+1))
                print(Fore.RED + "\t{}".format(lhs_out[k]))
                print(Fore.RED + "\t{}".format(rhs_out[k]))
                # exit(-1)
        # exit(-1)


if __name__ == "__main__":
    diff(sys.argv[1], sys.argv[2])
