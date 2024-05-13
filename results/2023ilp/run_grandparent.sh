#!/bin/bash

#SBATCH --job-name=grandparent
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_grandparent.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e grandparent --verbose=1

echo "Ended at: "
date