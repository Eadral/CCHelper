import operator
import os
import sys

from utils import get_exe_output, remove_space


def get_test_names(test_set):
    return os.listdir(test_set)


def unit(dir_name, test_set):
    ncases = 0
    npassed = 0
    for test in get_test_names(test_set):
        ncases += 1
        testfile_name = os.path.join(test_set, test, "testfile.txt")
        output_name = os.path.join(test_set, test, "output.txt")

        lhs_out = get_exe_output(dir_name, testfile_name)
        rhs_out = remove_space(open(output_name).readlines())

        if operator.eq(lhs_out, rhs_out):
            print("passed: {}".format(test))
            npassed += 1
        else:
            print("failed: {}".format(test), file=sys.stdout)
            length = min(len(lhs_out), len(rhs_out))
            for i in range(length):
                if lhs_out[i] != rhs_out[i]:
                    print("found {} while except {} at line {}".format(lhs_out[i], rhs_out[i], i))
                    exit(-1)
            exit(-1)


if __name__ == "__main__":
    unit("zyc", "test_set_error")