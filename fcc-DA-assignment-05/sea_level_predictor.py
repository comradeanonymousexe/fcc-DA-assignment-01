#ref code
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],color ='blue',alpha=0.4,label='CSIRO Adjusted Sea Level' )


    # Create first line of best fit
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred = pd.Series(range(int(df['Year'].min()), 2051))
    y_pred = slope * x_pred + intercept
    plt.plot(x_pred, y_pred, color="red", linestyle="dotted", linewidth=4, label="Best Fit Prediction - All Years")

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    slope2, intercept2, r_value, p_value, std_err = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = slope2 * x_pred2 + intercept2
    plt.plot(x_pred2, y_pred2, color="red", label="Best Fit Prediction - Recent Years")

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    plt.legend()
    plt.show()

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

