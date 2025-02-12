import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('Projects/SeaLevelPredictor/epa-sea-level.csv')


    # Create scatter plot
    x=df['Year']
    y=df['CSIRO Adjusted Sea Level']

    fig, ax = plt.subplots()
    plt.scatter(x, y)

    # Create first line of best fit
    res = linregress(x,y)

    x_res = pd.Series([i for i in range(1880,2051)])
    y_res = res.intercept + res.slope*x_res
    plt.plot(x_res, y_res, 'r')

    # Create second line of best fit
    df2 = df.loc[df['Year'] > 1999]
    x2 = df2['Year']
    y2 = df2['CSIRO Adjusted Sea Level']
    res2 = linregress(x2,y2)
    x_res2 = pd.Series([i for i in range(2000,2051)])
    y_res2 = res2.intercept + res2.slope*x_res2
    plt.plot(x_res2, y_res2, 'g')


    # Add labels and title
    ax.set_title('Rise in Sea Level')
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()