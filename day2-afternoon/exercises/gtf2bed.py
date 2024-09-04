#!/usr/bin/env python3

import sys

my_file = open( sys.argv[1] )


for my_line in my_file:
    if "##" in my_line:
        continue
    my_line = my_line.rstrip("\n")
    fields = my_line.split("\t")
    if "gene" in fields[2]:
        fields2 = fields[8].split(";")
        for my_name in fields2:
            if "gene_name" in my_name:
                gname = my_name
        gene_name = gname.replace("\"", "")
        gene_name = gene_name.replace("gene_name ", "")
        newline = fields[0] + "\t" + fields[3] + "\t" + fields[4] + "\t" + gene_name
        print( newline)

my_file.close()
