import os
import shutil
import time

testfile_dir = "testfiles"
outputfile_dir = "outputfiles"


def get_dirs():
    dirs = []
    for name in os.listdir("."):
        if os.path.isdir(name) \
                and not name.startswith(".") \
                and not name.startswith("test_set_error") \
                and not name.startswith("_"):
            dirs.append(name)
    dirs.remove(testfile_dir)
    dirs.remove(outputfile_dir)
    return dirs


def get_testfiles():
    return list(filter(lambda x: x.endswith(".txt"), os.listdir(testfile_dir)))


def get_exe_path(dir_name):
    for name in os.listdir(dir_name):
        if name.endswith(".exe"):
            return name


def get_exe_output(dir_name, testfile, redirect=False):
    shutil.copy(testfile, os.path.join(dir_name, "testfile.txt"))
    exe_path = get_exe_path(dir_name)
    if os.path.exists(os.path.join(dir_name, "output.txt")):
        os.remove(os.path.join(dir_name, "output.txt"))
    os.chdir(dir_name)
    os.system("{} > output.txt < testfile.txt".format(exe_path) if redirect else exe_path)
    os.chdir("..")
    rnd = time.time()
    outputfile_name = "output_{}.txt".format(dir_name)
    shutil.copy(os.path.join(dir_name, "output.txt"), os.path.join(outputfile_dir, outputfile_name))
    lines = open(os.path.join(outputfile_dir, outputfile_name), encoding="utf-8").readlines()
    lines = remove_space(lines)
    return lines


def remove_space(lines):
    lines = list(map(lambda x: x.rstrip(), lines))
    while len(lines) > 0 and lines[-1] == "":
        del lines[-1]
    return lines