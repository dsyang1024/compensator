'''
This library is including multiple functions for compensation
1. graphy : draw graph for the data
2. comp : compensation function for the loggers using baro
3. baro_crawler : crawling baro data from the purdue airport station
4. baro_cali : calibrate baro values(pressure) of the field, using one from purdue airport station
5. history
'''


def graphy(title, xtitle, xlist, y1title, y1list, y2title, y2list):
    '''
    this function is making graph for the processed data from main.py
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
    '''
    need to read setup file for compensation.
    this compensation setting file inclues depth of the logger in the field
    ''' 
    print('this is function [comp]')

def history():
    '''
    this function make history log file with file used for the compensation
    if the file read, it will be recorded to the history.log file in text format
    all the data (.csv) should be contained in the /data/ directory
    the data will be collected depends on the monitoring station, this function OUT, ILA, ILB, CEN
    '''
    import os
    data_list = os.listdir('data/')
    # print(data_list)
    OUTfile = [i for i in data_list if 'OUT' in i]
    # print(OUTfile)
    ILAfile = [i for i in data_list if 'ILA' in i]
    # print(ILAfile)
    ILBfile = [i for i in data_list if 'ILB' in i]
    # print(ILBfile)
    CENfile = [i for i in data_list if 'CEN' in i]
    # print(CENfile)


    # Read history file, if it does not exist, make a new one
    try:
        with open('history.log','r') as fhistory:
            olddata_list = fhistory.readlines()
        print('Reading history log...')
        # index [:-1] will make file name in the list without '\n'
        oldOUTfile = [i[:-1] for i in olddata_list if 'OUT' in i]
        oldILAfile = [i[:-1] for i in olddata_list if 'ILA' in i]
        oldILBfile = [i[:-1] for i in olddata_list if 'ILB' in i]
        oldCENfile = [i[:-1] for i in olddata_list if 'CEN' in i]
        print('\n\n::: Previous Data status :::','\nOUT :: ',len(oldOUTfile),'\nILA :: ',len(oldILAfile),'\nILB :: ',len(oldILBfile),'\nCEN :: ',len(oldCENfile))
    except:
        print('[Error 02] File doesnot exist and made a new file')
        fhistory = open('history.log','w')
        fhistory.close()
        # these empty list will prevent error when merging old/new lists below
        oldOUTfile = []
        oldILAfile = []
        oldILBfile = []
        oldCENfile = []


    # Check there is new data or not for each station
    # is OUTfile item is in the oldOUTfile list, it will be removed
    OUTfile = [i for i in OUTfile if i not in oldOUTfile]    
    ILAfile = [i for i in ILAfile if i not in oldILAfile]
    ILBfile = [i for i in ILBfile if i not in oldILBfile]
    CENfile = [i for i in CENfile if i not in oldCENfile]
    print('\n\n::: Updated Data status :::','\nOUT :: ',len(OUTfile),'\nILA :: ',len(ILAfile),'\nILB :: ',len(ILBfile),'\nCEN :: ',len(CENfile))



    # merge old list and new list
    newOUTfile = oldOUTfile + OUTfile
    newOUTfile.sort()
    newILAfile = oldILAfile + ILAfile
    newILAfile.sort()
    newILBfile = oldILBfile + ILBfile
    newILBfile.sort()
    newCENfile = oldCENfile + CENfile
    newCENfile.sort()


    with open('history.log','w') as fhistory:
        for i in [newOUTfile, newILAfile, newILBfile, newCENfile]:
            for r in i:
                fhistory.write(r)
                fhistory.write('\n')
            fhistory.write('\n\n')
    print('history log file updated')



import numpy as np
title = 'test'
xtitle = 'Date'
xlist = [i for i in range(200)]
y1title = 'ILA level (m)'
y1list = np.random.rand(200)
y2title = 'Baro pressure (kPa)'
y2list = np.random.rand(200)

# graphy(title, xtitle, xlist, y1title, y1list, y2title, y2list)
history()