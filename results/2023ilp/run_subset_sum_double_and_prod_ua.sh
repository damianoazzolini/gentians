#!/bin/bash

#SBATCH --job-name=subs2produa
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_subset_sum_double_and_prod_ua.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e subset_sum_double_and_prod -d 4 --aggregates "sum(el/2)" "sum(el/2)" --arithm add mul sub --verbose=2 --variables=5 -ua

echo "Ended at: "
date