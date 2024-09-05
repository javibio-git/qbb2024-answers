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
#       split line
        fields = line.strip("\n").split("\t")
#       save field 0 into gene IDs
        gene_IDs.append(fields[0])
#       save field 1 into gene names
        gene_names.append(fields[1])
#       save 2+ into expression values
        expression.append(fields[2:])
fs.close()

#print(gene_IDs)
#print(gene_names)
#print(expression[0])

tissues = numpy.array(tissues)
gene_IDs = numpy.array(gene_IDs)
gene_names = numpy.array(gene_names)
expression = numpy.array(expression, dtype=float)

#print(tissues)
#print(gene_IDs)
#print(gene_names)
#print(expression)


## Answer 3
#print(range(len(tissues)))
for i in range(10):
    total = 0
    count = 0
    for j in range(len(tissues)):
        total += expression[i][j]
        count += 1
    #print(i, total/count)

## Answer 4

# Calculate the mean values for the first 10 genes using numpy
#mean_values = numpy.mean(expression[:10], axis=1)

#print(mean_values)

# Print the mean values
#print(enumerate(mean_values))
#for i, mean in enumerate(mean_values):
#    print(i, mean)

## Answer 5

print(numpy.mean(expression))
print(numpy.median(expression))

## Answer 6

expression_mod = expression + 1
print(expression_mod)

expression_trans = numpy.log2(expression_mod)

#print(numpy.mean(expression_trans))
#print(numpy.median(expression_trans))

## Answer 7

#expression.log = 

