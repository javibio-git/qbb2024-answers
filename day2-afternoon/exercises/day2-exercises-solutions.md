# Day 2 afternoon exercises answers

## Answer 1

This is my take on the `grep.py` script:

```
#!/usr/bin/env python3

import sys

# save command line arguments to a variable
my_file = open( sys.argv[2] )
my_str = sys.argv[1]

# use a for loop to read each line of the file
for my_line in my_file:
    if "##" in my_line:
        continue
    my_line = my_line.rstrip("\n")
    # evaluate if the string we want to look for is present in each line, if so, print the line
    if my_str in my_line:
        print( my_line )
my_file.close()

```

## Answer 2

My take on `cut.py`:

```
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

```

## Answer 3 

My take on `gtf2bed.py` 

```
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

```

## Answer 4

This is the fixed `tally.py` script now called `tally-fixed.py`

```

#!/usr/bin/env python3

# Compare to grep -v "#" | cut -f 1 | uniq -c
# ... spot and fix the three bugs in this code

import sys

my_file = open( sys.argv[1] )

chr = "chr1"
count = 0

for my_line in my_file:
    if "#" in my_line:
        continue
    fields = my_line.split("\t")
    if fields[0] != chr:
        print( count, chr )
        chr = fields[0]
        count = 1
        continue
    count = count + 1
print( count, chr)

my_file.close()

```
