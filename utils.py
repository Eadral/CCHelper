import os
import shutil
import time
import platform

outputfile_dir = "outputfiles"


def get_testfiles(testfile_dir):
    return list(filter(lambda x: x.endswith(".txt"), os.listdir(testfile_dir)))


def get_exe_path(dir_name):
    for name in os.listdir(dir_name):
        if name.endswith(".exe") or name.endswith(".out"):
            return name


def get_exe_output(dir_name, testfile, outputname, redirect=False):
    shutil.copy(testfile, os.path.join(dir_name, "testfile.txt"))
    exe_path = get_exe_path(dir_name)
    if os.path.exists(os.path.join(dir_name, outputname)):
        os.remove(os.path.join(dir_name, outputname))
    os.chdir(dir_name)
    if platform.system() == "Linux":
        os.system("./{} > output.txt < testfile.txt".format(exe_path) if redirect else exe_path)
    else:
        os.system("{} > output.txt < testfile.txt".format(exe_path) if redirect else exe_path)
    os.chdir("..")
    rnd = time.time()
    outputfile_name = "output_{}.txt".format(dir_name)
    shutil.copy(os.path.join(dir_name, outputname), os.path.join(outputfile_dir, outputfile_name))
    lines = open(os.path.join(outputfile_dir, outputfile_name), encoding="utf-8").readlines()
    lines = remove_space(lines)
    return lines


def get_mips_output(dir_name, test, outputname="mips.txt"):
    shutil.copy(os.path.join(test, "testfile.txt"), os.path.join(dir_name, "testfile.txt"))
    exe_path = get_exe_path(dir_name)
    if os.path.exists(os.path.join(dir_name, outputname)):
        os.remove(os.path.join(dir_name, outputname))
    os.chdir(dir_name)
    if platform.system() == "Linux":
        os.system("timeout 8 ./{} 1>out 2>err".format(exe_path))
    else:
        # print("..\\timeout.exe 8000 {} 1>out 2>err".format(exe_path))
        os.system("..\\timeout.exe 8000 {} 1>out 2>err".format(exe_path))
    os.chdir("..")
    rnd = time.time()
    shutil.copy(os.path.join(dir_name, outputname), "mips.asm")
    shutil.copy(os.path.join(test, "input.txt"), "input.txt")
    if platform.system() == "Linux":
        os.system("DISPLAY= timeout 8 java -jar mars.jar nc ic mips.asm < input.txt > output.txt")
    else:
        os.system("timeout.exe 8000 java -jar mars.jar nc ic mips.asm < input.txt > output.txt")
    os.system("if errorLevel 1 echo TLE\n-1 > output.txt")
    # os.system("timeout /t 5")
    # os.system("taskkill /im java.exe /f")
    lines = open("output.txt", encoding="utf-8").readlines()
    lines = remove_space(lines)
    return lines[:-1], int(lines[-1])


def remove_space(lines):
    lines = list(map(lambda x: x.rstrip(), lines))
    while len(lines) > 0 and lines[-1] == "":
        del lines[-1]
    return lines
