TempTable = CENTable_2022;
BTable = FinalBaro_2022;

TempTable.Properties.VariableNames{'Var1'} = 'Datetime';
TempTable.Properties.VariableNames{'Var2'} = 'Cen';
TempTable.Properties.VariableNames{'Var3'} = 'Temp';

% Cen uncompensated pressure is in cm
[temp1,ia]=unique(TempTable.Datetime);
temp2 = TempTable(ia,:);

TT1=table2timetable(temp2);
TT2=sortrows(TT1);
TT3 = retime(TT2,'regular','mean','TimeStep',minutes(15));

% Baro pressure is in kPa
[temp1,ia]=unique(BTable.Datetime);
temp2 = BTable(ia,:);

TT5=table2timetable(temp2);
TT6=sortrows(TT5);
TT7 = retime(TT6,'regular','mean','TimeStep',minutes(15));


%Stage = (TT3.Var2/10 - TT7.Baro)*0.101972*100;

% There are 10.1972 cm per kPa
CenStage_2022 = synchronize(TT7,TT3,'regular','mean','TimeStep',minutes(15));
CenStage_2022.Compensated = (CenStage_2022.Cen/100 - CenStage_2022.Baro*10.1972);
