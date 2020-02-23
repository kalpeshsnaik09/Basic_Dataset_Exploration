import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Checking Normal Distubution
from scipy.stats import shapiro
from scipy.stats import skew
from scipy.stats import normaltest
from scipy.stats import kurtosis


def cont_numeric(df,col):
    '''
    plot the histogram and boxplt of given column

    param:
        df  : Dataset Variable
        col : Column Name
    
    return:
        None

    print:
        mean,median,Q1,Q3,min,max,skewness,kurtosis,shapiro test,normality test

    display:
        show plots
    '''

    mean=df[col].mean()
    median=df[col].median()
    Q1=np.nanpercentile(df[col],0.25)
    Q3=np.nanpercentile(df[col],0.75)
    min=df[col].min()
    max=df[col].max()

    Skewness=skew(df[col])
    Kurtosis=kurtosis(df[col])
    Shapiro=shapiro(df[col])
    #z_statistics,p=normaltest(df[col])
    normality_test=normaltest(df[col])
    # if p<0.05:
    #     normality_test='reject null hypothesis (H0). not normaly distributed' # not normaly distributed
    # else:
    #     normality_test='faild to reject null hypothesis (H0) assume alternate hypothesis (H1). correct normaly distributed' # normaly distributed
    
    print('Column Name : {}'.format(col))
    print('Mean : {}'.format(mean))
    print('Median : {}'.format(median))
    print('Quartile 1 : {}'.format(Q1))
    print('Quartile 3 : {}'.format(Q3))
    print('Minimun : {}'.format(min))
    print('Maximum : {}'.format(max))
    print('Skewness : {}'.format(Skewness))
    print('Kurtosis : {}'.format(Kurtosis))
    print('Shapiro : {}'.format(Shapiro))
    print('Normality Test : {}'.format(normality_test))

    dynamic_bins=int(np.cbrt(len(df[col]))*2)

    plt.figure(figsize=(15,8))
    sns.distplot(df[col],bins=dynamic_bins)
    sns
    plt.show()
    plt.figure(figsize=(15,8))
    sns.boxplot(df[col])
    plt.show()