import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# make a pandas dataframe to read all the data from the csv file
df = pd.read_csv('CPI.csv', header=4)
# drop all the columns that we don't need
df = df.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
# drop the years 1960-2017
df = df.drop(df.iloc[:, 1:58], axis=1)

df = df.loc[df['Country Name'].isin(['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])]
# print(df)

df = df.set_index('Country Name')
df = df.transpose()
df = df.drop(df.index[5])
# sort alphabetically
df = df.sort_index()

# change the dataframe so years are a column, countries are a column, and CPI is a column
df = df.reset_index()
df = df.melt(id_vars=['index'], value_vars=['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])
df = df.rename(columns={'index': 'Year', 'variable': 'Country Name', 'value': 'CPI'})
df = df.sort_values(by=['Year', 'Country Name'])
df = df.reset_index(drop=True)
# print(df)
# print("GDP:\n")

# make a pandas dataframe for the GDP and do the same thing as above
df2 = pd.read_csv('GDP.csv', header=2)
df2 = df2.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
df2 = df2.drop(df2.iloc[:, 1:58], axis=1)
df2 = df2.loc[df2['Country Name'].isin(['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])]
df2 = df2.set_index('Country Name')
df2 = df2.transpose()
df2 = df2.drop(df2.index[6])
df2 = df2.drop(df2.index[5])
df2 = df2.sort_index()
df2 = df2.reset_index()
df2 = df2.melt(id_vars=['index'], value_vars=['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])
df2 = df2.rename(columns={'index': 'Year', 'variable': 'Country Name', 'value': 'GDP'})
df2 = df2.sort_values(by=['Year', 'Country Name'])
df2 = df2.reset_index(drop=True)
# print(df2)

df3 = pd.read_csv('GdpDeflator.csv', header=2)
df3 = df3.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
df3 = df3.drop(df3.iloc[:, 1:58], axis=1)
df3 = df3.loc[df3['Country Name'].isin(['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])]
df3 = df3.set_index('Country Name')
df3 = df3.transpose()
df3 = df3.drop(df3.index[6])
df3 = df3.drop(df3.index[5])
df3 = df3.sort_index()
df3 = df3.reset_index()
df3 = df3.melt(id_vars=['index'], value_vars=['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])
df3 = df3.rename(columns={'index': 'Year', 'variable': 'Country Name', 'value': 'GDP Deflator'})
df3 = df3.sort_values(by=['Year', 'Country Name'])
df3 = df3.reset_index(drop=True)
# print(df3)

df4 = pd.read_csv('Inflation.csv', header=2)
df4 = df4.drop(columns=['Country Code', 'Indicator Name', 'Indicator Code'])
df4 = df4.drop(df4.iloc[:, 1:58], axis=1)
df4 = df4.loc[df4['Country Name'].isin(['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])]
df4 = df4.set_index('Country Name')
df4 = df4.transpose()
df4 = df4.drop(df4.index[6])
df4 = df4.drop(df4.index[5])
df4 = df4.sort_index()
df4 = df4.reset_index()
df4 = df4.melt(id_vars=['index'], value_vars=['United Arab Emirates', 'United States', 'United Kingdom', 'China', 'Japan', 'India', 'Germany', 'France', 'Canada', 'Brazil', 'Colombia', 'Poland'])
df4 = df4.rename(columns={'index': 'Year', 'variable': 'Country Name', 'value': 'Inflation'})
df4 = df4.sort_values(by=['Year', 'Country Name'])
df4 = df4.reset_index(drop=True)
# print(df4)

# # combine the dataframes into one dataframe, making sure to match the years and countries
# CPI, GDP, Inflation each get their own column
df5 = pd.concat([df, df2['GDP'], df3['GDP Deflator'], df4['Inflation']], axis=1)
print(df5)
# output the dataframe to a csv file
df5.to_csv('Final.csv', index=False)