import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def basic_exploration(df):
    '''
    find basic informatipn of dataset 
    
    Params:
    --------
    Pandas Dataset

    return:
    --------
    None

    Print:
    --------
    print all exploration information

    '''

    # Rows and Columns (Shape)
    print('rows:{},columns:{}'.format(str(df.shape[0]),str(df.shape[1]))) 
    print('*'*50)

    # Information of Dataset
    print('information of dataset:\n',df.info()) 
    print('*'*50)

    # Null value Columns in Dataset
    null_df=pd.DataFrame(df.isnull().sum(),columns=['Count']) 
    print('null values column:\n',null_df[null_df['Count']>0])
    print('*'*50)

    # Descriptive Statistics of Dataset
    try:
        print('Decriptive Statistics of Numerical Columns:\n',df.describe(exclude='object'))
        print('*'*50)
    except Exception:
        print('No Numerical Column')
        print('*'*50)
    try:
        print('Decriptive Statistics of Categorical Columns:\n',df.describe(include='object'))
        print('*'*50)
    except Exception:
        print('No Categorical Column')
        print('*'*50)

    # Outliers in Dataset
    try:
        num_cols=df.select_dtypes(exclude='object').columns.values
        for i in num_cols:
            per_75=np.nanpercentile(df[i],75)
            per_25=np.nanpercentile(df[i],25)
            iqr=per_75-per_25
            ub=per_75+(1.5*iqr)
            lb=per_25-(1.5*iqr)
            print(i,':',[j for j in df[i] if j>ub or j<lb])
        print('*'*50)
    except Exception:
        print('No Numerical Column')
        print('*'*50)