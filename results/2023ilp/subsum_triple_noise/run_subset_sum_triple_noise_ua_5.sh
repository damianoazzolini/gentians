#!/bin/bash

#SBATCH --job-name=subs35nua
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=longrun
#SBATCH --output=_subset_sum_triple_noise_ua_5.log

echo "Started at: "
date

multitime -n 10 python3 -u ../main.py -e subset_sum_triple -d 4 --aggregates "sum(el/3)" "sum(el/3)" "sum(el/3)" --verbose=1 --variables=4 -ua

echo "Ended at: "
date