#!/usr/bin/env python3

import sys

my_file = open( sys.argv[2] )
my_str = sys.argv[1]

for my_line in my_file:
    if "##" in my_line:
        continue
    my_line = my_line.rstrip("\n")
    if my_str in my_line:
        print( my_line )
my_file.close()
