# Advent of code solutions

Done using Python 3.11, stdlib only

## Organization

All puzzles are first organized in directories by `<YEAR>/<DAY>/` . From there, there will be 5 files with the same names:

- `1.py` and `2.py` - the actual python scripts
- `in.txt` - stdin applied to the python scripts
- `1_out.txt` and `2_out.txt` - answers to the puzzles, expected outputs from the python scripts. Each output file number corresponds to the python script number.

## Goal

Since there's not a way to measure code execution speed, these solutions attempt to be as concise as possible while not being grossly underperformant. These solutions should still be relatively fast for a Python solution, though. For example, it's careful to never use `+=` syntax for strings (since Python strings are immutable), but prefers to work with a list/tuple of characters instead.

All of the scripts are standalone, I'm not using a python library module for common code.

## Stdin formatting

These scripts always read from stdin instead of a direct file. These scripts should work regardless of whether or not there's a newline at the end of the file.

## Stdout formatting

All solutions print out the exact answer you'd want to submit. There will always be a newline appended at the end.

## Linting

Linting is done using Ruff, check the pyproject.toml for the configuration.

## Testing

Just run `test.py` - the test script will run every single script due to the naming convention. It runs each python script on the shell with stdin, and it compares the stdout of the script to the actual contents of the output file.

(Should probably use Pytest for this...)
