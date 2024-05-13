#!/bin/bash

#SBATCH --job-name=even_odd
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_even_odd.log

echo "Started at: "
date

multitime -n 10 python3 main.py -e even_odd --verbose=1

echo "Ended at: "
date