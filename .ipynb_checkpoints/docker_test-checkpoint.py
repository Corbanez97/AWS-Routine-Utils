import pandas as pd

def df_renaming(df, mapper):
    df.rename(columns = mapper, inplace = True)
    
    return df

if __name__ == '__main__':
    
    df = pd.read_csv('data/raw_data.csv')
    mapper = {'column1':'name', 'column2':'age', 'column3':'job'}
    
    df_renaming(df, mapper)
    
    df.to_csv('data/clean_data.csv', index = False)