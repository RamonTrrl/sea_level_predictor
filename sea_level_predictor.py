import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

# Cargar datos
df = pd.read_csv('epa-sea-level.csv')
print(df.head())  # puedes borrar esta línea después de verificar

def draw_plot():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Gráfico de dispersión (puntos negros)
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='black', alpha=0.5)
    
    # --- Primera línea de regresión (todos los datos) ---
    slope_all, intercept_all, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051, 1)   # desde 1880 hasta 2050
    line_all = slope_all * years_all + intercept_all
    ax.plot(years_all, line_all, color='blue', label='Best fit line (1880-2013)')
    
    # --- Segunda línea de regresión (desde el año 2000) ---
    df_recent = df[df['Year'] >= 2000]   # CORREGIDO: 2000, no 200
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051, 1)
    line_recent = slope_recent * years_recent + intercept_recent
    ax.plot(years_recent, line_recent, color='red', label='Best fit line (2000-2013)')
    
    # Etiquetas y título
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    
    # Leyenda y rejilla
    ax.legend()
    ax.grid(True, linestyle='--', alpha=0.5)
    
    # Guardar y devolver
    fig.savefig('sea_level_plot.png')
    return fig

if __name__ == "__main__":
    draw_plot()
    print("Gráfico guardado como 'sea_level_plot.png'")
