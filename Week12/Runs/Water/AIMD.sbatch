#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--ntasks-per-node=1
#SBATCH --cpus-per-task=8
#SBATCH	--time=6:00:00
#SBATCH --mem=20GB
#SBATCH --mail-type=END
#SBATCH --mail-user=tje3676@nyu.edu
#SBATCH --job-name=water_aimd_1ps_every0.5fs

module purge
module load cp2k/openmpi/intel/20201212

# Run gromacs
mpirun -np 8 --oversubscribe cp2k.popt -i water.inp -o output.log