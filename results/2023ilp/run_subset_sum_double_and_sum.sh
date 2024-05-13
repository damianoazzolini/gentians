#!/bin/bash

#SBATCH --job-name=subs2sum
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_subset_sum_double_and_sum.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e subset_sum_double_and_sum -d 4 --aggregates "sum(el/2)" "sum(el/2)" --arithm add --verbose=1 --variables=4


echo "Ended at: "
date