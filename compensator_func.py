"""
This library is including multiple functions for compensation
* done // *= needs to be modified // == needs more idea and plan
1. * graphy : draw graph for the data from pandas dataframe
2. *  history : update history.log file for future management of the data files
3. * readdata : read data file, make it as dataframe format
4. * intwrite : read all the compensated data, write it to the integrated file
5. * comp : compensation function for the loggers using baro
             from this function, the baro data(ATM) will be added to the dataframe of the level logger
6. == baro_crawler : crawling baro data from the purdue airport station
7. == baro_cali : calibrate baro values(pressure) of the field, using one from purdue airport station
8. *  oldetector : outlier detector for various situation
9. *  set_read : this file will read environmental variables for the compensation

===== System Flow =====
history / set_read
Baro_crawler >> baro_cali
readdata >> oldetector
comp >> graphy
intwrite

"""
from typing import List
import os, sys, shutil



def graphy(finname, indata, xvar, y1var, y2var):
    """_Summary_
        this function is making graph for the processed data from main.py
        users should make sure that list variable should contain 'only' float format numbers not string
        if you are using this function as part of compensator, you don't need to worry about
        ** this function is using pandas, seaborn, matplotlib

    Args(*: input or output):
        title(string) : title for the graph, should be string
        indata(dataframe) : pandas dataframe with data
        xvar(dataframe column name) : variable x (x axis, usually datetime)
        y1var(dataframe column name) : variable y1 (left side), this will be the graph title, Level(m)
        y2var(dataframe column name) : variable y2 (right side, barometer), Temp(C)

    Return: graph saved

    TODO : make separate directory for saving the image
    """

    import seaborn as sns
    import matplotlib.pyplot as plt
    from datetime import datetime

    # confirm title for the graph
    if 'integrated' in finname:
        if 'OUT' in finname:
            print('===== Integrated file  graph =====\n')
            title = 'ACRE outlet water level'
        elif 'ILA' in finname:
            title = 'ACRE inlet A water level'
        elif 'ILB' in finname:
            title = 'ACRE inlet B water level'
        elif 'CEN' in finname:
            title = 'ACRE center water level'
        elif 'F63' in finname:
            title = 'ACRE F63 water level'
        elif 'BARO' in finname:
            title = 'ACRE BARO Pressure'
    elif '.csv' in finname:
        print('===== Compensated  graph =====\n')
        title = finname
    else:
        print('===== Check the file name =====\n')

    # styling the graph
    sns.set_style('white')
    plt.rcParams['figure.figsize'] = 15, 5
    plt.grid(color='lightgrey', linewidth=0.5, axis='both', alpha=0.5)

    # sub setting for the graph
    ax1 = plt.subplot()  # plotting two set of graph
    ax2 = ax1.twinx()  # make two y-axis graph
    ax2.tick_params(axis='y', colors='red')  # for 2nd y-axis
    sns.lineplot(data=indata, x=xvar, y=y1var, ax=ax1, label=y1var).set(title=title)
    sns.lineplot(data=indata, x=xvar, y=y2var, color='salmon', ax=ax2, label=y2var)
    ax1.legend(labels=[y1var], loc=1)
    ax2.legend(labels=[y2var], loc=2)
    now = datetime.now()  # to make filename
    plt.savefig(now.strftime('%Y-%m-%d') + '_' + title + '.png', dpi=500)  # saving figure
    plt.show()  # show graph


def comp(finname):
    """
    need to read setup file for compensation.
    this compensation setting file inclues depth of the logger in the field
    에어포트 vs out/ila/ilb/cen 비교해서 meteric difference를 찾아가는 방식...?
    이건 확인이 더 필요할 듯
    comp이후 데이터 프레임은 뒤에 ATM(kPa)가 추가 되어야함
    """

    import pandas as pd

    print('>>>', finname, 'Compensating ...\n\n')

    Rawdata = pd.read_csv('data/' + finname,
                        encoding='cp949',
                        sep=',',
                        names=['Datetime', 'time', 'ms', 'Level(m)', 'Temp(C)'],
                        skiprows=12)

    # step 1. change the format of data and time creating one column
    # changed date column to the datetime format of the pandas for sorting
    Rawdata['Datetime'] = pd.to_datetime(Rawdata['Datetime'] + ' ' +
                                        Rawdata['time'])
    # changed date column to the datetime format of the pandas for sorting
    Rawdata['Datetime'] = pd.to_datetime(Rawdata['Datetime'],
                                        format='%m/%d/%Y %H:%M:%S %p')
    # deleted time column since datatime column is containing all of the info needed
    del Rawdata['time']

    # step 2. find the matching baro data
    # find matching Barodate for the same date of finname
    matchbaro = finname.split('_')
    matchbaro[-1] = 'BARO.csv'
    matchbaro = '_'.join(matchbaro)

    # check is there any file matching the date
    if os.path.isfile('data/' + matchbaro) == True:
        print('You have matching baro file for', matchbaro, '\n\n')
    else:
        print('You do not have matching baro file for', matchbaro, '\n\n')
        print('Check the file again and try.')
        print('Process terminated.')
        sys.exit()

    barodata = pd.read_csv(
        'data/' + matchbaro,
        encoding='cp949',
        sep=',',
        names=['Datetime', 'time', 'ms', 'Pressure(kPa)', 'Temp(C)'],
        skiprows=12)
    # changed date column to the datetime format of the pandas for sorting
    barodata['Datetime'] = pd.to_datetime(barodata['Datetime'] + ' ' +
                                        barodata['time'])
    # changed date column to the datetime format of the pandas for sorting
    barodata['Datetime'] = pd.to_datetime(barodata['Datetime'],
                                        format='%m/%d/%Y %H:%M:%S %p')
    # deleted time column since datatime column is containing all of the info needed
    del barodata['time']

    # step 3. match the baro data to the level data and make compensate DF
    # Baro values will be matched to the level values according to the datetime
    # if they do not exactly match, nearest values will be placed
    Rawdata = pd.merge_asof(Rawdata,
                            barodata,
                            on='Datetime',
                            by='Datetime',
                            direction='nearest')
    # remove the NaN values
    Rawdata = Rawdata.dropna()

    '''
    step 4. Compensation
    Using Level and Pressure data, it will be compensated
    equation is below:
        Compensated level = (Raw level) - (Baro value *10.1972 / 100)
    All the units will be in m, please make sure

    '''
    Rawdata['Complevel(m)'] = (Rawdata['Level(m)']) - (Rawdata['Pressure(kPa)'] * 10.1972 / 100)

    # make graph of compensated level and pressure
    graphy(finname, Rawdata, 'Datetime', 'Complevel(m)', 'Pressure(kPa)')

    # remove Level column and change complevel column to level column
    del Rawdata['Level(m)']
    Rawdata.rename(columns={'Complevel(m)': 'Level(m)'})
    # save compensated data
    Rawdata.to_csv('data/' + finname[:-4] + '_COMP.csv')

    # after the compensation, move the raw data file to the 'comped_raw' folder
    shutil.move('data/' + finname, 'comped_raw_data/' + finname)


def history():
    """_Summary_
        this function make history log file with file used for the compensation
        if the file read, it will be recorded to the history.log file in text format
        all the data (.csv) should be contained in the /data/ directory
        the data will be collected depends on the monitoring station, this function OUT, ILA, ILB, CEN
        return value of function is list of the updated data file

    Args(*: input or output):

    Returns:
         updatelist:
         (OUTfile, ILAfile, ILBfile, CENfile)(list): list of files need to be update for each station
         compreq:
         list of the files that need to be compensated
    """

    # step 1. import all the data in the data folder
    data_list = os.listdir('data/')
    # only for github .DS_Store file
    try:
        data_list.remove('.DS_Store')
    except:
        pass

    # print(data_list)
    OUTfile = [i for i in data_list if 'OUT_COMP' in i]
    # print(OUTfile)
    ILAfile = [i for i in data_list if 'ILA_COMP' in i]
    # print(ILAfile)
    ILBfile = [i for i in data_list if 'ILB_COMP' in i]
    # print(ILBfile)
    CENfile = [i for i in data_list if 'CEN_COMP' in i]
    # print(CENfile)
    F63file = [i for i in data_list if 'F63_COMP' in i]
    # print(F63file)
    BAROfile = [i for i in data_list if 'BARO' in i]
    # print(BAROfile)

    # list of file requires compensation
    # remove compensated data
    Compreq = [i for i in data_list if not 'COMP' in i]
    # remove baro data
    Compreq = [i for i in Compreq if not i.endswith('BARO.csv')]


    # step 2. check the existance of the new file using history log
    # Read history file, if it does not exist, make a new one
    try:
        with open('history.log', 'r') as fhistory:
            olddata_list = fhistory.readlines()
        print('Reading history log...')
        # index [:-1] will make file name in the list without '\n'
        oldOUTfile = [i[:-1] for i in olddata_list if 'OUT' in i]
        oldILAfile = [i[:-1] for i in olddata_list if 'ILA' in i]
        oldILBfile = [i[:-1] for i in olddata_list if 'ILB' in i]
        oldCENfile = [i[:-1] for i in olddata_list if 'CEN' in i]
        oldF63file = [i[:-1] for i in olddata_list if 'F63' in i]
        oldBAROfile = [i[:-1] for i in olddata_list if 'BARO' in i]


        print('\n\n::: Previous Data status :::', '\nOUT :: ',
              len(oldOUTfile), '\nILA :: ', len(oldILAfile), '\nILB :: ',
              len(oldILBfile), '\nCEN :: ', len(oldCENfile), '\nF63 :: ',
              len(oldF63file), '\nBARO :: ', len(oldBAROfile))
    except:
        print('[Error 02] File doesnot exist and made a new file')
        fhistory = open('history.log', 'w')
        fhistory.close()
        # these empty list will prevent error when merging old/new lists below
        oldOUTfile = []
        oldILAfile = []
        oldILBfile = []
        oldCENfile = []
        oldF63file = []
        oldBAROfile = []

    # Check there is new data or not for each station
    # is OUTfile item is in the oldOUTfile list, it will be removed
    OUTfile = [i for i in OUTfile if i not in oldOUTfile]
    ILAfile = [i for i in ILAfile if i not in oldILAfile]
    ILBfile = [i for i in ILBfile if i not in oldILBfile]
    CENfile = [i for i in CENfile if i not in oldCENfile]
    F63file = [i for i in F63file if i not in oldF63file]
    BAROfile = [i for i in BAROfile if i not in oldBAROfile]

    print('\n\n::: Updated Data status :::', '\nOUT :: ', len(OUTfile), '\nILA :: ', len(ILAfile), '\nILB :: ',
          len(ILBfile), '\nCEN :: ', len(CENfile), '\nF63 :: ', len(BAROfile), '\nBARO :: ', len(BAROfile))

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
    newF63file = oldF63file + F63file
    newF63file.sort()
    newBAROfile = oldBAROfile + BAROfile
    newBAROfile.sort()

    # important! this line commented for testing
    with open('history.log','w') as fhistory:
        for i in [newOUTfile, newILAfile, newILBfile, newCENfile, newF63file, newBAROfile]:
            for r in i:
                fhistory.write(r)
                fhistory.write('\n')
            fhistory.write('\n\n')

    # show message about the update
    if len(OUTfile)+len(ILAfile)+len(ILBfile)+len(CENfile)+len(BAROfile)+len(BAROfile)+len(Compreq) == 0:
        print('\n===== All the files are already up-to-date ! =====\n')
        sys.exit()
    else:
        print('\n',
            len(OUTfile) + len(ILAfile) + len(ILBfile) + len(CENfile) +
            len(BAROfile) + len(BAROfile),'files for integration')
        print(len(Compreq),'Files for compensation')
        print('\n==== history log file updated ====\n')

    # print compensation required file number and list
    print('\n===== Compensation required =====\n', str(len(Compreq)),
          'Files are needed for compensation ::\n')
    for compitem in Compreq:
        print(compitem)


    return (OUTfile, ILAfile, ILBfile, CENfile, F63file, BAROfile), Compreq


def readdata(finname):
    """_Summary_
    this function read data file and write into the integrated file
    the integrated file will be updated
    additionally, this file will checking if there is any missing date within the data
    ** this function is using pandas

    Args(*: input or output):
        *finname(string) : input file name (each updated data file)

    Returns:
        *data(dataframe) : dataframe from finname

    TODO : Unit conversion if it is cm to m
    """

    import pandas as pd

    # step 1. read the file
    if 'BARO' in finname:
        data = pd.read_csv(
            'data/' + finname,
            encoding='cp949',
            sep=',',
            names=['Datetime', 'time', 'ms', 'Pressure(kPa)', 'Temp(C)'],
            skiprows=12
        )  # this encoding and separation is following solinst format
    else:
        data = pd.read_csv(
            'data/' + finname,
            encoding='cp949',
            sep=',',
            names=['Datetime', 'time', 'ms', 'Level(m)', 'Temp(C)'],
            skiprows=12
        )  # this encoding and separation is following solinst format

    # step 2. change the format of data and time creating one column
    # changed date column to the datetime format of the pandas for sorting
    data['Datetime'] = pd.to_datetime(data['Datetime'] + ' ' + data['time'])
    # changed date column to the datetime format of the pandas for sorting
    data['Datetime'] = pd.to_datetime(data['Datetime'],format='%m/%d/%Y %H:%M:%S %p')
    del data['time']  # deleted time column since datatime column is containing all of the info needed
    # print(data)

    return data


def oldetector(indata):
    """_Summary
        this function is designed to detect outlier in the data file list
        for this, this fucntion is analyzing two types of outlier
            1. global outlier
            this is an outlier that exist out of min-max range of the data
            2. contextual outliers
            this is an outlier that exist within min-max range but sudden increase or decrease of the data
        all of this outliers can be easily found through plotting the graph
        after detecting outlier, the data will be removed

    Args(*: input or output):
        indata(dataframe) : dataframe passed from readdata
        indexlist(list) : headers of the dataframe
        outliers(dataframe) : dataframe of the outliers

    Returns:
        outdata(dataframe) : dataframe with outliers removed from indata
    """

    import seaborn as sns
    import matplotlib.pyplot as plt

    # showing graph with outliers
    figure, axes = plt.subplots(2,1, figsize=(12,8))
    sns.lineplot(ax=axes[0], x=indata['Datetime'], y=indata['Level(m)'])
    sns.boxplot(ax = axes[1], x=indata['Level(m)'])
    plt.show()

    print('\n====== Stats for data =====')
    print(indata.describe())

    # outlier detection is only for level and ATM
    indexlist = data.columns.to_list()
    if 'Level(m)' in indexlist:
        q1 = indata['Level(m)'].quantile(0.25)
        q3 = indata['Level(m)'].quantile(0.75)
        IQR = q3 - q1
        outliers = indata[((indata['Level(m)'] < (q1 - 1.5 * IQR)) | (indata['Level(m)'] > (q3 + 1.5 * IQR)))]
        outliers = indata.nsmallest(10,'Level(m)')
        print('\n===== Outlier Detected for Level(m) =====')
        print(outliers)
        print('...', len(outliers), ' outliers detected\n')
        rmlist = outliers.index.to_list()
        print(rmlist)
        outdata = indata.drop(rmlist)
        # for i in rmlist:
        # outdata = indata.drop(i)

        # plot the graph with outlier removed
        figure, axes = plt.subplots(2, 1, figsize=(12, 8))
        sns.lineplot(ax=axes[0], x=outdata['Datetime'], y=outdata['Level(m)']).set(title='Outliers Removed')
        sns.boxplot(ax=axes[1], x=outdata['Level(m)'])
        plt.show()
    else:
        outdata = indata
    # return dataframe with outliers removed
    return outdata


def set_read():
    """_Summary_
        this function is importing variable for compensation which refers height of the logger from the bottom(location of the logger)
        === input file is the setting file (setting.comp) and it contains variables below ===

    Args(*: input or output):
        ht :: height of each loggers in metric unit(m)
        OUT, ILA, ILB, CEN

    Returns:
        htvars(list) : variables for the height
    """
    with open('setting.comp', 'r') as f:
        htvars = f.readlines()[2]
        htvars: list[str] = htvars.split(',')
        htvars = [float(i) for i in htvars]
    print('===== Comp variables imported =====\n')

    return (htvars)


def inwrite(finname, indata):
    """_Summary
        this funcion is making integrated file with the input data
        first, 'indata' is the dataframe with outliers removed. (returned from oldetector)
        second, this will read the file name of the station according to the input file name(finname)
            this 'finname' is same variable with one goes into readdate() function
            and according to the finname var, which station it belongs to will be determined(foutname)
            foutname is local variable for this function and will not be shared with other functions
        third, the pandas dataframe will be written in the csv form with named 'foutname'

        reference: https://hyang2data.tistory.com/2

    Args(*: input or output):
        *finname(string) : file name of the input dataframe
        *indata(dataframe) : dataframe passed from oldetector
        mergedata(dataframe) : dataframe concatenated old and new logger data
        foutname(string) : file name of integrated logger data

    Returns:
        nothing returns from this function
        
    TODO : make separate directory for saving integrated files
    """


    # step 1. confirm foutname for writing result
    # TODO 사용자가 지점이름을 직접입력하고 이를 나중에 리스트의 형태로 활용할 수  있도록 수정해보자
    if 'OUT' in finname:
        foutname = 'OUT_integrated.csv'
        print('===== File name is OUT_integrated.csv =====\n')
    elif 'ILA' in finname:
        foutname = 'ILA_integrated.csv'
        print('===== File name is ILA_integrated.csv =====\n')
    elif 'ILB' in finname:
        foutname = 'ILB_integrated.csv'
        print('===== File name is ILB_integrated.csv =====\n')
    elif 'CEN' in finname:
        foutname = 'CEN_integrated.csv'
        print('===== File name is CEN_integrated.csv =====\n')
    elif 'F63' in finname:
        foutname = 'F63_integrated.csv'
        print('===== File name is F63_integrated.csv =====\n')
    elif 'BARO' in finname:
        foutname = 'BARO_integrated.csv'
        print('===== File name is BARO_integrated.csv =====\n')
    else:
        foutname = 'Empty'
        print('===== Check the file name =====\n')

    # in the case if foutname file not exist,
    if not os.path.isfile(foutname):
        with open(foutname, 'w') as f:
            f.close()
            print('=====', foutname, 'file is made =====')

    # step 2. read existing data from foutname
    if 'BARO' in foutname:
        exdata = pd.read_csv(
            foutname,
            encoding='cp949',
            sep=',',
            names=['Datetime', 'ms', 'Pressure(kPa)', 'Temp(C)'],
            skiprows=1)
        # this encoding and separation is following solinst format
    else:
        exdata = pd.read_csv(
            foutname,
            encoding='cp949',
            sep=',', names=['Datetime', 'ms', 'Level(m)', 'Temp(C)'],
            skiprows=1)
        # this encoding and separation is following solinst format

    exdata['Datetime'] = pd.to_datetime(exdata['Datetime'],format='%Y-%m-%d %H:%M:%S')  # changed date column to the datetime format of the pandas for sorting

    # step 3. add updated data to the integrated file with sorting data according to datetime column
    mergedata = pd.concat([indata, exdata])
    print('\nData merged and sorted\n')
    mergedata.sort_values(by='Datetime', inplace=True)
    # step 3.1. delete duplicated rows in terms of 'datetime'
    mergedata.drop_duplicates(['Datetime'])

    # step 4. turn pandas data frame into integrated file
    mergedata.to_csv(foutname, index=False)

    # step 5. implement graphy
    if 'BARO' in foutname:
        graphy(foutname, mergedata, 'Datetime', 'Pressure(kPa)', 'Temp(C)')
    else:
        graphy(foutname, mergedata, 'Datetime', 'Level(m)', 'Temp(C)')
