#!/bin/bash

#SBATCH --job-name=sc_partition
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_partition_sum_cardinality.log

echo "Started at: "
date

time python3 -u main.py -e set_partition_sum_and_cardinality -d 4 --verbose=1 --comparison neq neq --variables 4 --aggregates "sum(p/2)" "count(p/2)" -ua -itg 10000

echo "Ended at: "
date