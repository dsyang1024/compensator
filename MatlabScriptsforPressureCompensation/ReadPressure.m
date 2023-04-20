
%EST Begin: 1/12/2022
%EST End: 2/1/2022
T = readtable("Project Files 2022-02-05 01_59_28/clean.2014_10_25_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

A = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 10/25/2014,12:00:00 pm,0,98.9938,18.481
%DST End: 6/17/2015,08:00:00 am,0,99.2722,17.352
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2015_06_17_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

B = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 6/17/2015,10:00:00 am,0,99.2819,20.031
%DST End: 7/21/2015,08:45:00 am,0,98.5816,20.351
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2015_07_21_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

C = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);


%DST Begin: 7/21/2015,12:00:00 pm,0,98.7459,26.738
%DST End: 10/25/2015,05:15:00 pm,0,100.1750,16.081
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2015_10_25_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

D = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 10/25/2015,07:00:00 pm,0,100.2750,12.058
%DST End: 10/30/2015,03:00:00 pm,0,99.5634,15.752
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2015_10_30_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

E = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 10/30/2015,03:15:00 pm,0,99.5586,17.881
%EST End: 2/27/2016,02:15:00 pm,0,99.1625,11.325
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2016_02_27_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

F = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/27/2016,01:40:00 pm,0,99.1824,11.788
%DST End: 5/23/2016,05:34:00 pm,0,99.0110,21.315
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2016_05_23_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

G = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 5/23/2016,06:45:00 pm,0,99.0021,25.431
%DST End: 7/15/2016,12:21:00 pm,0,99.1273,29.971
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2016_07_15_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

H = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/15/2016,12:32:05 pm,0,99.0851,34.715
%DST End: 8/18/2016,11:20:05 am,0,99.4493,27.071
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2016_08_18_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

I = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 9/24/2016,07:14:00 pm,0,99.4843,23.196
%EST End: 3/10/2017,11:08:00 am,0,100.2660,2.110
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2017_03_10_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

J = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%EST Begin: 3/10/2017,10:24:00 am,0,100.2860,4.307
%DST End: 5/10/2017,09:30:00 am,0,98.9950,17.413
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2017_05_10_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

K = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 5/10/2017,10:42:00 am,0,98.9952,22.140
%DST End: 7/20/2017,11:18:00 am,0,99.3037,23.193
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2017_07_20_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

L = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/20/2017,11:24:00 am,0,99.2818,24.320
%DST End: 8/27/2017,12:12:00 pm,0,99.6077,24.076
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2017_08_27_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

M = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 8/27/2017,12:24:00 pm,0,99.6097,25.078
%DST End: 10/1/2017,10:48:00 am,0,100.049,14.700
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2017_10_01_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

N = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 10/1/2017,10:54:00 am,0,100.0810,19.486
%EST End: 11/20/2017,04:30:00 pm,0,98.8918,15.069
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2017_11_20_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

O = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%EST Begin: 11/20/2017,03:36:00 pm,0,98.9035,15.536
%EST End: 1/22/2018,05:48:00 pm,0,97.5010,10.611
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2018_01_22_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

P = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 1/22/2018,06:00:00 pm,0,97.5255,16.968
%EST End: 2/3/2018,05:42:00 pm,0,98.7910,1.358
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2018_02_03_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Q = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/3/2018,05:54:00 pm,0,98.7895,5.979
%DST End: 5/5/2018,11:54:00 am,0,99.2583,25.680
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2018_05_05_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

R = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 5/5/2018,01:06:00 pm,0,99.1920,31.610
%DST End: 9/27/2018,07:24:00 pm,0,99.0712,12.686
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2018_09_27_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

S = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 9/27/2018,07:36:00 pm,0,99.2084,17.772
%EST End: 12/14/2018,04:18:00 pm,0,99.4985,7.750
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2018_12_14_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

U = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%EST Begin: 12/14/2018,03:30:00 pm,0,99.4555,15.882
%EST End: 1/4/2019,12:00:00 pm,0,98.4561,6.554
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2019_01_04_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

V = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 1/4/2019,12:15:00 pm,0,98.4423,7.509
%EST End: 2/9/2019,01:09:00 pm,0,101.7910,-4.061
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2019_02_09_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

X = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 2/9/2019,01:24:00 pm,0,101.8440,6.552
%DST End: 3/31/2019,01:36:00 pm,0,100.1620,3.951
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2019_03_31_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Y = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 3/31/2019,02:42:00 pm,0,100.0910,7.551
%DST End: 5/11/2019,01:42:00 pm,0,99.2492,12.416
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2019_05_11_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

Z = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 5/11/2019,01:54:00 pm,0,99.2534,18.039
%DST End: 7/3/2019,12:42:00 pm,0,98.9298,28.010
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2019_07_03_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

AA = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 7/3/2019,12:48:00 pm,0,98.9074,31.611
%DST End: 8/2/2019,11:00:00 am,0,99.6215,23.076
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2019_08_02_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

BB = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 8/2/2019,11:15:00 am,0,99.6087,26.695
%DST End: 8/28/2019,04:30:00 pm,0,99.0707,25.982
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2019_08_28_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

CC = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 8/28/2019,04:45:00 pm,0,99.0531,29.213
%EST End: 1/9/2020,05:15:00 pm,0,99.2430,11.640
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2020_01_09_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

DD = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%EST Begin: 1/9/2020,04:30:00 pm,0,99.1525,12.151
%DST End: 4/5/2020,05:00:00 pm,0,99.4827,15.683
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2020_04_05_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

EE = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 4/5/2020,06:15:00 pm,0,99.4914,24.326
%DST End: 6/19/2020,03:30:00 pm,0,99.1806,29.124
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2020_06_19_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

FF = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 6/19/2020,03:45:00 pm,0,99.1945,28.009
%DST End: 9/13/2020,05:15:00 pm,0,99.4320,24.616
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2020_09_13_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

GG = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 9/13/2020,05:30:00 pm,0,99.4022,28.059
%EST End: 12/10/2020,04:30:00 pm,0,98.9150,15.179
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2020_12_10_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

HH = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%EST Begin: 12/10/2020,04:00:00 pm,0,98.7117,11.066
%DST End: 3/16/2021,06:30:00 pm,0,99.1838,16.181
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_03_16_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

II = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%DST Begin: 8/16/2021,03:30:00 pm,0,99.2034,29.724
%DST End: 9/18/2021,10:30:00 am,0,99.7036,29.381
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_09_18_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

JJ = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 9/18/2021,12:00:00 pm,0,99.6461,29.528
%DST End: 10/15/2021,04:30:00 pm,0,98.5279,17.220
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_10_15_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

KK = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%DST Begin: 10/15/2021,04:45:00 pm,0,98.4818,22.572
%DST End: 10/21/2021,10:15:00 am,0,98.7124,11.450
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_10_21_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

LL = table(T.Date + timeofday(T.Time) -1/24, T.LEVEL, T.TEMPERATURE);

%EST Begin: 11/11/2021,05:00:00 pm,0,98.1235,13.393
%EST End: 11/18/2021,10:00:00 am,0,99.8346,1.454
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_11_18_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

MM = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 11/18/2021,10:15:00 pm,0,100.444,0.008
%EST End: 12/2/2021,10:00:00 am,0,98.4642,9.459
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_12_02_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

NN = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 12/2/2021,10:30:00 am,0,98.4422,11.604
%EST End: 12/9/2021,09:45:00 am,0,98.6811,1.678
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_12_09_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

OO = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 12/9/2021,10:15:00 am,0,98.5493,5.447
%EST End: 12/22/2021,12:30:00 pm,0,99.7666,-0.415
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2021_12_22_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

PP = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

%EST Begin: 12/22/2021,01:00:00 pm,0,99.4439,10.825
%EST End: 1/12/2022,02:45:00 pm,0,99.1878,6.308
T = readtable("Baro Project Files 2022-07-17 15_20_21/clean.2022_01_12_ACRE_BARO.csv");
T.Date.Format = 'MM/dd/uuuu HH:mm';
T.Time.Format = 'MM/dd/uuuu HH:mm';

QQ = table(T.Date + timeofday(T.Time), T.LEVEL, T.TEMPERATURE);

BaroTable = cat(1,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,U,V,X,Y,Z,AA,BB,CC,DD,EE,FF,GG,HH,II,JJ,KK,LL,MM,NN,OO,PP,QQ);

