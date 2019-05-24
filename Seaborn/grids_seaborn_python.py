"""
Grids - Using Seaborn and Python to Visualize Datasets
-----------------------------------------------------------------------------
Gianluca Capraro
Created: April 2019
-----------------------------------------------------------------------------
This script will demonstrate the use of the Seaborn, Matplotlib, and Numpy
libraries to load, manipulate, and visualize data with Python.

The data that will be used is loaded from Seaborn's publicly available data. 
In this script we will be using the 'iris' data set and the 'tips' data set.

The examples contained in this script will demonstrate use of:
- Grids

Grids are general plots that allow the mapping of plot types to rows and columns of a grid.
Grids can be used to create similar plots that are separated by certain features.

Types of grids we will create with Seaborn are:
--------------------------------------------------------------------------------------------------------------------------------
- PairGrid()
- FacetGrid()
- JointGrid()
- pairplot() - this was covered in previous scripts and won't be used here

For all method parameters, refer to Seaborn official documentation.
--------------------------------------------------------------------------------------------------------------------------------
"""
#import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#load the iris and tips datasets
iris = sns.load_dataset('iris')
tips = sns.load_dataset('tips')

#print the head of the iris dataset to understand contents
print('\nIris Dataset Head:')
print(iris.head())
print('\n')

#print the head of the tips dataset to understand contents
print('\nTips Dataset Head:')
print(tips.head())
print('\n')

"""
--------------------------------------------------------------------------------------------------------------------------------
PairGrid - a subplot grid that is used to plot pairwise dataset relationships
--------------------------------------------------------------------------------------------------------------------------------
"""
#to help visualize what the pairgrid does, display the empty pairgrid on its own
print('Showing Empty PairGrid...')
sns.PairGrid(iris)
plt.show()
print('\n')

#to plot data on the grid, use the .map() function
print('Showing Iris PairGrid, Mapping Scatter Plots...')
to_map = sns.PairGrid(iris)
to_map.map(plt.scatter)
plt.show()
print('\n')

#the map function can be refined further into diag, upper, and lower sections
#map histograms to the diagonal, scatter plots to the upper portion, and kde plots to the lower diagonal
print('Showing Iris PairGrid, Mapping Scatter, Hist, KDE Plots...')
to_map = sns.PairGrid(iris)
to_map.map_upper(plt.scatter)
to_map.map_diag(plt.hist)
to_map.map_lower(sns.kdeplot)
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
FacetGrid - a general way to create plot grids based off features of the dataset
--------------------------------------------------------------------------------------------------------------------------------
"""
#using the tips dataset, create an empty facetgrid
#the columns should represent the 'time' data
#the rows should represent the 'smoker' data
print('Showing Empty FacetGrid For Tips Data...')
emptyfacetgrid = sns.FacetGrid(tips, col='time',row='smoker')
plt.show()
print('\n')

#now, we can simply map the data we want and the type of plot we want to this grid
#for this example, map the total bill distribution histogram
print('Showing FacetGrid For Tips Data, Mapping Total Bill Distribution...')
to_map = sns.FacetGrid(tips,col='time',row='smoker')
to_map.map(plt.hist, 'total_bill')
plt.show()
print('\n')

#going further, we can segment this data by gender and observe total bill vs. tip on each plot
print('Showing FacetGrid For Tips Data, Mapping Total Bill vs. Tips, Segmented by Gender...')
to_map = sns.FacetGrid(tips, col='time',  row='smoker',hue='sex')
to_map = to_map.map(plt.scatter, 'total_bill', 'tip').add_legend()
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
JointGrid - the general version of the jointplot() type grids
--------------------------------------------------------------------------------------------------------------------------------
"""
#create and display a joint grid comparing total bill to tip amount, show distribution plots and linear reg plots
print('Showing JointGrid For Tips Data, Plotting Total Bill vs. Tips Distribution...')
to_map = sns.JointGrid(x='total_bill',y='tip',data=tips)
to_map = to_map.plot(sns.regplot, sns.distplot)
plt.show()
print('\n')




