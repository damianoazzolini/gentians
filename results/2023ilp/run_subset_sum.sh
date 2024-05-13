#!/bin/bash

#SBATCH --job-name=subsum
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_subset_sum.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e subset_sum -d 3 --aggregates "sum(el/1)" --comparison neq --verbose=1

echo "Ended at: "
date