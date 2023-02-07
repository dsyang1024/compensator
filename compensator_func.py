
def make_graph(title, xtitle, xlist, y1title, y1list, y2title, y2list):
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
    '''

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
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
    ax1 = plt.subplot()
    ax2 = ax1.twinx()
    ax2.tick_params(axis='y', colors='red')
    sns.lineplot(data=dfy1, x=xtitle, y=y1title, ax=ax1).set(title = y1title)
    sns.lineplot(data=dfy2, x=xtitle, y=y2title, color='salmon',ax=ax2)
    plt.show()



import numpy as np
title = 'test'
xtitle = 'Date'
xlist = [i for i in range(200)]
y1title = 'ILA level (m)'
y1list = np.random.rand(200)
y2title = 'Baro pressure (kPa)'
y2list = np.random.rand(200)

make_graph(title, xtitle, xlist, y1title, y1list, y2title, y2list)