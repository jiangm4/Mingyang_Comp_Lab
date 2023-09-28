import mdtraj as md
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# a) Load the trajectory (replace this with your actual trajectory file path and topology)
traj = md.load_xtc('Data/1hz3_T310.stepid25000000.every100ps.nowater.xtc', top='Data/1hz3_T310.start.nowater.gro')

# b) Compute end-end distance and radius of gyration
def end_end(traj):
    first = traj.xyz[:, 0, :]
    last = traj.xyz[:, -1, :]
    dist = np.linalg.norm(first - last, axis=1)
    return dist

end_to_end_distances = end_end(traj)
radii_of_gyration = md.compute_rg(traj)

# c) Plot end-end distance and radius of gyration vs. time
with PdfPages('trajectory_analysis.pdf') as pdf:
    plt.figure()
    time = traj.time / 1000  # Convert to ns
    plt.plot(time, end_to_end_distances, label='End-to-End Distance')
    plt.plot(time, radii_of_gyration, label='Radius of Gyration')
    plt.xlabel('Time (ns)')
    plt.ylabel('Distance (nm)')
    plt.legend()
    plt.title('End-to-End Distance and Radius of Gyration vs Time')
    pdf.savefig()
    plt.close()

    # d) Plot histograms
    plt.figure()
    plt.hist(end_to_end_distances, bins=100, density=True, alpha=0.5, label='End-to-End Distance')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Probability Density')
    plt.title('End-to-End Distance Histogram')
    pdf.savefig()
    plt.close()

    plt.figure()
    plt.hist(radii_of_gyration, bins=100, density=True, alpha=0.5, label='Radius of Gyration')
    plt.xlabel('Distance (nm)')
    plt.ylabel('Probability Density')
    plt.title('Radius of Gyration Histogram')
    pdf.savefig()
    plt.close()
