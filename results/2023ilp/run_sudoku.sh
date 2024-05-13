#!/bin/bash

#SBATCH --job-name=sudoku
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=shortrun
#SBATCH --output=_sudoku.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e sudoku -d 3

echo "Ended at: "
date