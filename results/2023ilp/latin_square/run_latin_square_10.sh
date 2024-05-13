#!/bin/bash

#SBATCH --job-name=latin_square_10000
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_latin_square_10000_itg_10.log

echo "Started at: "
date

multitime -n 10 python3 -u ../main.py -e latin_square -d 4 --aggregates "sum(x/3,cell/1)" --comparison neq --verbose=1 --variables=3 -ua -itg 10000

echo "Ended at: "
date