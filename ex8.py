#! /usr/bin/env python3.7

import subprocess
import os
import argparse

parser = argparse.ArgumentParser(description='Kill the process if it is running')
parser.add_argument('port', type=int, help='the port number to search for')

port = parser.parse_args().port

try:
    result = subprocess.run(
            ['lsof', '-n', "-i4TCP:%s" % port],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE
            )
except subprocess.CalledProcessError:
    print("No process is listening on the provide port")
else:
    listening = None

    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            break

    if listening:
        pid = int(listening.split()[1])
        os.kill(pid, 9)
        print(f"Killed process {pid}")
    else:
        print(f"No process listening on the mentioned port")

