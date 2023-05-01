from typing import List
import os, sys, shutil

try:
    from compensator_func import set_read,history,readdata,oldetector,comp,graphy,inwrite,timeseriescheck,alloparms
    print("{::^60}".format('Compensator_func imported'),end='\n\n')
except:
    print("{:|^60}".format('Error accured for importing Compensator_func'),end='\n\n')
    sys.exit()




"""
===== System Flow =====
history / set_read
Baro_crawler >> baro_cali
readdata >> oldetector
comp >> graphy
inwrite
"""




'''
stations : string list
    this parameter is the name of the stations.
oldlist : string list
    this parameter is the name of files already in the history log
newlist : string list
    this parameter is the name of files to be added to the history log(comped)
complist : string list
    this parameter is the name of files to be comped
'''
# read setting variables
stations, htvars = set_read()

# make the lsit of the file
oldlist, newlist, complist = alloparms(stations)


# updatelist, Compreq = history(stations)


# compensate the file
for i in complist:
    print("{:=^60}".format(' Compensating '+i+' '))
    i = i.replace('.csv','_COMP.csv')
    for r in range(len(stations)):
        if stations[r] in i:
            if i in oldlist[r]:
                # check if the file never compensated before
                print("{:-^60}".format(i+' had copensated before'),end='\n\n')
            else:
                # if it is first time to compensate,
                newlist[r].append(i)
                print("{:-^60}".format(i+' added to the list'),end='\n\n')
                # comp(i)


# integrating files and run graphy
for i in newlist:
    for r in i:
        print("{:=^60}".format(r))
        # read the file needed to be processed (single file)
        testin = r
        data = readdata(testin)

        # oldetector
        data = oldetector(data)
        # make columns as variable (use for graphy)
        indexlist = data.columns.to_list()

        # inwrite
        # Graphy is included in the [inwrite] function
        inwrite(testin, data)

        # implement timeseries check function to inspect empty space of the output data
        timeseriescheck(testin)
        
        print("{:=^60}".format(r+' Finished'))
        print('\n\n\n')
        
        
