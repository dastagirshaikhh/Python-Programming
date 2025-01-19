# setting the working directory
import numpy as np
import pandas as pd
import os
from statistics import median
# os.chdir("C:\\Users\\dasta\\OneDrive\\Documents\\Data Science Tabular sheets")


df1 = pd.read_csv("C:\\Users\\dasta\\Documents\\Data Science Tabular sheets\\tips.csv")
print('\n', df1)  # displays the file

print('\n', df1.head())  # displays first 5 rows excluding index

print('\n', df1.tail())  # displays last five rows

print('\n', df1.head(3))  # displays a specific rows from beginning columns

print('\n', df1.tail(2))  # displays a specific rows from last columns

print('\n', len(df1))  # displays the total number of rows

print('\n', df1.columns)  # displays all the columns

print('\n', len(df1.columns))  # displays total number of columns

print('\n', df1.info())  # displays the information of the file

# pd.set_option('max_rows',1)
# print (df1) #displays all the rows

# displays the understanding of the numerical columns
print('\n', df1.describe())

df1 = df1.rename(columns={"sex": "gender", "size": "customers", })
# OR
df1.rename(columns={"total bill": "total_bill"}, inplace=True)
print('\n', df1)  # used to rename columns

print('\n', df1.total_bill)  # displays a specific coloumn

print('\n', df1.iloc[0:11, 0:3])
print('\n', df1.iloc[8:23, :])
print('\n', df1.iloc[100:, 2:5])
print('\n', df1.iloc[[0, 10, 20, 30, 40, 50, 60,
      70, 80, 90, 100, 200, 243], [0, 2, 4, 6]])
# displays specific rows & columns [SLICING OF DATAFRAME]

print("\n", df1.iloc[[0, 10, 20, 30, 40, 50, 60, 70,
      80, 90, 100, 200, 243], [0, 2, 4, 6]].values)
# displays in the form of array
# <<<<<<<<<<<<<<<------------------------------------------------->>>>>>>>>>>>>>>>>>>>>

# Filtering the data

print('\n', df1[(df1["gender"] == "Female") & (df1["tip"] >= 5)])
print('\n', df1[(df1["gender"] == "Male") & (df1["tip"] >= 5)])
# OR
# displays both male and female no need to add extra
print('\n', df1[(df1["gender"] == "Male") | (df1["tip"] >= 5)])

print('\n', df1[(df1["gender"] == "Male") & (df1["smoker"] == "Yes")])
print('\n', df1[(df1["gender"] == "Female") & (df1["smoker"] == "Yes")])
print('\n', df1[(df1["gender"] == "Male") & (df1["time"] == "Dinner")])
print('\n', df1[(df1["gender"] == "Male") & (df1["time"] == "Lunch")])
print('\n', df1[(df1["gender"] == "Female") & (df1["time"] == "Dinner")])
print('\n', df1[(df1["gender"] == "Female") & (df1["time"] == "Dinner")])

# Grouping the data

group = df1.groupby('gender').size()
print('\n', group)
group2 = df1.groupby(['gender', 'smoker']).size()
print('\n', group2)

print('\n', df1.groupby('gender').agg(
    {'total_bill': np.mean, 'tip': np.mean, 'customers': np.mean}))
print('\n', df1.groupby('gender').agg(
    {'total_bill': sum, 'tip': np.sum, 'customers': np.sum}))
print('\n', df1.groupby('gender').agg(
    {'total_bill': np.median, 'tip': np.median, 'customers': np.median}))
print('\n', df1.groupby('gender').agg(
    {'total_bill': np.average, 'tip': np.average, 'customers': np.average}))
# Calculating the mean median sum average etc by grouping the columns

# Overwriting the content in Data Frame
df1['Smoking_Charges'] = df1.smoker.astype(str) == 'Yes'
# Creating an another column for eligibility
df1['Smoking_Charges'] = df1.Smoking_Charges.map({False: "No", True: "Yes"})
# Overwriting the boolean value in the column with string
print('\n', df1)
