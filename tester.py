import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df1 = pd.read_csv('GdpDeflator.csv', header=2)
df1 = df1.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
df1 = df1.drop(df1.iloc[:, 1:58], axis=1)
df1 = df1.loc[df1['Country Name'].isin(['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])]
df1 = df1.set_index('Country Name')
df1 = df1.transpose()
df1 = df1.drop(df1.index[6])
df1 = df1.drop(df1.index[5])
df1 = df1.sort_index()
df1 = df1.reset_index()
df1 = df1.melt(id_vars=['index'], value_vars=['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])
df1 = df1.rename(columns={'index': 'Year', 'variable': 'Country Name', 'value': 'GDP Deflator'})
df1 = df1.sort_values(by=['Year', 'Country Name'])
df1 = df1.reset_index(drop=True)
print(df1)