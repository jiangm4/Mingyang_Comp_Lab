import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages  # Correct import for PdfPages

# Read the data
data = pd.read_csv('Data/1hz3_T310.run.25000000.energy.xvg', comment='@', delimiter='\s+', header=None, skiprows=17)
data.columns = ['Time', 'Potential', 'Kinetic En.', 'Total Energy', 'Temperature', 'Pressure', 'Volume']
data['Time'] /= 1000  # Convert Time from ps to ns

# Create a PDF for the plots
with PdfPages("plots_output.pdf") as pdf:  # Correct usage of PdfPages
    # 6 separate plots for each quantity vs time
    for column in ['Potential', 'Kinetic En.', 'Total Energy', 'Temperature', 'Pressure', 'Volume']:
        plt.figure()
        data.plot(x='Time', y=column, title=f'{column} vs Time')
        plt.xlabel('Time (ns)')
        plt.ylabel(column)
        pdf.savefig()  # saves the current figure into the pdf
        plt.close()

    # Kinetic energy and temperature on the same plot
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('Time (ns)')
    ax1.set_ylabel('Temperature (K)', color=color)
    ax1.plot(data['Time'], data['Temperature'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis
    color = 'tab:blue'
    ax2.set_ylabel('Kinetic En. (kJ/mol)', color=color)
    ax2.plot(data['Time'], data['Kinetic En.'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    pdf.savefig(fig)
    plt.close()
