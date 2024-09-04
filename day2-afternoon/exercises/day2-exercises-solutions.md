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
