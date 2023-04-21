# compensator
This is project for building compensator for the level loggers in the wetland projects.


## Update log
2023.02.05 Basic concept of the program designed
2023.02.07 Reinforce the basic design of the program and update readme file
2023.03.12 Updated readdata function to read all the data
2023.03.22 Updated readdata function to convert barometric data with correct header
2023.04.01 Graphy function updated
2023.04.10 Bug fixed for history function while updating list of records
2023.04.20 Update for changing or the temporal interval to 5 min
2023.04.20 Updated compensation function on the separate script 'comp_test.py'





## Draft of the project
this project is consisted with the 5 parts.
1. keep the barologger data
2. Download Purdue airport barologger data(pressure)
3. Update barologger
    - If they have difference over certain range, calibrate the field barologger
4. Compensate the data using barologger
    - Update the existing level logger data (in one file)
5. Make graph for all of loggers