#!/usr/bin/env python3

import sys

import numpy


# get the gene tissue file name
filename = sys.argv[1]
# open file
fs = open(filename, mode='r')
# create dict to hold samples for gene-tissues pairs
relevant_samples = {}
# step through file
for line in fs:
    # split line into fields
    fields = line.rstrip("\n").split("\t")
    # Create key from gene and tissue
    key = (fields[0], fields[2])
    # initialize dict from key with list to hold samples
    relevant_samples[key] = []
fs.close()

#print(relevant_samples)

# get the metadata file name
filename = sys.argv[2]
# open file
fs = open(filename, mode='r')
# skip line
fs.readline()
# create dict to hold samples for tissue name
tissue_samples = {}
# step through file
for line in fs:
    # split line into fields
    fields = line.rstrip("\n").split("\t")
    # Create key from tissue
    key = fields[6]
    value = fields[0]
    # initialize dict from key with list to hold samples
    tissue_samples.setdefault(key, [])
    tissue_samples[key].append(value)
fs.close()


# get the metadata file name
filename = sys.argv[3]
# open file
fs = open(filename, mode='r')
# skip line
fs.readline()
fs.readline()
header = fs.readline().rstrip("\n").split("\t")
header = header[2:]

tissue_columns = {}
for tissue, samples in tissue_samples.items():
    tissue_columns.setdefault(tissue, [])
    for sample in samples:
        if sample in header:
            position = header.index(sample)
            tissue_columns[tissue].append(position)


print(header)
