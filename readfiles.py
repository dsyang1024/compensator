"""
readfiles.py

list of the file changed:
- 2024_07_19_ACRE_CEN.csv
    at the very last part of the file had crazy amount of the waterlevel (malfunction of the sensor)

"""

import os
import pandas as pd

def get_dir(path):
    # get the directory of the given path
    dir = os.getcwd()+'/'+path
    return dir

def get_stationlist(path):
    # get the list of stations in the given path
    stationlist = os.listdir(path)
    return stationlist

def get_f_from_baro(path, barometric_name, mode):
    filelist = os.listdir(os.path.join(path, barometric_name[0], mode))
    # filter only csv files
    filelist = [f for f in filelist if f.endswith('.csv')]
    return filelist

def get_f_from_station(stationlist, station, path, mode):
    filelist = os.listdir(os.path.join(path, station, mode))
    # filter only csv files
    filelist = [f for f in filelist if f.endswith('.csv')]
    filelist = [f for f in filelist if 'connected' not in f]
    # sort the filelist by date
    filelist = sorted(filelist)
    return filelist

def connect_files(station, dir, mode, filelist):
    # make maindf with header ['Date_Time', 'ms', 'LEVEL (m)', 'TEMPERATURE (degC)']
    maindf = pd.DataFrame(columns=['Date_Time', 'ms', 'LEVEL (m)', 'TEMPERATURE (degC)'])

    # connect individual files with minimum filtering
    for filename in filelist:
        file = os.path.join(dir, station, mode, filename)
        print(file)
        with open (file, 'r', encoding='cp949') as f:
            if 'Baro' in station:
                # read csv and get info first
                header = f.readlines()[:11]
                elevunit = header[7].split(' ')[1].replace('\n','')
                tempunit = header[9].split(' ')[1].replace('\n','')
                tempunit = 'degC'
                pd_header = header[-1].replace('\n','').split(',')
                pd_header[-2] = pd_header[-2]+f' ({elevunit})'
                pd_header[-1] = pd_header[-1]+f' ({tempunit})'

                df = pd.read_csv(file, skiprows=12, names=pd_header, encoding='cp949')
            else:
                # read csv and get info first
                header = f.readlines()[:12]
                elevunit = header[7].split(' ')[1].replace('\n','')
                tempunit = header[10].split(' ')[1].replace('\n','')
                tempunit = 'degC'
                pd_header = header[-1].replace('\n','').split(',')
                pd_header[-2] = pd_header[-2]+f' ({elevunit})'
                pd_header[-1] = pd_header[-1]+f' ({tempunit})'

                df = pd.read_csv(file, skiprows=12, names=pd_header, encoding='cp949')
            # if na value in the row, in the file, drop it
            df = df.dropna().reset_index(drop=True)
            # make Date column to datetime format: yyyy/mm/dd or mm/dd/yyyy format
            df['Date_P'] = pd.to_datetime(df['Date'], errors='raise')
            # if time column is in 12hr format, convert it to 24hr format
            if df['Time'].str.contains('am|pm|AM|PM').any():
                df['Time_P'] = pd.to_datetime(df['Time'], format='%I:%M:%S %p', errors='raise').dt.time
            else:
                df['Time_P'] = pd.to_datetime(df['Time'], format='%H:%M:%S', errors='raise').dt.time
            # merge Date and Time column to Date_Time column in yyyy-mm-dd 24hr format
            df['Date_Time'] = pd.to_datetime(df['Date_P'].astype(str) + ' ' + df['Time_P'].astype(str), errors='raise')            

            # ! check the data is in the correct format, if not, try to parse it again
            # if 'Date_Time' column is object, not datetime62[ns] format, try to parse it again
            if df['Date_Time'].dtype == 'object':
                df['Date_Time'] = pd.to_datetime(df['Date_Time'])
            # if 'LEVEL (m)' column is object, not float64 format, try to parse it again
            if df[pd_header[-2]].dtype == 'object':
                df[pd_header[-2]] = pd.to_numeric(df[pd_header[-2]], errors='coerce')
            # if 'TEMPERATURE (°C)' column is object, not float64 format, try to parse it again
            if df[pd_header[-1]].dtype == 'object':
                df[pd_header[-1]] = pd.to_numeric(df[pd_header[-1]], errors='coerce')

            # remove first and last rows for the data quality check
            df = df.iloc[1:-1,:].reset_index(drop=True)
            
            if 'Baro' not in station:
                # ! check if the level unit is cm, convert it to m
                # ! change the column name to 'LEVEL (m)' if it is cm
                if elevunit == 'cm':
                    df[pd_header[-2]] = df[pd_header[-2]] / 100
                    df.rename(columns={pd_header[-2]: 'LEVEL (m)'}, inplace=True)
                
                # ! simple filtering 1
                # if the water level is less than -10 and more than 20 m, drop the row
                df = df[(df['LEVEL (m)'] >= -10) & (df['LEVEL (m)'] <= 20)].reset_index(drop=True)
                # ! simple filtering 2
                # if the temperature is less than -20 and more than 50 °C, drop the row
                df = df[(df['TEMPERATURE (degC)'] >= -20) & (df['TEMPERATURE (degC)'] <= 50)].reset_index(drop=True)


            if filename == filelist[0]:
                # if it is the first file, then just assign the dataframe to maindf
                maindf = df
            else:
                # ! check the first data has interval less than 2 hours from previous data
                time_diff = (df['Date_Time'].iloc[0] - maindf['Date_Time'].iloc[-1]).total_seconds()
                if (time_diff < 7200) and 'Baro' not in station:
                    # ! if the level of the first data is more than 0.05 m  (5 cm)different from the last data, substract the difference
                    # ! from the all data of the file to be connected
                    if abs(df['LEVEL (m)'].iloc[0] - maindf['LEVEL (m)'].iloc[-1]) > 0.1:
                        diff = df['LEVEL (m)'].iloc[0] - maindf['LEVEL (m)'].iloc[-1]
                        df['LEVEL (m)'] = df['LEVEL (m)'] - diff
                        print (f"Warning: The first data of {filename} has level more than 0.1 m different from previous data.\nThe difference of {diff:.2f} m has been subtracted from the file to be connected.")

                else:
                    print (f"Warning: The first data of {filename} has interval more than 2 hours from previous data. Please check the data.")
                    print (maindf.iloc[-1], '\nUP>MAIN    BOTTOM>ADDED\n', df.iloc[0],'\n\n')

            maindf = pd.concat([maindf, df], ignore_index=True)

    # save the connected dataframe as csv file
    maindf.to_csv(os.path.join(dir, station, mode, f'{station}_connected.csv'), index=False, encoding='cp949')
    print(f'{station} files connected and saved as {station}_connected.csv\n')
