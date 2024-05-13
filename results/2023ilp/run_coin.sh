#!/bin/bash

#SBATCH --job-name=coin
#SBATCH --ntasks=1
#SBATCH --mem=8gb
#SBATCH --partition=shortrun
#SBATCH --output=_coin.log

echo "Started at: "
date

multitime -n 10 python3 main.py -e coin --verbose=1

echo "Ended at: "
date