

# Import the necessary packages
# pip install seaborn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# Read the data using the pandas package
# For this, I downloaded the csv file that was given
# in the Class 1- Housing.ipnyb
fileName = "california_housing_train.csv"

# Read the csv file, and add a separator
csvData = pd.read_csv( fileName, sep=",")

print( "\n======================================================================\n" )
# To better understand what is inside the csv data, try printing
# print( csvData)
print( " The CSV data that has been read: \n" )
print( csvData )


print( "\n======================================================================\n" )
# The csv_data is read as a matrix
# If you want to understand its shape, print the shape
# The csvData has 17000 columns and 9 rows
# The columns are:
#           - Index, Longitude, Latitude, Housing Median age,
#           - Total Rooms, Total Bedrooms, Population, Households,
#           - Median Income, and Median House Value
# The result tuple of the printed shape: (17000, 9)
# print( csvData.shape )
print( " The shape of the CSV data: ", csvData.shape )


print( "\n======================================================================\n" )
# Now check the first 5 data points in the csvData
# If you want to see a specific number of rows,
# send the number of rows to the head function.
# But if you leave it empty, the default is 5
# print( csvData.head() )
# print( csvData.head(8) )
print( " The first 8 rows: \n" )
print( csvData.head(8) )


print( "\n======================================================================\n" )
# To transpose the data, you can use the transpose function
# Basically, what this does is change the position of the column and rows
# So after transposing, the shape becomes (9, 17000)
# However, please be advised that using csvData.head().transpose().shape()
# doesn't work because the output csvData.head().transpose() is already
# a tuple. 
# print( csvData.head().transpose() )
print( " The transposed head: \n" )
print( csvData.head().transpose() )


print( "\n======================================================================\n" )
# For looking at the basic data stats of each column
# the describe function can be used.
# The describe will display the ----
#   count: number of rows in each column
#   mean: the mean value of each column (Average value)
#   std: the standard deviation
#   min: the minimum of the values present in the column
#   max: the maximum of the values present in the column
#   percentiles: this could be 25%, 50%, 75%, and 100%
# By default the lower percentile is 25 and the upper percentile is 75. The 50 percentile is the same as the median.
# print( csvData.describe() )
print( " Description of the CSV data: \n" )
print( csvData.describe() )


print( "\n======================================================================\n" )
# To display your desired features/columns,
# use csvData[ [ "desiredFeature1", "desiredFeature2" ]]
# print( csvData[ [ "total_rooms", "total_bedrooms", "median_house_value" ]])
print( " The data for 3 desired features: \n" )
print( csvData[ [ "total_rooms", "total_bedrooms", "median_house_value" ]])


print( "\n======================================================================\n" )
# To do a scatter plot, use the relplot function of seaborn
# and use your desired features as the values for x and y.
# To see the result. use the matplotlib.pyplot
sns.relplot(x='latitude', y='longitude', size='total_bedrooms', alpha=0.5, palette='muted', data=csvData)

# Use pairplot on 5 features
# This will output 25 graphs where each graph is a paired plot
# Another thing to note here is that the first 1000 rows will be used as data
sns.pairplot(csvData.head(1000)[['longitude', 'latitude', 'total_bedrooms', 'median_house_value', 'population']])


# This is the answer at the last part of the ipnyb file for Lecture 1
# The question was, why is the map messed up...
# My answer is : Because what was taken was the first 1000 rows from the data.
#
# Furthermore, since the provided code says csv_data.s1000
# but the proper format for taking the sample of a csv is csvData.sample( n = 1000 )
sns.pairplot(csvData.sample( n = 1000 )[['longitude', 'latitude', 'total_bedrooms', 'median_house_value', 'population']])

# Show the plotted features
# Set block to False to prevent the plot from closing immediately after the program terminates
plt.show(block=False)

