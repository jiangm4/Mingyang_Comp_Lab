#!/bin/bash
#SBATCH --nodes=1
#SBATCH	--ntasks-per-node=1
#SBATCH --cpus-per-task=10
#SBATCH	--time=6:00:00
#SBATCH --mem=20GB
#SBATCH --mail-type=END
#SBATCH --mail-user=tje3676@nyu.edu
#SBATCH --job-name=proton_aimd_1ps_every0.5fs

module purge
module load cp2k/openmpi/intel/20201212

# Run gromacs
mpirun -np 10 --oversubscribe cp2k.popt -i proton.inp -o output.log