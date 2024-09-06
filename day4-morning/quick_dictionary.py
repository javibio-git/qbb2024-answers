#!/usr/bin/env python


import sys



L = [0, 1, 2]

d = { 9 : "nueve" }

D = {"lista" : L, 5.5 : "cincopcinco", "dic"  : d }

#print(L)
#print(d)
#print(D)


S = "it was the best of times it was the worst of times"

S = S.split()

print(S)

first = {}

for i in range(len(S)):
    word = S[i]
    if word in first:
        continue
    else:
        first[word] = i

#print(first)


# Count the number of times a character appears in the following sentence

S = "it was the best of times it was the worst of times"

counts = {}

for i in range(len(S)):
    char = S[i]
    if char not in counts:
        counts[char] = 0
    counts[char] += 1

print(counts)
