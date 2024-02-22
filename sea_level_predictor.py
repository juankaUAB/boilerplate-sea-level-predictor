import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot

    fig, ax = plt.subplots()
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    

    # Create first line of best fit

    lin1 = linregress(df['Year'], y=df['CSIRO Adjusted Sea Level'])
    plt.plot(range(1880, 2051), [lin1.slope * i + lin1.intercept for i in range(1880, 2051)])

    # Create second line of best fit

    lin2 = linregress(df.loc[df['Year'] >= 2000]['Year'], y=df.loc[df['Year'] >= 2000]['CSIRO Adjusted Sea Level'])
    plt.plot(range(2000, 2051), [lin2.slope * i + lin2.intercept for i in range(2000, 2051)])

    # Add labels and title
    
    ax.set_title("Rise in Sea Level")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_xlabel("Year")
    ax.set_xlim(1850, 2075)

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()