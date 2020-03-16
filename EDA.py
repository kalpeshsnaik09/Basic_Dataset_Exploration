import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Checking Normal Distubution
from scipy.stats import shapiro
from scipy.stats import skew
from scipy.stats import normaltest
from scipy.stats import kurtosis
from scipy.stats import pearsonr
from statsmodels.graphics.gofplots import qqplot


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
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.show()
    plt.figure(figsize=(15,8))
    sns.boxplot(df[col])
    plt.axvline(mean, color='r', linestyle='--')
    plt.axvline(median, color='g', linestyle='-')
    plt.show()




def num_num_scatter(df,col_x,col_y):
    '''
    plot the Scatter Plot of given Input and Output column

    param:
        df    : Dataset Variable
        col_x : Input Column Name
        col_y : Output Column Name
    
    return:
        None

    print:
        Perason Correlation Coefficient

    display:
        show plots
    '''

    # Print Perason Correlation Coefficient
    pea_corr=df[col_y].corr(df[col_x])
    print('Perason Correlation Coefficient between {} and {} : {}'.format(col_y,col_x,pea_corr))
    print('Perason Correlation Coefficient Square between {} and {} : {}'.format(col_y,col_x,pea_corr**2))


    plt.figure(figsize=(15,8))
    # sns.regplot(x=df[col_x],y=df[col_y])
    sns.jointplot(df[col_x], df[col_y], kind="reg", stat_func=r2)
    # plt.title('Scatter plot of {} vs {}'.format(col_y,col_x))
    plt.show()



def cat_plot(df,col):
    '''
    plot the Piechart and bargraph of given column

    param:
        df  : Dataset Variable
        col : Column Name
    
    return:
        None

    display:
        show plots
    '''
    fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,5))
    fig.suptitle('Plots of {} column'.format(col))
    ax1.pie(df[col].value_counts(),autopct='%2.2f')
    ax1.set_title('Pie-Chart')
    ax2.bar(df[col].value_counts().index,df[col].value_counts())
    ax2.set_title('Bar-Graph')
    fig.show()
    

# Multi colinearity detection
def plot_heatmap(df, fig_size=(10, 7)):
    fig = plt.figure(figsize=fig_size)
    ax=sns.heatmap(df.corr(), annot=True)
    ax.set_ylim(5.0,0.0)
    plt.title('Heatmap for detecting multicollinearity', fontsize=16, color='navy')
    plt.show()

# for simple linear regrassion
def r2(x, y):
    return pearsonr(x, y)[0] ** 2

def normality_plots(df, col):
    fig = plt.figure(figsize=(15, 5))
    shapiro_p = round(shapiro(df[col])[1], 2)
    normaltest_p = round(normaltest(df[col])[1], 2)
    plt.subplot(1, 3, 1)
    plt.title('Histogram for '+col, color='navy', fontsize=12)
    plt.hist(df[col])
    plt.subplot(1, 3, 2)
    plt.title('Q-Q Plot for '+col, color='brown', fontsize=12)
    qqplot(df[col], line='s', ax=plt.subplot(1, 3, 2))
    plt.subplot(1, 3, 3)
    plt.title('Normality Test Results for '+col, color='olive', fontsize=12)
    plt.plot([shapiro_p, normaltest_p], linestyle=' ', marker='x')
    plt.text(x=0.2, y=0.5, s='Shapiro\np value\n'+str(shapiro_p))
    plt.text(x=0.6, y=0.5, s='Normaltest\np value\n'+str(normaltest_p))
    plt.ylim((0, 1))
    plt.hlines(y=0.05, color='r', xmin=0, xmax=1)
    plt.suptitle('Normality Test for '+col, fontsize=16, color='b')
    plt.show()

def ml_normality_plots(col):    
    fig = plt.figure(figsize=(15, 5))
    shapiro_p = round(shapiro(col)[1], 2)
    normaltest_p = round(normaltest(col)[1], 2)
    plt.subplot(1, 3, 1)
    plt.title('Histogram', color='navy', fontsize=12)
    plt.hist(col)
    plt.subplot(1, 3, 2)
    plt.title('Q-Q Plot', color='brown', fontsize=12)
    qqplot(col, line='s', ax=plt.subplot(1, 3, 2))
    plt.subplot(1, 3, 3)
    plt.title('Normality Test Results', color='olive', fontsize=12)
    plt.plot([shapiro_p, normaltest_p], linestyle=' ', marker='x')
    plt.text(x=0.2, y=0.5, s='Shapiro\np value\n'+str(shapiro_p))
    plt.text(x=0.6, y=0.5, s='Normaltest\np value\n'+str(normaltest_p))
    plt.ylim((0, 1))
    plt.hlines(y=0.05, color='r', xmin=0, xmax=1)
    plt.suptitle('Normality Test', fontsize=16, color='b')
    plt.show()

