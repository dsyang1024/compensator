from typing import List
import os, sys, shutil

try:
    from compensator_func import set_read,history,readdata,oldetector,comp,graphy,inwrite
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
updatelist1, Compreq = history()

# compensate the file
for i in Compreq:
    comp(i)

# Update once more to include compensated files
updatelist2, Compreq = history()
updatelist = updatelist1 + updatelist2


# integrating files and run graphy
for i in updatelist:
    for r in i:
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
