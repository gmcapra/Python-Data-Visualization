"""
Pandas Built-in Data Visualization 
---------------------------------------------------------------------------------------------
Gianluca Capraro
Created: April 2019
---------------------------------------------------------------------------------------------
This script contains examples demonstrating the use of the Pandas library to
visualize data. The data used in this script is artificially created.

The following plot types will be created using Pandas:
- Area Plots
- Bar Plots
- Histograms
- Scatter Plots
- Box Plots
- Hexagonal Bin Plots
- Kernel Density Estimation Plots (KDE)

Many of the plots created with Pandas can also accept additional arguments
of their parent matplotlib plt. call. Refer to Matplotlib and Pandas documentation
for additional parameters.
---------------------------------------------------------------------------------------------
Matplotlib style sheets can be used to create a set of rules for create plots
to follow, giving all plots the same look and feel.

Link to Matplotlib Style Sheets:
https://matplotlib.org/gallery.html#style_sheets
---------------------------------------------------------------------------------------------
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read in dataframes from artificially created csv data files
df1 = pd.read_csv('df1.csv',index_col = 0)
df2 = pd.read_csv('df2.csv')

#print head for each file
print('DF1:')
print('\n')
print(df1.head())
print('\n')

print('DF2:')
print('\n')
print(df2.head())
print('\n')


"""
---------------------------------------------------------------------------------------------
Area Plots
- can take in entire dataframe or individual x,y column arguments
---------------------------------------------------------------------------------------------
"""
print('Showing Example Area Plot...')
df2.plot.area(alpha=0.4)
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------------
Bar Plots
- can take in entire data frame or individual x,y column arguments
---------------------------------------------------------------------------------------------
"""
print('Showing Example Bar Plot...')
df2.plot.bar(stacked = True)
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------------
Histograms
- takes in one column of a data set
---------------------------------------------------------------------------------------------
"""
print('Showing Example Histogram...')
df1['A'].plot.hist(bins=50)
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------------
Scatter Plots
- takes in individual x and y parameters
- takes in cmap for color, and s for point size based on column C
---------------------------------------------------------------------------------------------
"""
print('Showing Example Scatter Plot...')
df1.plot.scatter(x='A',y='B')
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------------
Box Plots
- takes in entire data frame
- can use the by= argument to groupby
---------------------------------------------------------------------------------------------
"""
print('Showing Example Box Plot...')
df2.plot.box()
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------------
Hexgonal Bin Plots
- takes in two x and y column parameters
- in this example we will plot a hex bin for a random data set
---------------------------------------------------------------------------------------------
"""
print('Showing Example Hexgonal Bin Plot...')
rand_df = pd.DataFrame(np.random.randn(500, 2), columns=['X', 'Y'])
rand_df.plot.hexbin(x='X',y='Y',gridsize=25,cmap='Greens')
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------------
Kernel Density Estimation Plots
- takes in column of data and estimates kernel density
- can also take in entire dataframe
---------------------------------------------------------------------------------------------
"""
print('Showing Example KDE Plot for Column a, DF2...')
df2['a'].plot.kde()
plt.show()
print('\n')

print('Showing Example KDE Plot for DF2...')
df2.plot.density()
plt.show()
print('\n')

"""
---------------------------------------------------------------------------------------------
Style Sheets with Matplotlib and Pandas
- Demonstrate 3 different styles that can be used with Pandas
---------------------------------------------------------------------------------------------
"""

#ggplot
plt.style.use('ggplot')
print('ggplot style example...')
df1['A'].hist()
plt.show()
print('\n')

#dark_background
plt.style.use('dark_background')
print('dark_background style example...')
df1['A'].hist()
plt.show()
print('\n')

#fivethirtyeight
plt.style.use('fivethirtyeight')
print('fivethirtyeight style example...')
df1['A'].hist()
plt.show()
print('\n')













