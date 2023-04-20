% Aiport is a table with variables Datetime, Temp (in Farenheight),
% Atmospehric Pressure (mbar) and Sea Level Pressure (kPa)

% Create a new vector with estimated ACRE pressure.

Elev_ACRE = 708;
Elev_Airport = 599;

Datetime = Airport.Datetime;

%Est.Pressure = (Airport.Press_mbar + (708.-599.) * (Airport.SLP - Airport.Press_mbar) ./ 599)/10.;

EstPress = (Airport.Press_mbar + (992.159-994.144))/10 - 0.0081;

Est = sortrows(table(Datetime, EstPress));

%BaroTable.Properties.VariableNames{'Var1'} = 'Datetime';
%BaroTable.Properties.VariableNames{'Var2'} = 'Baro';
%BaroTable.Properties.VariableNames{'Var3'} = 'Temp';

temp2 = sortrows(BaroTable);

%temp2 = table2timetable(BaroLogger);
temp3 = table2timetable(Est);
temp4 = table2timetable(temp2);

TT = synchronize(temp3,temp4,'regular','mean','TimeStep',minutes(60));

Diff = (TT.Baro - TT.EstPress);
%Diff(Diff>2)=2;
%Diff(Diff<2)=1;

M=[TT.Baro,TT.EstPress];
TT.MergedBaro = M(sub2ind(size(M),1:numel(Diff),Diff.')).';
