# Project-cluster

Identify and count clusters across a series of .sam files.

## Usage

`python run.py --help`

## Install

`git clone https://github.com/DomBennett/Project-cluster.git`

## Requirements

* One .sam file stored per folder
* cdhit
* Python (v2 or v3)

## Steps

* Convert .sam to .fasta by extracting the orthologous sequence identified within
the .sam file.
* Run cdhit
* Count clusters with greater than `min_nsqs`
* Report number of clusters per .sam in a .csv

## Authors

D.J. Bennett & J.S. Eriksson
