#!/bin/bash

#SBATCH --job-name=adjred
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_adjacent_to_red.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e adjacent_to_red -d 4 --verbose=1

echo "Ended at: "
date