import os
import shutil
import time
import operator
import sys

testfile_dir = "testfiles"
outputfile_dir = "outputfiles"


def get_dirs():
    dirs = []
    for name in os.listdir("."):
        if os.path.isdir(name) and not name.startswith("."):
            dirs.append(name)
    dirs.remove(testfile_dir)
    dirs.remove(outputfile_dir)
    return dirs


def get_testfiles():
    return os.listdir(testfile_dir)


def get_exe_path(dir_name):
    for name in os.listdir(dir_name):
        if name.endswith(".exe"):
            return name


def get_exe_output(dir_name, testfile, redirect=False):
    shutil.copy(os.path.join(testfile_dir, testfile), os.path.join(dir_name, "testfile.txt"))
    exe_path = get_exe_path(dir_name)
    if os.path.exists(os.path.join(dir_name, "output.txt")):
        os.remove(os.path.join(dir_name, "output.txt"))
    os.chdir(dir_name)
    os.system("{} > output.txt < testfile.txt".format(exe_path) if redirect else exe_path)
    os.chdir("..")
    rnd = time.time()
    outputfile_name = "output_{}.txt".format(rnd)
    shutil.copy(os.path.join(dir_name, "output.txt"), os.path.join(outputfile_dir, outputfile_name))
    lines = open(os.path.join(outputfile_dir, outputfile_name), encoding="utf-8").readlines()
    lines = list(map(lambda x: x, lines))
    while len(lines) > 0 and lines[-1] == "":
        del lines[-1]
    return lines

def pat(redirect):
    ncases = 0
    npassed = 0
    dirs = get_dirs()
    for testfile in get_testfiles():
        for i in range(0, len(dirs)):
            for j in range(i + 1, len(dirs)):
                ncases += 1
                lhs = dirs[i]
                rhs = dirs[j]

                lhs_out = get_exe_output(lhs, testfile)
                rhs_out = get_exe_output(rhs, testfile)

                if operator.eq(lhs_out, rhs_out):
                    print("passed: {}, compared {} and {}".format(testfile, lhs, rhs))
                    npassed += 1
                else:
                    print("failed: {}, comparing {} and {}".format(testfile, lhs, rhs), file=sys.stdout)

    print("passed: {}/{}".format(npassed, ncases))

if __name__ == "__main__":
    pat(redirect=False)
