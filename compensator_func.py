'''
This library is including multiple functions for compensation
1. *graphy : draw graph for the data from pandas dataframe
2. *history : update history.log file for future management of the data files
3. *readdata : read data file, make it as dataframe format. 
4. intwrite : read all the compensated data, write it to the integrated file
5. == comp : compensation function for the loggers using baro
6. baro_crawler : crawling baro data from the purdue airport station
7. baro_cali : calibrate baro values(pressure) of the field, using one from purdue airport station
8. *oldetector : outlier detector for various situation
9. *set_read : this file will read environmental variables for the compensation

===== System Flow =====
history / set_read
Baro_crawler >> baro_cali
readdata >> oldetector
comp >> graphy
intwrite

'''


def graphy(title, indata, xvar, y1var, y2var):
    '''
    this function is making graph for the processed data from main.py
    users should make sure that list variable should contain 'only' float format numbers not string
    if you are using this function as part of compensator, you don't need to worry about
    ** this function is using pandas, seaborn, matplotlib
    title : title for the graph, should be string
    indata : pandas dataframe with data
    xvar : variable x (x axis, usually datetime)
    y1var : variable y1 (left side), this will be the graph title, Level(m)
    y2var : variable y2 (right side, barometer), Temp(C)
    
    # todo
    1. get the name of station outside the function and make it as title variable
    '''

    import pandas as pd
    import seaborn as sns
    import matplotlib.pyplot as plt
    from datetime import datetime
    
    # styling the graph
    sns.set_style('white')
    plt.rcParams['figure.figsize'] = 15,5
    plt.grid(color='lightgrey',linewidth=0.5,axis='both',alpha=0.5)
    
    # sub setting for the graph
    ax1 = plt.subplot() # plotting two set of graph
    ax2 = ax1.twinx() # make two y-axis graph
    ax2.tick_params(axis='y', colors='red') # for 2nd y-axis
    sns.lineplot(data=indata, x=xvar, y=y1var, ax=ax1, label=y1var).set(title = y1var)
    sns.lineplot(data=indata, x=xvar, y=y2var, color='salmon',ax=ax2, label=y2var)
    ax1.legend(labels=[y1var], loc=1)
    ax2.legend(labels=[y2var], loc=2)
    now = datetime.now() # to make filename
    plt.savefig(now.strftime('%Y-%m-%d')+'_'+title+'.png',dpi=500) # saving figure
    plt.show() # show graph


def comp():
    '''
    need to read setup file for compensation.
    this compensation setting file inclues depth of the logger in the field
    에어포트 vs out/ila/ilb/cen 비교해서 meteric difference를 찾아가는 방식...?
    이건 확인이 더 필요할 듯
    comp이후 데이터 프레임은 뒤에 ATM(kPa)가 추가 되어야함
    ''' 
    print('this is function [comp]')


def history():
    '''
    this function make history log file with file used for the compensation
    if the file read, it will be recorded to the history.log file in text format
    all the data (.csv) should be contained in the /data/ directory
    the data will be collected depends on the monitoring station, this function OUT, ILA, ILB, CEN
    return value of function is list of the updated data file
    == Output ==
    (return list) list of files need to be update for each station
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
    data = pd.read_csv('data/'+finname, encoding='cp949',sep=',',names=['Datetime','time','ms','Level(m)','Temp(C)'],skiprows=12)  # this encoding and separation is following solinst format
    

    # step 2. change the format of data and time creating one column
    data['Datetime'] = pd.to_datetime(data['Datetime']+' '+data['time']) # changed date column to the datetime format of the pandas for sorting
    data['Datetime'] = pd.to_datetime(data['Datetime'],format='%m/%d/%Y %H:%M:%S %p') # changed date column to the datetime format of the pandas for sorting
    del data['time'] # deleted time column since datatime column is containing all of the info needed
    # print(data)
    
    '''
    # step 3. read existing data from foutname
    exdata = pd.read_csv(foutname, encoding='cp949',sep=',',names=['Datetime','ms','Level(m)','Temp(C)'],skiprows=1)  # this encoding and separation is following solinst format
    exdata['Datetime'] = pd.to_datetime(exdata['Datetime'],format='%Y-%m-%d %H:%M:%S') # changed date column to the datetime format of the pandas for sorting
    # print(exdata)


    # step 4. add updated data to the integrated file with sorting data according to datetime column
    mergedata = pd.concat([data,exdata])
    print('\nData merged and sorted\n')
    mergedata.sort_values(by='Datetime', inplace=True)

    # step 5. turn pandas data frame into integrated file
    mergedata.to_csv('OUT_integrated_1.csv', index=False)
    '''

    return data


def oldetector(indata):
    '''
    this function is designed to detect outlier in the data file list
    for this, this fucntion is analyzing two types of outlier
        1. global outlier
        this is an outlier that exist out of min-max range of the data
        2. contextual outliers
        this is an outlier that exist within min-max range but sudden increase or decrease of the data
    all of this outliers can be easily found through plotting the graph
    after detecting outlier, the data will be removed
    '''

    import seaborn as sns
    import matplotlib.pyplot as plt
    import pandas as pd
    '''
    # showing graph with outliers
    figure, axes = plt.subplots(2,1, figsize=(12,5))
    sns.lineplot(ax=axes[0], x=indata['Datetime'], y=indata['Level(m)'])
    sns.boxplot(ax = axes[1], x=indata['Level(m)'])
    plt.show()
    '''
    print('\n====== Stats for data =====')
    print(indata.describe())

    # outlier detection is only for level and ATM
    indexlist = data.columns.to_list()
    if 'Level(m)' in indexlist :
        q1=indata['Level(m)'].quantile(0.25)
        q3=indata['Level(m)'].quantile(0.75)
        IQR=q3-q1
        outliers = indata[((indata['Level(m)']<(q1-1.5*IQR)) | (indata['Level(m)']>(q3+1.5*IQR)))]
        print('\n===== Outlier Detected for Level(m) =====')
        print(outliers)
        print('...',len(outliers),' outliers detected\n')
        rmlist = outliers.index.to_list()
        
        for i in rmlist:
            outdata = indata.drop(i)
        figure, axes = plt.subplots(2,1, figsize=(12,8))
        sns.lineplot(ax = axes[0], x=outdata['Datetime'], y=outdata['Level(m)']).set(title='Outliers Removed')
        sns.boxplot(ax = axes[1], x=outdata['Level(m)'])
        plt.show()
    
    # return dataframe with outliers removed
    return outdata


def set_read():
    '''
    this function is importing variable for compensation which refers height of the logger from the bottom(location of the logger)
    === input file is the setting file (setting.comp) and it contains variables below ===
    ht :: height of each loggers in metric unit(m)
    OUT, ILA, ILB, CEN
    '''
    with open('setting.comp','r') as f:
        htvars = f.readlines()[2]
        htvars = htvars.split(',')
        htvars = [float(i) for i in htvars]
    print('===== Comp variables imported =====\n')

    return(htvars)







import numpy as np
import pandas as df
import matplotlib.pyplot as plt

# testing history
updatelist =  history()

# testing readdata and graphy
testin = updatelist[0][0]
testout = 'OUT_integrated.csv'
data = readdata(testin, testout)
graphy('TEST GRAPH', data, 'Datetime', 'Level(m)', 'Temp(C)')

# testing oldector
data = oldetector(data)
indexlist = data.columns.to_list() # make colums as variable (use for graphy)

# testing set_read
htvars = set_read()
