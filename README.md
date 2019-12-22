# CCHelper

A Helper for the Compiler Course in Beihang University

## Features

- Verify your compiler's correctness
- Support Windows and Linux.
- Scoring system for optimization.

## Usage 

MIPS test: `python mips_test.py [dir] test_set_mips`

Single MIPS test: `python mips_test.py [dir] test_set_mips [testfilename]`

Performance test: ` python mips_test.py [dir] optimization_test_set speed`

Grammar test: `python pat.py testfiles_grammar [dir] [dir] [dir...]`

Error test: `python test.py [dir] test_set_error`

`dir`: a directory in `CCHelper` that has your `.exe` or `.out` file 

### Example

```shell script
python mips_test.py zyc_mips_ref test_set_mips
python mips_test.py zyc_mips_ref optimization_test_set speed
```

## FAQ

Feel free to contact me

