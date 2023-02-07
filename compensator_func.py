
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
    import numpy as np
    import matplotlib.pyplot as plt
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
    sns.lineplot(data=dfy1, x=xtitle, y=y1title, ax=ax1).set(title = y1title)
    sns.lineplot(data=dfy2, x=xtitle, y=y2title, color='r', ax=ax2)
    ax2.tick_params(axis='y', colors='red')
    plt.show()




title = 'test'
xtitle = 'Date'
xlist = [1,2,3,4,5,6,7,8,9,10]
y1title = 'ILA level (m)'
y1list = [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0]
y2title = 'Baro pressure (kPa)'
y2list = [1.0,0.9,0.8,0.7,0.6,0.5,0.4,0.3,0.2,0.1]

make_graph(title, xtitle, xlist, y1title, y1list, y2title, y2list)