import operator
import os
import sys

from utils import get_exe_output, remove_space
from colorama import init, Fore
init(autoreset=True)

def get_test_names(test_set):
    return os.listdir(test_set)


def unit(dir_name, test_set):
    ncases = 0
    npassed = 0
    for test in get_test_names(test_set):
        ncases += 1
        testfile_name = os.path.join(test_set, test, "testfile.txt")
        output_name = os.path.join(test_set, test, "output.txt")

        lhs_out = get_exe_output(dir_name, testfile_name, "error.txt")
        rhs_out = remove_space(open(output_name).readlines())

        if lhs_out[0] == rhs_out[0]:
            is_correct = True
            for line in rhs_out:
                # print(line)
                if line not in lhs_out:
                    is_correct = False
            if is_correct:
                # correct
                print(Fore.GREEN + "passed: {}".format(test))
                continue
        # error
        print(Fore.LIGHTRED_EX + "failed: {}".format(test))
        if lhs_out[0] != rhs_out[0]:
            print(Fore.LIGHTRED_EX + "first line error: expected '{}' while found '{}'".format(rhs_out[0], lhs_out[0]))
            continue
        for line in rhs_out:
            if line not in lhs_out:
                print(Fore.LIGHTRED_EX + "could not find '{}'".format(line))
                #               .format("'{}'".format(lhs_out[i]), "'{}'".format(rhs_out[i]), i + 1))
        # length = min(len(lhs_out), len(rhs_out))
        # for i in range(length):
        #     if lhs_out[i] != rhs_out[i]:
        #         print(Fore.LIGHTRED_EX + "found {} while expected '{}' at line {}"
        #               .format("'{}'".format(lhs_out[i]), "'{}'".format(rhs_out[i]), i + 1))
                # exit(-1)
        # if len(lhs_out) > len(rhs_out):
        #     print(Fore.LIGHTRED_EX + "found {} while expected {} at line {}"
        #           .format("'{}'".format(lhs_out[length]), "NOTHING", length + 1))
        # else:
        #     print(Fore.LIGHTRED_EX + "found {} while expected {} at line {}"
        #           .format("NOTHING", "'{}'".format(rhs_out[length]), length + 1))
        # exit(-1)

        # if operator.eq(lhs_out, rhs_out):
        #     print(Fore.GREEN + "passed: {}".format(test))
        #     npassed += 1
        # else:
        #     print(Fore.LIGHTRED_EX + "failed: {}".format(test))
        #     length = min(len(lhs_out), len(rhs_out))
        #     for i in range(length):
        #         if lhs_out[i] != rhs_out[i]:
        #             print(Fore.LIGHTRED_EX + "found {} while expected '{}' at line {}"
        #                   .format("'{}'".format(lhs_out[i]), "'{}'".format(rhs_out[i]), i+1))
        #             exit(-1)
        #     if len(lhs_out) > len(rhs_out):
        #         print(Fore.LIGHTRED_EX + "found {} while expected {} at line {}"
        #               .format("'{}'".format(lhs_out[length]), "NOTHING", length + 1))
        #     else:
        #         print(Fore.LIGHTRED_EX + "found {} while expected {} at line {}"
        #               .format("NOTHING", "'{}'".format(rhs_out[length]), length + 1))
        #     exit(-1)


if __name__ == "__main__":
    unit(sys.argv[1], sys.argv[2])
