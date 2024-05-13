#!/bin/bash

#SBATCH --job-name=subsumdouble
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_subset_sum_double_noise_ua.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e subset_sum_double -d 4 --aggregates "sum(el/2)" "sum(el/2)" --arithm add --verbose=1 --variables=3 -ua

echo "Ended at: "
date