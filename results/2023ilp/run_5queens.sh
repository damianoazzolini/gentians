#!/bin/bash

#SBATCH --job-name=5queens
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=longrun
#SBATCH --output=_5queens.log

echo "Started at: "
date

time python3 -u main.py -e 5queens -d 5 --verbose=1 --arithm add add sub sub --comparison lt --variables 5 -pil 0.8

echo "Ended at: "
date