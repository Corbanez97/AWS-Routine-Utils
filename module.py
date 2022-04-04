import pandas as pd

df = pd.read_csv('data/raw_data.csv')

mapper = {'column1':'name', 'column2':'age', 'column3':'job'}

df.rename(columns = mapper, inplace = True)

df.to_csv('data/clean_data.csv', index = False)