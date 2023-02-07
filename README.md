# compensator
This is project for building compensator for the level loggers in the wetland projects.
---

### Update log
2023.02.07 Make the basic design of the program and update readme file
---

## Draft of the project
this project is consisted with the 5 parts.
1. keep the barologger data
2. Download Purdue airport barologger data(pressure)
3. Update barologger
    - If they have difference over certain range, calibrate the field barologger
4. Compensate the data using barologger
    - Update the existing level logger data (in one file)
5. Make graph for all of loggers