import os
import pandas as pd
cwd = os.path.abspath(r'Location of files in a folder') 
files = os.listdir(cwd)  


df = pd.DataFrame()
for file in files:
    if file.endswith('.xls'):
        df = df.append(pd.read_excel(file), ignore_index=True, sort=True) 
df.head() 
df.to_excel('Combined.xls')
