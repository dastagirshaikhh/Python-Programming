import os
from re import A
import pandas as pd

# Dictionary 1
stu_details = {"id": [1, 2, 3, 4, 5, 6], "Name": ['Dastagir', 'Zeeshan', 'Saud',
                                                  'Shahzeb', 'Shifa', 'Shafiya'], "Region": ['S', 'N', 'W', 'E', 'N', 'W']}

# Dictionary 2
Intstu_details = {"id": [1, 2, 3, 4, 5, 6], "Name": ['Thompson', 'Mike', 'jack',
                                                     'John', 'Sara', 'Sofie'], "Region": ['USA', 'UK', 'CA', 'UK', 'UAE', 'USA']}

# Creating Data Frames
df1 = pd.DataFrame(stu_details)
df2 = pd.DataFrame(Intstu_details)

# Merging Data Frames and storing them in the varables
total = pd.concat([df1, df2]).reset_index().drop(columns='index')

# Printing Data Frames in the form of variable
print('\n', total)

# Saving Data frames in excel
import os
excelfile = 'my_data_sheet1.xlsx'
os.chdir("C:\\Users\\dasta\\OneDrive\\Documents\\Data Science Tabular sheets")
total.to_excel(excelfile)
