#!/bin/bash

#SBATCH --job-name=hamming1
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_hamming_1.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e hamming_1 -d 3 --aggregates "sum(d/2)" --comparison neq --verbose=1 --variables=4

echo "Ended at: "
date