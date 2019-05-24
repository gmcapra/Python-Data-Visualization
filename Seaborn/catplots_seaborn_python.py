"""
Categorical Plots - Using Seaborn and Python to Visualize Datasets
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
- Categorical Plots

Types of categorical plots available in Seaborn are:
--------------------------------------------------------------------------------------------------------------------------------
- factorplot()
- boxplot()
- violinplot()
- stripplot()
- swarmplot()
- barplot()
- countplot()

For all method parameters, refer to Seaborn official documentation.
--------------------------------------------------------------------------------------------------------------------------------
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
--------------------------------------------------------------------------------------------------------------------------------
Bar and Count Plots - allow aggregation of data off of a categorical feature
					- aggregate function defaults to mean()
					- this estimator object can be changed to another function (vector->scalar)
--------------------------------------------------------------------------------------------------------------------------------
"""

#create a barplot of the total_bill column of data
print('Showing Barplot of mean total bill by gender...')
sns.barplot(x='sex',y='total_bill',data=tips_data)
plt.title('Mean Total Bill by Gender')
plt.show()
print('\n')

#create a barplot of total bill by gender, use the standard deviation estimator from numpy
print('Showing Barplot of the standard deviation of total bill by gender...')
sns.barplot(x='sex',y='total_bill',data=tips_data, estimator = np.std)
plt.title('Standard Deviation of Total Bill by Gender')
plt.show()
print('\n')

#a count plot is the same as a barplot, except the estimator explicitly counts the num of occurrences
#create a countplot of the number of males and females
print('Showing Number of Males vs. Females in the Tips Dataset...')
sns.countplot(x='sex',data=tips_data)
plt.title('Number of Males vs. Females in the Tips Dataset')
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Box and Violin Plots - used to show distribution of categorical data
					 - box plot shows distribution of quantitative data
					 - violin plot features a kernel density estimation of underlying distribution
--------------------------------------------------------------------------------------------------------------------------------
"""
#create a box plot showing the distribution of total_bill amounts by the day of the week
print('Showing Boxplot of Total Bill by Day of Week...')
sns.boxplot(x='day',y='total_bill',data=tips_data,palette='coolwarm')
plt.title('Boxplot of Total Bill by Day of Week')
plt.show()
print('\n')

#use the orient parameter = h to do a boxplot of the entire dataframe
#this shows the total_bill, tip, and party size distributions for the entire dataset
print('Showing Boxplot of Entire DataFrame...')
sns.boxplot(data=tips_data,palette='coolwarm', orient = 'h')
plt.title('Boxplot of Tips Dataset')
plt.show()
print('\n')

#create a box plot showing the distribution of total_bill amounts by the day of the week
#segment this data by the smoking status of the person who paid
print('Showing Boxplot of Total Bill by Day of Week, Segmented by Smoker...')
sns.boxplot(x='day',y='total_bill', hue = 'smoker',data=tips_data,palette='coolwarm')
plt.title('Boxplot of Total Bill by Day of Week, Segmented by Smoker')
plt.show()
print('\n')

#create a violin plot of the same data
print('Showing Violinplot of Total Bill by Day of Week...')
sns.violinplot(x='day', y='total_bill', data=tips_data,palette='rainbow')
plt.title('Violinplot of Total Bill by Day of Week')
plt.show()
print('\n')

#create a violin plot of the same data, segmented by gender
#include paramter (split = True) to see this a little differently
print('Showing Violinplot of Total Bill by Day of Week, Segmented by Gender...')
sns.violinplot(x='day', y='total_bill', hue = 'sex',data=tips_data,palette='rainbow')
plt.title('Violinplot of Total Bill by Day of Week, Segmented by Gender')
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Strip and Swarm Plots - stripplot will draw a scatter plot with one categorical variable
					  - strip plot can be drawn on its own, also a good complement to box or violin plots
					  - good for showing underlying distribution

					  - swarmplot is similar, but points are adjusted so they do not overlap
					  - provides a better representation for distribution of values
					  - does not scale as well to large numbers of observations (both computationally and aesthetically)
--------------------------------------------------------------------------------------------------------------------------------
"""
#create a stripplot of the day of the week vs. the total bill amount
print('Showing Stripplot of Day vs. Total Bill Amount...')
sns.stripplot(x='day', y='total_bill', data= tips_data, palette = 'Set2')
plt.title('Stripplot of Day vs. Total Bill Amount')
plt.show()
print('\n')

#create a stripplot of the day of the week vs. the total bill amount with jitter
#separate by male and female
#set split = True for better visualization
print('Showing Stripplot of Day vs. Total Bill Amount, Segmented by Gender...')
sns.stripplot(x='day', y='total_bill', data= tips_data, jitter = True, hue = 'sex', split = True, palette = 'Set2')
plt.title('Stripplot of Day vs. Total Bill Amount, Segmented by Gender')
plt.show()
print('\n')

#create a swarmplot of the same data
print('Showing Swarmplot of Day vs. Total Bill Amount...')
sns.swarmplot(x='day', y='total_bill', data= tips_data, palette = 'Set2')
plt.title('Swarmplot of Day vs. Total Bill Amount')
plt.show()
print('\n')

#create another swarmplot, segmented by gender, and split = True for visualization
print('Showing Swarmplot of Day vs. Total Bill Amount, Segmented by Gender...')
sns.swarmplot(x='day', y='total_bill', data= tips_data, hue = 'sex', split = True, palette = 'Set2')
plt.title('Swarmplot of Day vs. Total Bill Amount, Segmented by Gender')
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Combining Categorical Plots - to combine plots onto the same graph with seaborn, declare the plots prior to using plt.show()
--------------------------------------------------------------------------------------------------------------------------------
"""
# one effective plot combination can be created by combining the violin plot with the swarm plot
print('Showing Violin/Swarm plot combination, Tip Amount vs. Day of Week...')
sns.violinplot(x='tip', y='day', data=tips_data,palette='rainbow')
sns.swarmplot(x='tip', y='day', data=tips_data,color='black',size=3)
plt.title('Violin/Swarm plot combination, Tip Amount vs. Day of Week')
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Factorplot - the most general form of categorical plot
		   - can take in the 'kind' parameter to adjust plot type
--------------------------------------------------------------------------------------------------------------------------------
"""
#use the factorplot method to create a bar graph
print('Showing Use of Factorplot to create a bar graph...')
plt.title("Factorplot (kind = 'bar'), Total Bill Amount by Gender")
sns.factorplot(x='sex',y='total_bill',data=tips_data,kind='bar')
plt.show()
print('\n')


"""
--------------------------------------------------------------------------------------------------------------------------------
Conclusion
--------------------------------------------------------------------------------------------------------------------------------
This script has demonstrated how Seaborn can be used to create categorical plots.
--------------------------------------------------------------------------------------------------------------------------------
"""







