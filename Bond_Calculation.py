import mdtraj as md

traj = md.load('Data/1UBQ_processed.pdb')
hbonds = md.baker_hubbard(traj)
num_hbonds = len(hbonds)

with open('output.txt', 'w') as f:
    f.write(f"Total number of hydrogen bonds: {num_hbonds}\n")
ss = md.compute_dssp(traj)[0]  # Assuming one frame
num_helical = sum(1 for s in ss if s in ['H', 'G', 'I'])  # Helix is 'H', 3-10 helix is 'G', and pi-helix is 'I'.

with open('output.txt', 'a') as f:
    f.write(f"Number of helical amino acids: {num_helical}\n")
