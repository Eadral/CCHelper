import operator
import sys
import os

from utils import get_dirs, get_testfiles, get_exe_output, testfile_dir, outputfile_dir


def pat(redirect):
    if not os.path.exists(outputfile_dir):
        os.mkdir(outputfile_dir)
    ncases = 0
    npassed = 0
    dirs = get_dirs()
    for testfile in get_testfiles():
        for i in range(0, len(dirs)):
            for j in range(i + 1, len(dirs)):
                ncases += 1
                lhs = dirs[i]
                rhs = dirs[j]

                lhs_out = get_exe_output(lhs, os.path.join(testfile_dir, testfile))
                rhs_out = get_exe_output(rhs, os.path.join(testfile_dir, testfile))

                if operator.eq(lhs_out, rhs_out):
                    print("passed: {}, compared {} and {}".format(testfile, lhs, rhs))
                    npassed += 1
                else:
                    print("failed: {}, comparing {} and {}".format(testfile, lhs, rhs))
                    length = min(len(lhs_out), len(rhs_out))
                    for i in range(length):
                        if lhs_out[i] != rhs_out[i]:
                            print("{}:{} != {}:{}".format(lhs, i, rhs, i))
                            print("\t{}".format(lhs_out[i]))
                            print("\t{}".format(rhs_out[i]))
                            exit(-1)
                    exit(-1)

    print("passed: {}/{}".format(npassed, ncases))


if __name__ == "__main__":
    pat(redirect=True)
