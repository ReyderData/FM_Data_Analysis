#IMPORTS
import pandas as pd
from bs4 import BeautifulSoup
import numpy as np
import seaborn as sb
import matplotlib as plt
import csv
import os
import sys
  
#FILES NAMES
#In this case I have all in the same directory, if not, will be required to pass the full path
#HTML
html = "prueba.html"
#CSV
csv_file = "prueba.csv"
#EXCEL
excel_file = "prueba_excel.xlsx"



# Select the only (first) table using indexing [0]; encoding added cause was getting errors instead
df = pd.read_html(os.path.join(sys.path[0], html), encoding='utf8')[0]
# Write DataFrame to CSV - no index required
df.to_csv(csv_file, index=False)
print(df.head())

#Create an output excel file | tests with this but currently not working
#resultExcelFile = pd.ExcelWriter('D:\\IGNACI_STUFF\\FOOTBALL\\Data_Analyst\\MONEYBALL\\FM_PYTHON_MONEYBALL\\players_data.xlsx')
#resultExcelFile = pd.ExcelWriter('players_data.xlsx')

df_csv = pd.read_csv(csv_file)
print(df_csv.head(2))
# I was using this method but changed to the bottom one because now I am passing it the variable instead of path string
#df_csv.to_excel (r'excel_file.xlsx', index = None, header=True)

#Converting csv to excel file
df_csv.to_excel(excel_file,'Players data',index=None, header=True)
