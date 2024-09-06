# Day 2 afternoon exercises answers

## Answer 1

To decompress `*.gz` files you can use `gunzip` for instance: `gunzip GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct.gz`, which will create a new file called `GTEx_Analysis_2017-06-05_v8_RNASeQCv1.1.9_gene_median_tpm.gct`. The old `gz` file will be removed (but there are ways to preserve the original file).

### Pseudocode

```
open file

skip 2 lines

split column header by tabs and skip first two entries

create way to hold gene names

create way to hold expression values

for each line
	split line
	save field 0 into gene IDs
	save field 1 into gene names
	save 2+ into expression values
```

### Python code
```
#!/usr/bin/env python

import sys

import numpy

# open file
fs = open(sys.argv[1], mode ='r')

# skip 2 lines
fs.readline()
fs.readline()

# this is to check everything is working fine (a checkpoint). Unco
#print(fs.readline())

# split column header by tabs and skip first two entries
line = fs.readline()
fields = line.strip("\n").split("\t")
tissues =  fields[2:]
# print(tissues) # checkpoint

# create way to hold gene names
gene_names = []
gene_IDs = []

# create way to hold expression values
expression = []

# for each line
for line in fs:
#	split line
	fields = line.strip("\n").split("\t")
#	save field 0 into gene IDs
	gene_IDs.append(fields[0])
#	save field 1 into gene names
	gene_IDs.append(fields[1])
#	save 2+ into expression values
	expression.append(fields[2:])
fs.close()
	
#print(gene_IDs)
#print(gene_names)
#print(expression[0])

tissues = numpy.array(tissues)
gene_IDs = numpy.array(gene_IDs)
gene_names = numpy.array(gene_names)
expression = numpy.array(expression, dtype=float)

print(gene_IDs)
print(gene_names)
print(expression)

```
