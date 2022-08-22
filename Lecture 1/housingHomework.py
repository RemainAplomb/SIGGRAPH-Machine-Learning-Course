"""
    Name: Rahmani Dibansa
    Date: 22nd of August 2022
    Description:
        This python program is for the homework on the Lecture 1
    Homework:
        Play with the data, try other plots
    Reference(s):
        ACMSIGGRAPH. SIGGRAPH Now | Hands-on Workshop: Machine Learning and Neural Networks – Lecture 1
        Retrieved from: https://www.youtube.com/watch?v=gfY2LfRfE1E&list=PLUPhVMQuDB_b2kcOooEduedthcBH53mvC
"""


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

# Plot 1
# In this plot, it shows the population size of the given area
# depending on the latitude and longitude. By looking at this graph
# We can see where the population hotspots are.
sns.relplot(x='latitude', y='longitude', size='population', alpha=0.5, palette='muted', data=csvData)


# Plot 2
# In this plot, the median income will be plotted.
# We can infer from this graph that the highest earners are concentrated
# on particular places. These places could either be comercial hotspots
# or has high standard of living
sns.relplot(x='latitude', y='longitude', size='median_income', alpha=0.5, palette='muted', data=csvData)

# Plot 3
# In this plot, I have a sample of 2500
# and I would like to see how that will affect the
# representation of the median_house_value on a place
sns.relplot(x='latitude', y='longitude', size='median_house_value', alpha=0.5, palette='muted', data=csvData.sample(n=2500))

# Plot 4
# In this graph, I used a sample of 5000
# and used 6 features. As such, it produced 36 graphs.
sns.pairplot(csvData.sample(n= 5000)[['longitude', 'latitude', 'total_bedrooms', "total_rooms" , 'median_house_value', 'population']])


# Show the plotted features
# Set block to False to prevent the plot from closing immediately after the program terminates
plt.show(block=False)
