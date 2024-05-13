#!/bin/bash

#SBATCH --job-name=hammingh1
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_hamming_harder_1.log

echo "Started at: "
date

time python3 -u main.py -e harder_hamming_1 -d 4 --verbose=1 --comparison neq --variables 4 --aggregates "sum(d/2)" --arithm abs

echo "Ended at: "
date