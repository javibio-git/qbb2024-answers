#!/usr/bin/env python3

import sys

my_file = open( sys.argv[2] )
fields = sys.argv[1].split(",")

for my_line in my_file:
    # list is declared
    final = []
    my_line = my_line.rstrip("\n")
    if "##" in my_line:
        continue
    lf = my_line.split("\t")
    for f in fields:
        final.append(lf[int(f)])
    print(final)


my_file.close()
