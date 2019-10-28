import operator
import sys
import os
from colorama import init, Fore, Back, Style
init(autoreset=True)

from utils import get_testfiles, get_exe_output, outputfile_dir

def pat(testfile_dir, redirect, dirs):
    if not os.path.exists(outputfile_dir):
        os.mkdir(outputfile_dir)
    ncases = 0
    npassed = 0
    # dirs = get_dirs()
    for testfile in get_testfiles(testfile_dir):
        for i in range(0, len(dirs)):
            for j in range(i + 1, len(dirs)):
                ncases += 1
                lhs = dirs[i]
                rhs = dirs[j]

                lhs_out = get_exe_output(lhs, os.path.join(testfile_dir, testfile))
                rhs_out = get_exe_output(rhs, os.path.join(testfile_dir, testfile))

                if operator.eq(lhs_out, rhs_out):
                    print(Fore.GREEN + "passed: {}, compared {} and {}".format(testfile, lhs, rhs))
                    npassed += 1
                else:
                    print(Fore.LIGHTRED_EX + "failed: {}, comparing {} and {}".format(testfile, lhs, rhs))
                    length = min(len(lhs_out), len(rhs_out))
                    for k in range(length):
                        if lhs_out[k] != rhs_out[k]:
                            print(Fore.LIGHTRED_EX + "different line {}:{} != {}:{}".format(lhs, k+1, rhs, k+1))
                            print(Fore.LIGHTRED_EX + "\t{}".format(lhs_out[k]))
                            print(Fore.LIGHTRED_EX + "\t{}".format(rhs_out[k]))
                            exit(-1)
                    if len(lhs_out) > len(rhs_out):
                        print(Fore.LIGHTRED_EX + "found {} while except {} at line {}"
                              .format("'{}'".format(lhs_out[length]), "NOTHING", length + 1))
                    else:
                        print(Fore.LIGHTRED_EX + "found {} while except {} at line {}"
                              .format("NOTHING", "'{}'".format(rhs_out[length]), length + 1))
                    exit(-1)

    if npassed == ncases:
        print(Fore.GREEN + "passed: {}/{}".format(npassed, ncases))
    else:
        print(Fore.RED + "passed: {}/{}".format(npassed, ncases))


if __name__ == "__main__":
    pat(testfile_dir=sys.argv[1], redirect=True, dirs=sys.argv[2:])
