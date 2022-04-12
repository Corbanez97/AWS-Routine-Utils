import pandas as pd
import json
import os

def linearization(raw: dict, non_relational: list) -> pd.DataFrame:
    
    '''
    This function takes dict with the shape of said data
    and transforms it into a DataFrame by linearazing its keys, subkeys, and values
    to a single [{column -> value}, ... , {column -> value}] list.

            Parameters:
                    raw (dict): A dictionary with nested dictionaries where we find values;
                    non_relational (list): List of keys to ignore. Mainly because said data is not relational.

            Returns:
                    pd.DataFrame.from_dict(index, orient = 'index') (pandas.DataFrame): Dataframe from linearized dict.
    '''
    
    
    prime = list(raw.keys())[0]
    idx = 1
    index = {}
    for sup in raw:
        temp = {}
        for key in raw[sup]:
            if key in non_relational:
                pass
            else:
                value = raw[sup][key]
                if isinstance(value, list):
                    value = value[0]
                    for sec_key in value:
                        if sec_key == 'source':
                            pass
                        else:
                            temp[key + '_' + sec_key] = value[sec_key]
                    index[idx] = temp
        idx += 1
                    
    return pd.DataFrame.from_dict(index, orient = 'index')

def merger(directory: str) -> dict:
    '''
    Import a series of .JSON files with a prime key as a dict,
    and merges them into one dict with this set of keys.

            Parameters:
                    directory (str): Directory with a collection of .JSON files to be imported and merged.

            Returns:
                    temp (dict): A dictionary with all data from those .JSON concatenated.
    '''
    
    files = os.listdir(directory)
    
    temp = {}
    
    for file in files:
        if file[-5::] != '.json':
            continue
        f = directory + r'/' + file
        with open(f, 'r') as j:
            raw = json.loads(j.read())
        temp[list(raw.keys())[0]] = raw[list(raw.keys())[0]]
    
    return temp

def main(parent: str, dump: str, ignore: list) -> None:
    
    raw = merger(parent)

    df = linearization(raw, ignore)

    df.to_csv(dump, index = False)

    return None