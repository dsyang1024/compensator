'''
This library is including multiple functions for compensation
1. graphy : draw graph for the data
2. history : update history.log file for future management of the data files
3. readdata : read data file and write it to the integrated file
3. comp : compensation function for the loggers using baro
4. baro_crawler : crawling baro data from the purdue airport station
5. baro_cali : calibrate baro values(pressure) of the field, using one from purdue airport station
'''


def graphy(title, xtitle, xlist, y1title, y1list, y2title, y2list):
    '''
    this function is making graph for the processed data from main.py
    users should make sure that list variable should contain 'only' float format numbers not string
    if you are using this function as part of compensator, you don't need to worry about
    ** this function is using pandas, seaborn, matplotlib
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
    return value of function is list of the updated data file
    '''
    import os

    # step 1. import all the data in the data folder
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


    # step 2. check the existance of the new file using history log
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


    # step 3. make a new history log including updated file list
    # merge old list and new list
    newOUTfile = oldOUTfile + OUTfile
    newOUTfile.sort()
    newILAfile = oldILAfile + ILAfile
    newILAfile.sort()
    newILBfile = oldILBfile + ILBfile
    newILBfile.sort()
    newCENfile = oldCENfile + CENfile
    newCENfile.sort()

    '''
    # important! this line commented for testing
    with open('history.log','w') as fhistory:
        for i in [newOUTfile, newILAfile, newILBfile, newCENfile]:
            for r in i:
                fhistory.write(r)
                fhistory.write('\n')
            fhistory.write('\n\n')
    print('history log file updated')
    '''
    return(OUTfile, ILAfile, ILBfile, CENfile)


def readdata(finname, foutname):
    '''
    this function read data file and write into the integrated file
    the integrated file will be updated
    additionally, this file will checking if there is any missing date within the data
    ** this function is using pandas
    == input ==
    finname : input file name (each updated data file)
    foutname : the name of the integrated file
    '''

    from datetime import datetime
    import pandas as pd

    # step 1. read the file
    data = pd.read_csv('data/'+finname, encoding='cp949',sep=',',names=['datetime','time','ms','level','temp'],skiprows=12)  # this encoding and separation is following solinst format
    
    # step 2. change the format of data and time creating one column
    data['datetime'] = pd.to_datetime(data['datetime'],format='%m/%d/%Y') # changed date column to the datetime format of the pandas for sorting
    data['time'] = pd.to_datetime(data['time'],format='%H:%M:%S %p') # changed date column to the datetime format of the pandas for sorting
    
    

    
    # todo this is the problem 날짜랑 시간 합치는게 제대로 안되는 문제가 있어서 수정이 필요함.... 검색해서 방법을 찾아봐야함.
    data['datetime'] = pd.to_datetime(data['datetime']+' '+data['time']) # changed date column to the datetime format of the pandas for sorting
    
    
    
    
    
    del data['time'] # deleted time column since datatime column is containing all of the info needed
    print(data)
    
    # step 3. read existing data from foutname
    exdata = pd.read_csv(foutname, encoding='cp949',sep=',',names=['datetime','ms','level','temp'],skiprows=1)  # this encoding and separation is following solinst format
    exdata['datetime'] = pd.to_datetime(exdata['datetime'],format='%Y-%m-%d %H:%M:%S') # changed date column to the datetime format of the pandas for sorting
    print(exdata)
    # step 4. add updated data to the integrated file with sorting data according to datetime column
    mergedata = pd.concat([exdata,data])
    print('\n\n')
    mergedata.sort_values(by='datetime', inplace=True)
    print (mergedata)





import numpy as np
title = 'test'
xtitle = 'Date'
xlist = [i for i in range(200)]
y1title = 'ILA level (m)'
y1list = np.random.rand(200)
y2title = 'Baro pressure (kPa)'
y2list = np.random.rand(200)

# graphy(title, xtitle, xlist, y1title, y1list, y2title, y2list)
updatelist =  history()
print('\n\n')
# testing readdata function
testin = updatelist[0][0]
testout = 'OUT_integrated.csv'
readdata(testin, testout)