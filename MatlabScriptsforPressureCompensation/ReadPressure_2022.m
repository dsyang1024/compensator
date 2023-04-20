
%EST Begin: 1/12/2022
%EST End: 2/1/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_02_01_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

A = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/1/2022
%EST End: 2/9/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_02_09_ACRE_BARO_BAD_DATA.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

B = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/9/2022
%EST End: 2/16/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_02_16_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

C = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/16/2022
%EST End: 2/23/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_02_23_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

D = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/23/2022
%EST End: 3/9/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_03_09_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

E = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 3/9/2022
%DST End: 3/23/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_03_23_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

F = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 3/23/2022
%DST End: 4/3/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_04_03_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

G = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 4/3/2022
%DST End: 6/21/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_06_21_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

H = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 6/21/2022
%DST End: 6/28/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_06_28_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

I = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 6/28/2022
%DST End: 7/7/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_07_07_ACRE_BARO_BAD.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

J = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_07_13_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

K = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_07_19_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

L = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_07_26_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

M = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_08_02_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

N = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_08_10_ACRE_BARO_MD.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

O = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_08_31_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

P = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_09_13_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Q = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_09_20_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

R = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_09_27_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

S = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_10_04_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

U = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_10_27_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

V = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_11_03_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

W = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/7/2022
%DST End: 7/13/2022
T = readtable("Baro Project Files 2022-11-11 18_46_58/2022_11_08_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

X = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

BaroTable_2022 = cat(1,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,U,V,W,X);

