
%EST Begin: 2/9/2022
%EST End: 2/16/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_02_16_ACRE_Field63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

A = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);


%EST Begin: 2/16/2022
%EST End: 2/23/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_02_28_ACRE_Field63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

B = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/16/2022
%EST End: 2/23/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_03_02_ACRE_Field63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

C = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);


%EST Begin: 2/23/2022
%EST End: 3/9/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_03_09_ACRE_FIELD63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

D = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_04_03_ACRE_FIELD63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

E = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_04_06_ACRE_FIELD63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

F = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_04_20_ACRE_FIELD63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

G = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_04_26_ACRE_F63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

H = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_05_04_ACRE_Field63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

I = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_05_25_ACRE_Field63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

J = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);


%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_06_01_ACRE_FIELD63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

K = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_06_07_ACRE_FIELD63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

L = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_06_15_ACRE_F63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

M = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 4/3/2022
%DST End: 6/21/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_06_21_ACRE_F63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

N = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 6/21/2022
%DST End: 6/28/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_06_28_ACRE_F63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

O = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 6/28/2022
%DST End: 7/7/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_07_05_ACRE_F63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

P = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Stage/Field63_Project_Files_2022-07-17/2022_07_13_ACRE_F63.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Q = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

Field63Table_2022 = cat(1,A,B,C,D,E,F,G,H,I,J,K, L, M, N, O, P, Q);

