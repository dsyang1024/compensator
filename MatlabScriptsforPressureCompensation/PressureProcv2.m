% Aiport is a table with variables Datetime, Temp (in Farenheight),
% Atmospehric Pressure (mbar) and Sea Level Pressure (kPa)

% Create a new vector with estimated ACRE pressure.

Elev_ACRE = 708;
Elev_Airport = 599;

Datetime = Airport.Datetime;

%Est.Pressure = (Airport.Press_mbar + (708.-599.) * (Airport.SLP - Airport.Press_mbar) ./ 599)/10.;

% Pressure converted to kPa
EstPress = (Airport.Press_mbar + (992.159-994.144))/10 - 0.0081;

Est = sortrows(table(Datetime, EstPress));
temp3 = table2timetable(Est);

%BaroTable.Properties.VariableNames{'Var1'} = 'Datetime';
%BaroTable.Properties.VariableNames{'Var2'} = 'Baro';
%BaroTable.Properties.VariableNames{'Var3'} = 'Temp';

% Barologger in kPa
temp4 = table2timetable(sortrows(BaroTable));

TT = synchronize(temp3,temp4,'regular','linear','TimeStep',minutes(15));


%CenTable.Properties.VariableNames{'Var1'} = 'Datetime';
%CenTable.Properties.VariableNames{'Var2'} = 'Cen';
%CenTable.Properties.VariableNames{'Var3'} = 'Temp';

[temp1,ia]=unique(CenTable.Datetime);
temp2 = CenTable(ia,:);

TT1=sortrows(table2timetable(temp2));

TTStage = synchronize(TT,TT1,'regular','mean','TimeStep',minutes(15));

TTStage.Diff = abs((TTStage.Baro - TTStage.EstPress));
A = abs(TTStage.Cen/10 - TTStage.Baro);
B = smoothdata(A);
TTStage.Diff2 = abs(A-B);

k = find(TTStage.Diff > 0.2 & TTStage.Diff2 > 0.2);

TTStage.Flag = TTStage.Diff - TTStage.Diff + 1;
TTStage.Flag(k)=2;
TTStage.Flag(isnan(TTStage.Flag))=2;

FinalBaro = table(TTStage.Datetime, TTStage.Baro);
k=find(isnan(TTStage.Baro));
FinalBaro.Properties.VariableNames{'Var1'} = 'Datetime';
FinalBaro.Properties.VariableNames{'Var2'} = 'Baro';
FinalBaro.Baro(k) = TTStage.EstPress(k);

%M=[TTStage.Baro,TTStage.EstPress];
%TTStage.MergedBaro = M(sub2ind(size(M),1:numel(TTStage.Flag),TTStage.Flag.')).';
%TTStage.Stage = (TTStage.Cen/10 - TTStage.MergedBaro)*0.101972*100;