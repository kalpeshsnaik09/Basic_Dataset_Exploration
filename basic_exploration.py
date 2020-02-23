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
    print('Decriptive Statistics of Numerical Columns:\n',df.describe(exclude='object'))
    print('*'*50)
    print('Decriptive Statistics of Categorical Columns:\n',df.describe(include='object'))
    print('*'*50)

    # Outliers in Dataset
    num_cols=df.select_dtypes(exclude='object').columns.values
    for i in num_cols:
        per_75=np.nanpercentile(df[i],75)
        per_25=np.nanpercentile(df[i],25)
        iqr=per_75-per_25
        ub=per_75+(1.5*iqr)
        lb=per_25-(1.5*iqr)
        print(i,':',[j for j in df[i] if j>ub or j<lb])
    print('*'*50)



def eda(df):
    '''
    find basic exploratory data analysis

    param:
    ---------------
    Pandas DataFrame

    return:
    ---------------
    None

    print:
    ---------------
    print error message

    show:
    ---------------
    eda related plots
    '''
    # variable declarartion
    numeric_columns,object_columns=[],[]
    categorical_list,non_categorical_list=[],[]

    # column classification (numeric/non-numeric)
    try:
        numeric_columns=list(df.describe(exclude='object').columns)
    except Exception:
        print('numeric columns not exists.')
    try:
        object_columns=list(df.describe(include='object').columns)
    except Exception:
        print('non numeric columns not exists.')

    # column classification (categorical/non-categorical)
    if len(numeric_columns)>0:
        for col_name in numeric_columns:
            if df[col_name].nunique()>len(df[col_name])//4:
                non_categorical_list.append(col_name)
            else:
                categorical_list.append(col_name)
    
    # append non-numerical columns to categorical columns list  
    categorical_list=categorical_list+object_columns

    # plot histogram and boxplot for continuous numerical columns (non-categorical)
    if len(non_categorical_list)>0:
        for i in non_categorical_list:
            fig,(ax1,ax2)=plt.subplots(1,2,figsize=(9,5))
            fig.suptitle('Plots of {} column'.format(i))
            ax1.hist(df[i])
            ax1.set_title('Histogram')
            ax2.boxplot(df[i])
            ax2.set_title('Boxplot')
            fig.show()

    # plot pie chart, bar graph and line plot for categorical columns
    if len(categorical_list)>0:
        for i in categorical_list:
            fig,(ax1,ax2,ax3)=plt.subplots(1,3,figsize=(12,5))
            fig.suptitle('Plots of {} column'.format(i))
            ax1.pie(df[i].value_counts(),autopct='%2.2f')
            ax1.set_title('Pie-Chart')
            ax2.bar(df[i].index,df[i])
            ax2.set_title('Bar-Graph')
            ax3.plot(df[i])
            ax3.set_title('Line-Plot')
            fig.show()

    # print('numeric',numeric_columns)
    # print('non-numeric',object_columns)
    # print('noncat',non_categorical_list)
    # print('cat',categorical_list)
    
    