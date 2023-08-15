import pandas as pd

def read_my_csv(path):
    
    # load data from csv file at path to pandas data frame
    df = pd.read_csv(path)
    
    # Rename columns using indices
    # Note: columns are 3 and 4 because Scope 3 saves TEK files with preamble 
    t = df.iloc[:,3]    # time (s)
    vol = df.iloc[:,4]  # voltage (V)
    
    return t,vol