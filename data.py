# Para leer un archivo LAS 
import os
import pandas as pd
import numpy as np
import lasio

las = lasio.read("data_01JAN2014_18JAN2015.las")

# Para mostrar las claves del directorio usamos keys
las.keys()

# Convertimos a dataframe
df = las.df()

df.columns

df.head()