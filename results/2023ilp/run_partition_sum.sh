#!/bin/bash

#SBATCH --job-name=s_partition
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_partition_sum.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e set_partition_sum -d 4 --verbose=1 --comparison neq neq --variables 4 --aggregates "sum(p/2)" -ua -itg 10000 


echo "Ended at: "
date