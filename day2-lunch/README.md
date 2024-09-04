# Exercises answers for day 2 morning

## Answer 1 

`cut -f 7 hg38-gene-metadata-feature.tsv | sort | uniq -c | sort -n`

There are 19,618 protein coding genes

## Answer 2
`cut -f 1 hg38-gene-metadata-go.tsv | sort | uniq -c | sort -n | tail`

The gene with the most GOs is `ENSG00000168036` with 273 GOs.

`grep "ENSG00000168036" hg38-gene-metadata-go.tsv | sort -k3 > ENSG00000168036_GOs.tsv`

## Answer 4 

File we created:
`grep -w gene gencode.v46.basic.annotation.gtf > gene.gtf`

`grep "IG_._gene" gene.gtf |  cut -f 1 | sort | uniq -c | sort -n`

chr21 = 1, chr16 = 6, chr15 = 16, chr22 = 48, chr2 = 52, chr14 = 91

`grep "IG_._pseudogene" gene.gtf |  cut -f 1 | sort | uniq -c | sort -n`

chr1, chr10, chr18, chr8 = 1; chr9 = 5, chr15 = 6, chr16 = 8, chr2 = 45, chr22 = 48, chr14 = 83

## Answer 5

This is a bit more advance but you can find more info about regular expression (here) [https://www.digitalocean.com/community/tutorials/using-grep-regular-expressions-to-search-for-text-patterns-in-linux#bracket-expressions]

`grep "gene_type \"[A-Za-z_]*_pseudogene" gene.gtf | wc -l`

There are 15,213 pseudogenes

## Answer 6

Provided code
`sed "s/ /\t/g" gene.gtf > gene-tabs.gtf`

`cut -f 1,4,5,14 gene-tabs.gtf > gene-tabs.bed`

