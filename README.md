# compensator
This is project for building compensator for the level loggers in the wetland projects.


## Update log
This is only for the major updates
>Minor updates will be addressed below for each functions
- 2023.02.05 Basic concept of the program designed
- 2023.02.07 Reinforce the basic design of the program and update readme file
- 2023.03.12 Updated readdata function to read all the data
- 2023.03.22 Updated readdata function to convert barometric data with correct header
- 2023.04.01 Graphy function updated
- 2023.04.10 Bug fixed for history function while updating list of records
- 2023.04.20 Update for changing or the temporal interval to 5 min
- 2023.04.20 Updated compensation function on the separate script 'comp_test.py'
- 2023.04.21 Updated compensation function to move to 'comped_raw' folder after compensation


### Next update
- make separate directory for image and integrated files


## Draft of the project

This library is including multiple functions for compensation

* done // *= needs to be modified // == needs more idea and plan
1. * graphy : draw graph for the data from pandas dataframe
2. *  history : update history.log file for future management of the data files
3. * readdata : read data file, make it as dataframe format
4. * intwrite : read all the compensated data, write it to the integrated file
5. * comp : compensation function for the loggers using baro
        > from this function, the baro data(ATM) will be added to the dataframe of the level logger
6. == baro_crawler : crawling baro data from the purdue airport station
7. == baro_cali : calibrate baro values(pressure) of the field, using one from purdue airport station
8. *  oldetector : outlier detector for various situation
9. *  set_read : this file will read environmental variables for the compensation

## System Flow
|Step|Function name|What they do?|
|:---:|:---:|:---:|
|테스트1|테스트2|테스트3|
|테스트1|테스트2|테스트3|
|테스트1|테스트2|테스트3|

- step 1. history / set_read
- step 2. Baro_crawler >> baro_cali
- step 3. readdata >> oldetector
- step 4. comp >> graphy
- step 5. intwrite