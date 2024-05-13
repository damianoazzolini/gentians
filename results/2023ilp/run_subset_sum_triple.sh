#!/bin/bash

#SBATCH --job-name=subsumtriple
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_subset_sum_triple.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e subset_sum_triple -d 4 --aggregates "sum(el/3)" "sum(el/3)" "sum(el/3)" --verbose=1 --variables=4


echo "Ended at: "
date