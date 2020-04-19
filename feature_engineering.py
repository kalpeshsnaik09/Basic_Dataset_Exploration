import pandas as pd
import numpy as np

def unique_eliminate(df,col):
    '''
        identify the unique value columns of all value or only one value

        param:
            df  :   dataframe
            col :   column name

        return:
            boolean 
    '''
    assert isinstance(df,pd.DataFrame),'Enter only Pandas DataFrame.'
    assert isinstance(col,str),'Enter Column Name in String Type.'
    assert col in df.columns,'Column Must Present in DataFrame.'

    df_len=len(df) #df.shape[0]
    col_unique=df[col].nunique()
    if col_unique == 1 or col_unique == df_len:
        return True
    return False

def max_unique(df,col,dtype,threshold):
    '''
        identify the unique value columns of 90% for catogarical column or 
        0.1 variance for numerical column

        param:
            df          :   dataframe
            col         :   column name
            dtype       :   column dtype(catogarical/numerical)
            threshold   :   threshold 

        return:
            boolean 
    '''
    assert isinstance(df,pd.DataFrame),'Enter only Pandas DataFrame.'
    assert isinstance(col,str),'Enter Column Name in String Type.'
    assert col in df.columns,'Column Must Present in DataFrame.'
    assert isinstance(threshold,float),'Enter Threshold Between 0 & 1.'
    assert dtype in ['cat','num'],'Please Enter \'cat\' for Categorical and \'num\' for Numerical'

    if dtype=='cat':
        value_count=df[col].value_counts(normalize=True)
        if len(value_count[value_count>threshold])>0:
            return True
    else:
        assert col in df.describe(exclude='object').columns,'Give only Numerical dtype Column'
        if df[col].var()<=threshold:
            return True
    return False