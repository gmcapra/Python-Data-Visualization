"""
Distribution Plots - Using Seaborn and Python to Visualize Datasets
-----------------------------------------------------------------------------
Gianluca Capraro
Created: April 2019
-----------------------------------------------------------------------------
This script will demonstrate the use of the Seaborn, Matplotlib, and Numpy
libraries to load, manipulate, and visualize data with Python.

The data that will be used is loaded from Seaborn's publicly available data.
It contains data related to restaurant bills, the associated tip, party size,
paying customer's sex, their status as a smoker, the day, and time.

The examples contained in this script will demonstrate use of:
- Distribution Plots

Types of distribution plots available in Seaborn are:
-----------------------------------------------------------------------------
- distplot(col of data, num bins, histogram bool, kde bool, etc.)
- jointplot(x col, y col, dataset, kind, color, dropna)
	- kind could be 'scatter','reg','resid', 'kde', 'hex'
- pairplot(data, hue, hue_order, palette)
- rugplot(col of data, height, axis)
- kdeplot(data, second set of data, shade bool, vertical bool)

For all method parameters, refer to Seaborn official documentation.
-----------------------------------------------------------------------------
"""

#import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#load the dataset
tips_data = sns.load_dataset('tips')

#print out the head of the data to terminal to understand columns
print('\nTips Dataset Head:')
print(tips_data.head())
print('\n')


"""
----------------------------------------------------------------------------
Distplots - useful for analyzing feature distributions
----------------------------------------------------------------------------
"""
#create a distribution plot of the total bill data with only the data parameter
print('Showing Distribution of Total Bill...')
sns.distplot(tips_data['total_bill'])
plt.show()
print('\n')

#create a distribution plot without the kde layer, show only the histogram, add more bins
#add a title and x label to the plot
print('Showing Histogram of Total Bill data, KDE=False...')
sns.distplot(tips_data['total_bill'], kde=False, bins=30)
plt.title('Distribution of Total Bills')
plt.xlabel('Total Bill ($)')
plt.show()
print('\n')


"""
----------------------------------------------------------------------------
Jointplots - useful for comparing two different data features
----------------------------------------------------------------------------
"""
#create a jointplot, scatter kind, comparing total bill on x axis to the tip amount on y axis
print('Showing Jointplot of Total Bill vs. Tip Amount...')
sns.jointplot(x='total_bill',y='tip',data=tips_data,kind='scatter')
plt.show()
print('\n')

#repeat this type of plot, however this time change the kind type to 'hex'
print('Showing Jointplot (Hex) of Total Bill vs. Tip Amount...')
sns.jointplot(x='total_bill',y='tip',data=tips_data,kind='hex')
plt.show()
print('\n')

#this time change the kind type to 'reg'
print('Showing Jointplot (Linear Reg) of Total Bill vs. Tip Amount...')
sns.jointplot(x='total_bill',y='tip',data=tips_data,kind='reg')
plt.show()
print('\n')


"""
----------------------------------------------------------------------------
Pairplot - useful for analyzing all relationships in data quickly
----------------------------------------------------------------------------
"""
#create a pairplot of all relationships in tips data
print('Showing Pairplot of Tips Dataset...')
sns.pairplot(tips_data)
plt.show()
print('\n')

#create the same pairplot, however segment this data based on gender
#use the palette parameter to adjust the color scheme
#change diagonal kind to show histograms
print('Showing Pairplot of Tips Dataset Segmented by Gender...')
sns.pairplot(tips_data, hue = 'sex', palette = 'coolwarm', diag_kind = 'hist')
plt.show()
print('\n')


"""
----------------------------------------------------------------------------
Rugplot - show a dash mark for every point on a univariate distribution
		- a building block of the KDE plot shown later
----------------------------------------------------------------------------
"""
#create a rugplot 
print('Showing Rugplot of Total Bills...')
sns.rugplot(tips_data['total_bill'])
plt.title('Rugplot of Total Bills')
plt.xlabel('Total Bill ($)')
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------
KDE Plot - kernel density estimation plot
		 - replace every observation of data with normal distribution around that value
---------------------------------------------------------------------------------------
"""
#create a kde plot with seaborn 
print('Showing KDE Plot of Total Bills...')
sns.kdeplot(tips_data['total_bill'])
plt.title('KDE Plot of Total Bills')
plt.xlabel('Total Bill ($)')
plt.show()
print('\n')

#show rugplot with the kde plot to visualize their relationship
print('Showing KDE and Rug Plots of Total Bills...')
sns.kdeplot(tips_data['total_bill'])
sns.rugplot(tips_data['total_bill'])
plt.title('KDE and Rug Plots of Total Bills')
plt.xlabel('Total Bill ($)')
plt.show()
print('\n')

#show the same, but for data related to tip amount
print('Showing KDE and Rug Plots of Tip Amounts...')
sns.kdeplot(tips_data['tip'])
sns.rugplot(tips_data['tip'])
plt.title('KDE and Rug Plots of Tip Amounts')
plt.xlabel('Tip Amount ($)')
plt.show()
print('\n')


"""
---------------------------------------------------------------------------------------
CONCLUSION
---------------------------------------------------------------------------------------
In this script we have demonstrated how Seaborn can be used with Python to read data
and create several different 'kinds' of distribution plots.
---------------------------------------------------------------------------------------
"""
