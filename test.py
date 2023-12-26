# WARNING: seems to only run on Linux right now.
# Script to test all Advent of Code scripts in parallel.
# Script exits 1 if any subscript fails, but will wait to execute all subscripts first.

import glob
import os
import subprocess
import sys
import time

# TODO maybe use threading here instead of multiprocessing
from multiprocessing import Pool

os.chdir(os.path.dirname(os.path.abspath(__file__)))
paths = glob.glob('20*/**')


def run_command(path):
    rc = 0
    for num in range(1, 3):
        with open(f'./{path}/{num}_out.txt', 'rb') as f:
            target = f.read()
        with open(f'./{path}/in.txt', 'rb') as f:
            stdin = f.read()
        start = time.time()
        stdout, _ = subprocess.Popen(
            f'python ./{path}/{num}.py',
            shell=True,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        ).communicate(input=stdin)
        end = time.time()
        if target != stdout:
            print(f"Failed: {path}/{num} . Expected '{target}', got '{stdout}'", file=sys.stderr)
            rc = 1
        else:
            print(f'Success: {path}/{num} . Completed in {end - start} seconds', file=sys.stderr)
    return rc


pool = Pool()
results = pool.map(run_command, paths)
sys.exit(max(results))
