import pandas as pd

# Cargar el dataset (asegúrate de que el archivo esté en el mismo directorio)
df = pd.read_csv('Dataset_UFO-Sanchez.csv')

# Mostrar las primeras filas del dataset
print("Primeras filas del dataset original:")
print(df.head())

# Filtrar datos de ejemplo (cambia la condición según tu dataset)
df_filtered = df[df['Country'] == 'USA']

# Guardar el dataset modificado en un archivo nuevo
df_filtered.to_csv('Dataset_UFO_Sanchez_filtered.csv', index=False)

print("El dataset filtrado ha sido guardado como 'Dataset_UFO_Sanchez_filtered.csv'.")
