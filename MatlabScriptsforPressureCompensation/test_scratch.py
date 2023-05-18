
from typing import List
import os, sys, shutil

try:
    from compensator_func import *
    # from compensator_func import set_read,history,readdata,oldetector,comp,graphy,inwrite,timeseriescheck,alloparms
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

history(stations, oldlist, newlist, complist)


