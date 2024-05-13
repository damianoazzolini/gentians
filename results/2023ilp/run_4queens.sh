#!/bin/bash

#SBATCH --job-name=4queens
#SBATCH --ntasks=1
#SBATCH --mem=16gb
#SBATCH --partition=longrun
#SBATCH --output=_4queens.log

echo "Started at: "
date

multitime -n 10 python3 -u main.py -e 4queens -d 5 --verbose=1 --arithm add sub --comparison lt --variables 3 -pil 0.8


echo "Ended at: "
date