import sys
import os
import json
import hashlib

if len(sys.argv) != 3:
    print('Run: python3 hash_buckets.py n s')
    sys.exit()

try:
    n = int(sys.argv[1])
    s = int(sys.argv[2])
except ValueError:
    print('n and s must be numbers')
    sys.exit()

if n < 1 or s < 1:
    print('n and s must be positive')
    sys.exit()