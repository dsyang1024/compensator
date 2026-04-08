"""
Preprocess.py

"""

import os
import pandas as pd
import matplotlib.pyplot as plt


def read_connected(stationlist, dir, mode):
    for station in stationlist:
        # read connected files and make maindf
        try:
            maindf = pd.read_csv(os.path.join(dir, station, mode, f'{station}_connected.csv'), encoding='cp949', parse_dates=['Date_Time'])
            print (maindf.info())
        except FileNotFoundError:
            print(f'{station} connected file not found. Please check the file name and path.')
        print (f'{station} connected file read successfully. Number of data: {len(maindf)}')
        plot_connected(maindf, station, mode)




def plot_connected(maindf, station, mode):
    # plot the connected data for each year into bar graph in one figure
    # from maindf, read how many years of data are there, and make a list of years
    years = maindf['Date_Time'].dt.year.unique()
    # sort data in Date_Time column in ascending order
    maindf = maindf.sort_values(by='Date_Time')
    print (years)
    # for each year, plot the data in bar graph with x axis as date and y axis as level and save
    for year in years:
        df_year = maindf[maindf['Date_Time'].dt.year == year]
        if 'Baro' in station:
            ax = df_year.plot(x='Date_Time', y='LEVEL (kPa)', figsize=(12,5), title=f'{station} {year}', linestyle='none', marker='o', markersize=.5)
        else:
            ax = df_year.plot(x='Date_Time', y='LEVEL (m)', figsize=(12,5), title=f'{station} {year}', linestyle='none', marker='o', markersize=.5)

        # set x axis range from jan to dec of the year
        ax.set_xlim(pd.to_datetime(f'{year}-01-01'), pd.to_datetime(f'{year}-12-31'))
        # set y axis range from 8-11 m
        # ax.set_ylim(8, 11)

        # save the figure in the same folder as the current script with name as station_year_connected.png
        plt.savefig(f'{mode}_{station}_{year}_connected.png')
        print (f'{station} {year} connected data plotted successfully. Figure saved as {station}_{year}_connected.png')
        plt.tight_layout()
        plt.close()
