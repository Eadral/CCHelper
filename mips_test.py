import operator
import os
import sys

from colorama import init, Fore

from utils import get_mips_output, remove_space

import concurrent.futures as confu
import multiprocessing.pool as mpp

init(autoreset=True)


def get_test_names(test_set):
    return os.listdir(test_set)


def run_unit(dir_name, test, test_set):
    try:
        testfile_name = os.path.join(test_set, test)
        output_name = os.path.join(test_set, test, "output.txt")

        # lhs_out = get_exe_output(dir_name, testfile_name, "error.txt")
        lhs_out, cycles = get_mips_output(dir_name, testfile_name)
        lhs_out = remove_space(lhs_out)
        rhs_out = remove_space(open(output_name).readlines())

        if operator.eq(lhs_out, rhs_out):
            print(Fore.GREEN + "passed: {}. Cycles: {}".format(test, cycles))
            return True
        else:
            print(Fore.LIGHTRED_EX + "failed: {}".format(test))
            length = min(len(lhs_out), len(rhs_out))
            for i in range(length):
                if lhs_out[i] != rhs_out[i]:
                    print(Fore.LIGHTRED_EX + "found {} while expected '{}' at line {}"
                          .format("'{}'".format(lhs_out[i]), "'{}'".format(rhs_out[i]), i + 1))
                    return False
            if len(lhs_out) > len(rhs_out):
                print(Fore.LIGHTRED_EX + "found {} while expected {} at line {}"
                      .format("'{}'".format(lhs_out[length]), "NOTHING", length + 1))
            elif len(lhs_out) < len(rhs_out):
                print(Fore.LIGHTRED_EX + "found {} while expected {} at line {}"
                      .format("NOTHING", "'{}'".format(rhs_out[length]), length + 1))
            return False
            # exit(-1)
    except:
        print(Fore.LIGHTRED_EX + "failed: {}. unable to compile and run".format(test))
        return False


def unit(dir_name, test_set):
    ncases = 0
    npassed = 0
    for test in get_test_names(test_set):
        ncases += 1
        if run_unit(dir_name, test, test_set):
            npassed += 1
    if ncases == npassed:
        print(Fore.GREEN + "Passed {}/{}".format(npassed, ncases))
    else:
        print(Fore.LIGHTRED_EX + "Passed {}/{}".format(npassed, ncases))


if __name__ == "__main__":
    # unit("zyc", "test_set_mips")
    if not os.path.exists("outputfiles"):
        os.mkdir("outputfiles")

    if len(sys.argv) <= 3:
        unit(sys.argv[1], sys.argv[2])
    else:
        run_unit(sys.argv[1], sys.argv[3], sys.argv[2])
        # pass
