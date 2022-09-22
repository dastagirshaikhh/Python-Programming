import seaborn as sns
import matplotlib.pyplot as plt
from itertools import groupby
import pandas as pd
import os
# Setting the working directory
os.chdir("C:\\Users\\dasta\\OneDrive\\Documents\\Data Science Tabular sheets")
df = pd.read_csv("Car_sales.csv")  # Displaying the data
print(df)


for group, data in df.groupby('Manufacturer'):
    # printing the mean value of a column by grouping columns
    print(group, data['4-year resale value'].mean())

# Printing the average in the form of Horizontal Bar Graph
for group, data in df.groupby('Manufacturer'):
    plt.barh('\n', group, data['4-year resale value'].mean())
