#!/bin/bash

#SBATCH --job-name=clique
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=shortrun
#SBATCH --output=_clique.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e clique -d 7 --comparison neq --verbose=1 --variables=2

echo "Ended at: "
date