% Aiport is a table with variables Datetime, Temp (in Farenheight),
% Atmospheric Pressure (mbar) and Sea Level Pressure (kPa)

% Create a new vector with estimated ACRE pressure.

Elev_ACRE = 708;
Elev_Airport = 599;

Datetime = Airport.Datetime;

% Pressure converted to kPa
EstPress = (Airport.AtmPresshPa + (992.159-994.144))/10 - 0.0081;

Est = sortrows(table(Datetime, EstPress));
temp3 = table2timetable(Est);
temp5 = sortrows(unique(temp3));
temp8 = synchronize(temp5,'regular','linear','TimeStep',minutes(15));

%BaroTable_2022.Properties.VariableNames{'Var1'} = 'Datetime';
%BaroTable_2022.Properties.VariableNames{'Var2'} = 'Baro';
%BaroTable_2022.Properties.VariableNames{'Var3'} = 'Temp';

% Barologger in kPa
temp4 = table2timetable(sortrows(BaroTable_2022));
temp6 = sortrows(unique(temp4));
temp7 = synchronize(temp6,'regular','TimeStep',minutes(15));

TT = synchronize(temp8,temp7,'regular','TimeStep',minutes(15));

FinalBaro_2022 = table(TT.Datetime, TT.Baro);
k=find(isnan(TT.Baro));
FinalBaro_2022.Properties.VariableNames{'Var1'} = 'Datetime';
FinalBaro_2022.Properties.VariableNames{'Var2'} = 'Baro';
FinalBaro_2022.Baro(k) = TT.EstPress(k);
