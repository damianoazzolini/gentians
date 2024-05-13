#!/bin/bash

#SBATCH --job-name=scnew_partition
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_partition_sum_new.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e set_partition_sum_new -d 4 --verbose=1 --comparison neq neq --variables 4 --aggregates "sum(p/2)" -ua 

echo "Ended at: "
date