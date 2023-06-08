# COMPENSATOR
This is project for building compensator for the level loggers in the wetland projects.
The loggers are the from Solinst and the detailed could be found from the manual pdf file.
The github link includes all the version and explanation about the structure.



## Update log
This is only for the major updates
>Minor updates will be addressed below for each functions
- 2023.02.05    Basic concept of the program designed
- 2023.02.07    Reinforce the basic design of the program and update readme file
- 2023.03.12    Updated readdata function to read all the data
- 2023.03.22    Updated readdata function to convert barometric data with correct header
- 2023.04.01    Graphy function updated
- 2023.04.10    Bug fixed for history function while updating list of records
- 2023.04.20    Update for changing or the temporal interval to 5 min
- 2023.04.20    Updated compensation function on the separate script 'comp_test.py'
- 2023.04.21    Updated compensation function to move to 'comped_raw' folder after compensation
- 2023.05.01    Working on the station code reading from the set_read function
- 2023.05.17    File naming method has been automated and separate directory for image and integrated files
- 2023.05.21    'Receipt' function added. Now after running the program, user will receive receipt with the name of stations and individual files in the receipt
- 2023.06.08    'Receipt' function minor update


### Next update

- Update or make a choiceable outlier method
- Check versatility on the Windows 11 system



## Draft of the project

This library is including multiple functions for compensation

* done // *= needs to be modified // == needs more idea and plan
0. * graphy : draw graph for the data from pandas dataframe
1. * history : update history.log file for future management of the data files
2. * alloparm : read station names and update the list of the files need to be updated
3. * readdata : read data file, make it as dataframe format
4. * intwrite : read all the compensated data, write it to the integrated file
5. * comp : compensation function for the loggers using baro
        > from this function, the baro data(ATM) will be added to the dataframe of the level logger
6. == baro_crawler : crawling baro data from the purdue airport station
7. == baro_cali : calibrate baro values(pressure) of the field, using one from purdue airport station
8. *  oldetector : outlier detector for various situation
9. *  set_read : this file will read environmental variables for the compensation
10. * receipt : this funciton will give you the receipt of the process files and person in charge



## System Flow
|Step|Function name|What they do?|
|:---:|:---:|:---:|
|1|Graphy|This will deliver the graph for the user in time-seires|
|1|Alloparm|This function will allocate parameters 'station names', 'update lists'|
|1|History|This function will arrange file names in the hitory.log|
|2|Comp|This function compensate the data that are not on  the history log|
|2|Oldetector|This function captures outlier from the compensated data and exclude them from the data|
|3|Intwrite|This function makes integrated files for each stations, if there is no integration file, it will make a new file|
|3|Receipt|This function makes receipt with name, date and the data processed|




- step 1. alloparm / history / set_read
- step 2. Baro_crawler >> baro_cali
- step 3. readdata >> oldetector
- step 4. comp >> graphy
- step 5. intwrite
