#!/bin/bash

#SBATCH --job-name=scs_partition
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_partition_sum_cardinality_square_new.log

echo "Started at: "
date

time python3 -u main.py -e set_partition_sum_cardinality_and_square -d 4 --verbose=1 --comparison neq neq --variables 4 --aggregates "sum(sq/2)" "count(p/2)" -ua 

echo "Ended at: "
date