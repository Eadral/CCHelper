#!/bin/sh
cd $1
if [ $? -ne 0 ]; then
    exit
fi
mkdir -v $2
if [ $? -ne 0 ]; then
    exit
fi
cd $2
echo "void main() {}" > testfile.txt
touch input.txt
touch output.txt

# code ./testfile.txt
# code ./input.txt
# code ./output.txt
