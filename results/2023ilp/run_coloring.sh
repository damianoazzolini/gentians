#!/bin/bash

#SBATCH --job-name=coloring
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=shortrun
#SBATCH --output=_coloring.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e coloring -dh 3 -d 4 --verbose=1

echo "Ended at: "
date