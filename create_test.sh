#!/bin/sh
cd $1
mkdir $2
if [ $? -ne 0 ]; then
    exit
fi
cd $2
echo "void main() {}" > testfile.txt
touch output.txt

/mnt/c/Program\ Files/Notepad++/notepad++.exe ./testfile.txt
/mnt/c/Program\ Files/Notepad++/notepad++.exe ./output.txt
