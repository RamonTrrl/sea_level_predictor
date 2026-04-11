import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

#creamos del data frame
df = pd.read_csv('epa-sea-level.csv')
print(df.head())

#creamos la función
def draw_plot():
    fig, ax = plt.subplots(figsize=(10, 6))

    #puntos de dispersión
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='black', alpha=0.5)

    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    
