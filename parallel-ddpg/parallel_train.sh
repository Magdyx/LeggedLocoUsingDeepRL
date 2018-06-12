#!/bin/sh

#SBATCH --job-name=ddpg_train_parallel
#SBATCH --partition=cpu
#SBATCH --nodes=20
#SBATCH --ntasks=5
#SBATCH --time=200:00:00

module load Anaconda3/4.2.0
module load GLib/2.49.5-intel-2016b
source activate opensim-rl
python main2.py 20
