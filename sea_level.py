import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Read data from file
df = pd.read_csv('epa-sea-level.csv')

# Create scatter plot
fig = plt.figure()
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create first line of best fit
lin_reg = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])

# Create second line of best fit


# Add labels and title


# Save plot and return data for testing (DO NOT MODIFY)
plt.savefig('sea_level_plot.png')


'''def draw_plot():
    # Read data from file


    # Create scatter plot


    # Create first line of best fit


    # Create second line of best fit


    # Add labels and title

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

draw_plot()'''