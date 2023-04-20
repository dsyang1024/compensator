%Field63Table_2022.Properties.VariableNames{'Var1'} = 'Datetime';
%Field63Table_2022.Properties.VariableNames{'Var2'} = 'F63';
%Field63Table_2022.Properties.VariableNames{'Var3'} = 'Temp';

% F63 uncompensated pressure is in cm
[temp1,ia]=unique(Field63Table_2022.Datetime);
temp2 = Field63Table_2022(ia,:);

TT1=table2timetable(temp2);
TT2=sortrows(TT1);
TT3 = retime(TT2,'regular','mean','TimeStep',minutes(60));

% Baro pressure is in kPa
[temp1,ia]=unique(FinalBaro_2022.Datetime);
temp2 = FinalBaro_2022(ia,:);

TT5=table2timetable(temp2);
TT6=sortrows(TT5);
TT7 = retime(TT6,'regular','mean','TimeStep',minutes(60));


%Stage = (TT3.Var2/10 - TT7.Baro)*0.101972*100;

% There are 10.1972 cm per kPa
F63Stage = synchronize(TT7,TT3,'regular','mean','TimeStep',minutes(60));
F63Stage.Compensated = (F63Stage.F63 - F63Stage.Baro*10.1972);
