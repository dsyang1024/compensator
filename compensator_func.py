'''
This library is including multiple functions for compensation
1. graphy : draw graph for the data
2. comp : compensation function for the loggers using baro
3. baro_crawler : crawling baro data from the purdue airport station
4. baro_cali : calibrate baro values(pressure) of the field, using one from purdue airport station
'''


def graphy(title, xtitle, xlist, y1title, y1list, y2title, y2list):
    '''
    this script is making graph for the processed data from main.py
    users should make sure that list variable should contain 'only' float format numbers not string
    if you are using this function as part of compensator, you don't need to worry about
    title : title for the graph, should be string
    x : variable x (x axis, usually timeseries)
    y1 : variable y1 (left side), this will be the graph title
    y2 : variable y2 (right side, barometer)
    title : title of each axis
    list : list of the variable
    # todo
    1. x axis should be date format
    '''

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from datetime import datetime
    
    # styling the graph
    sns.set_style('white')
    plt.rcParams['figure.figsize'] = 15,5
    plt.grid(color='lightgrey',linewidth=0.5,axis='both',alpha=0.5)

    # setting data 1 (y1)
    dfy1 = pd.DataFrame({xtitle: xlist,
                        y1title: y1list,
                    })
    # setting data 2 (y2)
    dfy2 = pd.DataFrame({xtitle: xlist,
                        y2title: y2list,
                    })
    
    # sub setting for the graph
    ax1 = plt.subplot() # plotting two set of graph
    ax2 = ax1.twinx() # make two y-axis graph
    ax2.tick_params(axis='y', colors='red') # for 2nd y-axis
    sns.lineplot(data=dfy1, x=xtitle, y=y1title, ax=ax1).set(title = y1title)
    sns.lineplot(data=dfy2, x=xtitle, y=y2title, color='salmon',ax=ax2)
    now = datetime.now() # to make filename
    plt.savefig(now.strftime('%Y-%m-%d')+'_'+y1title+'.png',dpi=500) # saving figure
    plt.show() # show graph


def comp():
    # Need to read setup file for compensation.
    # this compensation setting file inclues depth of the logger in the field
    print('this is function [comp]')

def history():



import numpy as np
title = 'test'
xtitle = 'Date'
xlist = [i for i in range(200)]
y1title = 'ILA level (m)'
y1list = np.random.rand(200)
y2title = 'Baro pressure (kPa)'
y2list = np.random.rand(200)

graphy(title, xtitle, xlist, y1title, y1list, y2title, y2list)