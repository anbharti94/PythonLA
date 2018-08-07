#! /usr/bin/env python3.7

import os
import math

count = int(os.getenv("DIGITS") or 10)

print(f"The value of PI is %.{count}f"% math.pi)
