"""
Matrix Plots - Using Seaborn and Python to Visualize Datasets
-----------------------------------------------------------------------------
Gianluca Capraro
Created: April 2019
-----------------------------------------------------------------------------
This script will demonstrate the use of the Seaborn, Matplotlib, and Numpy
libraries to load, manipulate, and visualize data with Python.

The data that will be used is loaded from Seaborn's publicly available data. 
In this script we will be using the 'tips' and 'flights' data sets.

tips - contains data related to restaurant bills, the associated tip, party size,
paying customer's gender, their status as a smoker, the day, and time.

flights - contains year, month, and number of passengers data.

The examples demonstrate use of:
- Matrix Plots

Types of matrix plots we will plot with Seaborn are:
--------------------------------------------------------------------------------------------------------------------------------
- heatmaps
- clustermaps

For all method parameters, refer to Seaborn official documentation.
--------------------------------------------------------------------------------------------------------------------------------
"""

#import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

#load the datasets
tips_data = sns.load_dataset('tips')
flights_data = sns.load_dataset('flights')

#print out the head of the data sets to terminal to understand columns
print('\nTips Dataset Head:')
print(tips_data.head())
print('\n')

print('Flights Dataset Head:')
print(flights_data.head())
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Heatmaps - show matrix representation of correlation between data points
	 - to work properly, data should be in matrix form prior to seaborn plotting
	 - the corr() method can be useful here, as it returns the matrix form for correlation data
--------------------------------------------------------------------------------------------------------------------------------
"""
#get the matrix data using tips_data.corr()
tips_matrix_data = tips_data.corr()

#print this matrix
print('Tips Correlation Matrix:')
print(tips_matrix_data)
print('\n')

#now, we can create a heatmap simply by calling its method with seaborn
#by adding the cmap parameter, we can change the color scheme
#by adding the annot boolean parameter we can change its annotation
print('Showing Tips Data Heatmap...')
sns.heatmap(tips_matrix_data, cmap = 'coolwarm', annot = True)
plt.title('Tips Data Heatmap')
plt.show()
print('\n')


#now, let's look at the flights data
#using this data set, we can use a pivot table to get our data in matrix form
#we want each Month as the rows, and each year as the columns
#this way, we can easily find the number of passengers at every cell
flights_matrix_data = flights_data.pivot_table(values='passengers',index='month',columns='year')

#print this matrix
print('Flights Matrix Data:')
print(flights_matrix_data)
print('\n')

#call heatmap with seaborn, and this data can be beautifully visualized
#with this map, you can easily track the busiest and slowest months for flying within that time period
#adding in linecolor, and linewidths parameters can futher refine this map
print('Showing Flights Data Heatmap...')
sns.heatmap(flights_matrix_data, cmap = 'coolwarm', linecolor='white',linewidths=3)
plt.title('Flights Data Heatmap')
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Clustermaps - use clustering to produce a grouped version of the heatmap
--------------------------------------------------------------------------------------------------------------------------------
"""
#call the clustermap on the flights data
#now, we can see similar months being grouped together
print('Showing Clustermap of Flights Data...')
sns.clustermap(flights_matrix_data, cmap='coolwarm',standard_scale=1)
plt.title('Flights Data Clustermap')
plt.show()
print('\n')


"""
Conclusion
--------------------------------------------------------------------------------------------------------------------------------
This script has demonstrated the use of seaborn and python to transform data into matrix form and create heat and cluster maps.
--------------------------------------------------------------------------------------------------------------------------------
"""
