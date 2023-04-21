import pandas as pd
import os
from compensator_func import graphy
import shutil

print('>>>',finname,'Compensating ...\n\n')

Rawdata = pd.read_csv(
    'data/' + finname,
    encoding='cp949',
    sep=',',
    names=['Datetime', 'time', 'ms', 'Level(m)', 'Temp(C)'],
    skiprows=12)

# step 1. change the format of data and time creating one column
# changed date column to the datetime format of the pandas for sorting
Rawdata['Datetime'] = pd.to_datetime(Rawdata['Datetime'] + ' ' + Rawdata['time'])
# changed date column to the datetime format of the pandas for sorting
Rawdata['Datetime'] = pd.to_datetime(Rawdata['Datetime'],format='%m/%d/%Y %H:%M:%S %p')
# deleted time column since datatime column is containing all of the info needed
del Rawdata['time']



# step 2. find the matching baro data
# find matching Barodate for the same date of finname
matchbaro = finname.split('_')
matchbaro[-1] = 'BARO.csv'
matchbaro = '_'.join(matchbaro)

# check is there any file matching the date
if os.path.isfile('data/'+matchbaro) == True:
    print('You have matching baro file for',matchbaro,'\n\n')
else:
    print('You do not have matching baro file for',matchbaro,'\n\n')
    print('Check the file again and try.')
    print('Process terminated.')
    os.exit()


barodata = pd.read_csv(
    'data/' + matchbaro,
    encoding='cp949',
    sep=',',
    names=['Datetime', 'time', 'ms', 'Pressure(kPa)', 'Temp(C)'],
    skiprows=12)
# changed date column to the datetime format of the pandas for sorting
barodata['Datetime'] = pd.to_datetime(barodata['Datetime'] + ' ' + barodata['time'])
# changed date column to the datetime format of the pandas for sorting
barodata['Datetime'] = pd.to_datetime(barodata['Datetime'],format='%m/%d/%Y %H:%M:%S %p')
# deleted time column since datatime column is containing all of the info needed
del barodata['time']



# step 3. match the baro data to the level data and make compensate DF
# Baro values will be matched to the level values according to the datetime
# if they do not exactly match, nearest values will be placed
Rawdata = pd.merge_asof(Rawdata, barodata, on='Datetime', by='Datetime', direction='nearest')
# remove the NaN values
Rawdata = Rawdata.dropna()

'''
step 4. Compensation
Using Level and Pressure data, it will be compensated
equation is below:
    Compensated level = (Raw level) - (Baro value *10.1972 / 100)
All the units will be in m, please make sure

'''
Rawdata['Complevel(m)'] = (Rawdata['Level(m)']) - (Rawdata['Pressure(kPa)']*10.1972/100)

# make graph of compensated level and pressure
graphy(finname, Rawdata, 'Datetime', 'Complevel(m)', 'Pressure(kPa)')

# remove Level column and change complevel column to level column
del Rawdata['Level(m)']
Rawdata.rename(columns = {'Complevel(m)':'Level(m)'})
# save compensated data
Rawdata.to_csv('data/'+finname[:-4]+'_COMP-test.csv')

# after the compensation, move the raw data file to the 'comped_raw' folder
shutil.move('data/'+finname,'comped_raw_data/'+finname)



#


'''
df2 = df.copy()
df2['date'] = df2['date'] + pd.to_timedelta(1, unit='D')
df2['timestamp'] = df2['timestamp'] + pd.to_timedelta(1, unit='D')
pd.merge_asof(df, df2, on='timestamp', by='date', direction='nearest')
'''