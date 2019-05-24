"""
Regression Plots - LMPLOT() - Using Seaborn and Python to Visualize Datasets
-----------------------------------------------------------------------------
Gianluca Capraro
Created: April 2019
-----------------------------------------------------------------------------
This script will demonstrate the use of the Seaborn, Matplotlib, and Numpy
libraries to load, manipulate, and visualize data with Python.

The data that will be used is loaded from Seaborn's publicly available data. 
In this script we will be using the 'tips' data set.

The examples contained in this script will demonstrate use of:
- Regression Plots, however this script will specifically cover 
	the use of the lmplot() method.

The lmplot() method in seaborn allows you to easily plot linear models,
it also allows the plots to be split and further classified based off features.

For all method parameters, refer to Seaborn official documentation.
--------------------------------------------------------------------------------------------------------------------------------
"""
#import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#load the iris and tips datasets
tips = sns.load_dataset('tips')

#print the head of the tips dataset to understand contents
print('\nTips Dataset Head:')
print(tips.head())
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
lmplot()
--------------------------------------------------------------------------------------------------------------------------------
"""
#create a linear regression plot for the total bill vs the tip amount using the tips dataset
#segment the data by gender and change the color palette
#change the marker style for each gender
#change the marker size using scatter_kws
print('Showing Lmplot of Total Bill vs. Tip Amount, Segmented by Gender...')
sns.lmplot(x='total_bill', y='tip', data=tips, hue='sex', palette = 'coolwarm', markers=['o','+'], scatter_kws={'s':20})
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Using lmplot() to create a feature segmented grid
--------------------------------------------------------------------------------------------------------------------------------
"""
#create a 2x2 grid 
#showing total bill vs. tip with one column for each gender
#showing one row for time lunch or dinner
print('Showing Lmplot of Total Bill vs. Tip Amount, Separating Plots by Gender and Time of Meal...')
sns.lmplot(x='total_bill',y='tip',data=tips, row='sex', col='time')
plt.show()
print('\n')

#create a 4x1 grid 
#showing total bill vs. tip with one column for each gender
#showing one row for time lunch or dinner
print('Showing Lmplot of Total Bill vs. Tip Amount, Separating Plots by Day, Segmenting by Gender...')
sns.lmplot(x='total_bill',y='tip',data=tips, col='day', hue='sex', palette = 'coolwarm', aspect= 0.5, height = 7)
plt.show()
print('\n')

































