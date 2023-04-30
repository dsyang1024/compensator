from typing import List
import os, sys, shutil

try:
    from compensator_func import set_read,history,readdata,oldetector,comp,graphy,inwrite,timeseriescheck
    print('compensator_func imported')
except:
    print('Compensator function error')
    sys.exit()




"""
===== System Flow =====
history / set_read
Baro_crawler >> baro_cali
readdata >> oldetector
comp >> graphy
inwrite
"""

# read setting variables
htvars = set_read()

# update history file
# updatelist: already compensated and need to be added to integrated files
# compreq: files need to be compensated
updatelist, Compreq = history()

# compensate the file
for i in Compreq:
    comp(i)
    # add compensated file names to update list
    i = i.replace('.csv','_COMP.csv')
    print('>>>',i,'added to the update list')
    updatelist[0].append(i)


# integrating files and run graphy
for i in updatelist:
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
