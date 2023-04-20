
%EST Begin: 2/9/2022
%EST End: 1/27/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_02_01_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

A = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%EST Begin: 1/27/2022
%EST End: 2/9/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_02_09_ACRE_CEN_BAD_DATA.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

B = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);


%EST Begin: 2/9/2022
%EST End: 2/16/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_02_16_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

C = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);


%EST Begin: 2/16/2022
%EST End: 2/23/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_02_23_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

D = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%EST Begin: 2/16/2022
%EST End: 2/23/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_03_02_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

E = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);


%EST Begin: 2/23/2022
%EST End: 3/9/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_03_09_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

F = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%EST Begin: 2/23/2022
%EST End: 3/9/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_03_23_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

G = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_04_03_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

H = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_04_06_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

I = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_04_20_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

J = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_04_26_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

K = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_05_04_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

L = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);


%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_06_07_ACRE_CEN_MD.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

P = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_06_15_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Q = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 4/3/2022
%DST End: 6/21/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_06_21_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

R = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 6/21/2022
%DST End: 6/28/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_06_28_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

S = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 6/28/2022
%DST End: 7/7/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_07_05_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

U = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_07_13_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

V = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 7/13/2022
%DST End: 7/19/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_07_19_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

W = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 7/19/2022
%DST End: 7/26/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_07_26_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

X = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 7/26/2022
%DST End: 8/2/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_08_02_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Y = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 8/2/2022
%DST End: 8/10/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_08_12_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Z = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 8/10/2022
%DST End: 8/31/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_08_31_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AA = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 8/10/2022
%DST End: 8/31/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_09_13_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

L = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 8/31/2022
%DST End: 9/20/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_09_20_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AB = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 9/20/2022
%DST End: 9/27/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_09_27_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AC = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 9/20/2022
%DST End: 9/27/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_10_04_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AD = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);


%DST Begin: 9/27/2022
%DST End: 10/27/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_10_27_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AE = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 10/27/2022
%DST End: 11/8/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_11_03_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AF = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);

%DST Begin: 10/27/2022
%DST End: 11/8/2022
T = readtable("Project Files 2022-11-13 01_30_50/2022_11_08_ACRE_CEN.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AG = table(T.Date + timeofday(T.Time), T.LEVEL*100, T.TEMPERATURE);



CENTable_2022 = cat(1,A,B,C,D,E,F,G,H,I,J,K,L,P, Q, R, S, U, V, W,X,Y,Z,AA,L, AB,AC,AD,AE, AF, AG);

