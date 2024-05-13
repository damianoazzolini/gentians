#!/bin/bash

#SBATCH --job-name=msnd
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_magic_square_no_diag.log

echo "Started at: "
date

time python3 -u main.py -e magic_square_no_diag -d 4 --aggregates "sum(x/3,size/1)" --comparison neq --verbose=1 --variables=4 -ua


echo "Ended at: "
date