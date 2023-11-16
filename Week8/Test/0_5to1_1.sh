start_density=0.5
end_density=1.1
increment=0.1


for density in $(seq $start_density $increment $end_density)
do
    mkdir ../Inputs/WCA_${density}
    logfile=../Inputs/WCA_${density}/log_${density}.log
    dcdfile=../Inputs/WCA_${density}/traj_${density}.dcd
    final_structure=../Inputs/WCA_${density}/final_${density}.lammpstrj
    mpirun lmp -in ../Inputs/2dWCA.in -var density $density -log $logfile -var dcdfile $dcdfile -var final_structure $final_structure

done