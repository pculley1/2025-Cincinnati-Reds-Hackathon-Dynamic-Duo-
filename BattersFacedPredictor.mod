#Define the player set
set Players;

#Total sum of squares
param TSS;

#Input data
param 2021_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB {j in Players};
param 2021_BF {j in Players};
param 2021_Strikeout_vs_LHB_Percentage {j in Players};
param 2021_Strikeout_vs_RHB_Percentage {j in Players};
param 2021_Walk_vs_LHB_Percentage {j in Players};
param 2021_Walk_vs_RHB_Percentage {j in Players};
param 2021_Delta_Bat_Score_vs_RHB {j in Players};
param 2022_Vertical_Movement_vs_LHB {j in Players};
param 2022_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB {j in Players};
param 2022_Launch_Speed_vs_LHB {j in Players};
param 2022_Launch_Speed_vs_RHB {j in Players};
param 2022_Release_Spin_Rate_vs_LHB {j in Players};
param 2022_Release_Extension_vs_LHB {j in Players};
param 2022_wOBA_Value_vs_LHB {j in Players};
param 2022_wOBA_Value_vs_RHB {j in Players};
param 2022_Pitch_Number_vs_LHB {j in Players};
param 2022_Pitch_Number_vs_RHB {j in Players};
param 2022_BF {j in Players};
param 2022_Strikeout_vs_LHB_Percentage {j in Players};
param 2022_Strikeout_vs_RHB_Percentage {j in Players};
param 2022_Walk_vs_LHB_Percentage {j in Players};
param 2022_Walk_vs_RHB_Percentage {j in Players};
param 2022_Delta_Bat_Score_vs_RHB {j in Players};
param Japan {j in Players};
param Height {j in Players};

#Output data
param 2023_BF {j in Players};

#Decision variables (i.e., model parameters we want to fit), where d is the constant at the end of the model
var c1;
var c2;
var c3;
var c4;
var c5;
var c6;
var c7;
var c8;
var c9;
var c10;
var c11;
var c12;
var c13;
var c14;
var c15;
var c16;
var c17;
var c18;
var c19;
var c20;
var c21;
var c22;
var c23;
var c24;
var c25;
var c26;
var c27;
var c28;
var c29;
var c30;
var c31;
var c32;
var c33;
var c34;
var c35;
var c36;
var c37;
var c38;
var c39;
var c40;
var c41;
var c42;
var c43;
var c44;
var c45;
var c46;
var c47;
var c48;
var c49;
var c50;
var d;

#Objective function (r^2 = (1 - (residual sum of squares)/(total sum of squares)))
#Residual sum of squares: sum((actual Y - predicted Y)^2)
#Total sum of squares: sum((actual Yi - mean actual Y)^2)

#The first line is for linear regression, and the second is for quadratic regression; comment out whichever one is not being used
maximize R_Squared: 1 - (sum {j in Players} ((2023_BF[j] - (c1*2021_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c2*2021_BF[j] + c3*2021_Strikeout_vs_LHB_Percentage[j] + c4*2021_Strikeout_vs_RHB_Percentage[j] + c5*2021_Walk_vs_LHB_Percentage[j] + c6*2021_Walk_vs_RHB_Percentage[j] + c7*2021_Delta_Bat_Score_vs_RHB[j] + c8*2022_Vertical_Movement_vs_LHB[j] + c9*2022_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c10*2022_Launch_Speed_vs_LHB[j] + c11*2022_Launch_Speed_vs_RHB[j] + c12*2022_Release_Spin_Rate_vs_LHB[j] + c13*2022_Release_Extension_vs_LHB[j] + c14*2022_wOBA_Value_vs_LHB[j] + c15*2022_wOBA_Value_vs_RHB[j] + c16*2022_Pitch_Number_vs_LHB[j] + c17*2022_Pitch_Number_vs_RHB[j] + c18*2022_BF[j] + c19*2022_Strikeout_vs_LHB_Percentage[j] + c20*2022_Strikeout_vs_RHB_Percentage[j] + c21*2022_Walk_vs_LHB_Percentage[j] + c22*2022_Walk_vs_RHB_Percentage[j] + c23*2022_Delta_Bat_Score_vs_RHB[j] + c24*Japan[j] + c25*Height[j] + d))^2))/TSS;
#maximize R_Squared: 1 - (sum {j in Players} ((2023_BF[j] - (c1*2021_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j]^2 + c2*2021_BF[j]^2 + c3*2021_Strikeout_vs_LHB_Percentage[j]^2 + c4*2021_Strikeout_vs_RHB_Percentage[j]^2 + c5*2021_Walk_vs_LHB_Percentage[j]^2 + c6*2021_Walk_vs_RHB_Percentage[j]^2 + c7*2021_Delta_Bat_Score_vs_RHB[j]^2 + c8*2022_Vertical_Movement_vs_LHB[j]^2 + c9*2022_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j]^2 + c10*2022_Launch_Speed_vs_LHB[j]^2 + c11*2022_Launch_Speed_vs_RHB[j]^2 + c12*2022_Release_Spin_Rate_vs_LHB[j]^2 + c13*2022_Release_Extension_vs_LHB[j]^2 + c14*2022_wOBA_Value_vs_LHB[j]^2 + c15*2022_wOBA_Value_vs_RHB[j]^2 + c16*2022_Pitch_Number_vs_LHB[j]^2 + c17*2022_Pitch_Number_vs_RHB[j]^2 + c18*2022_BF[j]^2 + c19*2022_Strikeout_vs_LHB_Percentage[j]^2 + c20*2022_Strikeout_vs_RHB_Percentage[j]^2 + c21*2022_Walk_vs_LHB_Percentage[j]^2 + c22*2022_Walk_vs_RHB_Percentage[j]^2 + c23*2022_Delta_Bat_Score_vs_RHB[j]^2 + c24*Japan[j]^2 + c25*Height[j]^2 + c26*2021_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c27*2021_BF[j] + c28*2021_Strikeout_vs_LHB_Percentage[j] + c29*2021_Strikeout_vs_RHB_Percentage[j] + c30*2021_Walk_vs_LHB_Percentage[j] + c31*2021_Walk_vs_RHB_Percentage[j] + c32*2021_Delta_Bat_Score_vs_RHB[j] + c33*2022_Vertical_Movement_vs_LHB[j] + c34*2022_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c35*2022_Launch_Speed_vs_LHB[j] + c36*2022_Launch_Speed_vs_RHB[j] + c37*2022_Release_Spin_Rate_vs_LHB[j] + c38*2022_Release_Extension_vs_LHB[j] + c39*2022_wOBA_Value_vs_LHB[j] + c40*2022_wOBA_Value_vs_RHB[j] + c41*2022_Pitch_Number_vs_LHB[j] + c42*2022_Pitch_Number_vs_RHB[j] + c43*2022_BF[j] + c44*2022_Strikeout_vs_LHB_Percentage[j] + c45*2022_Strikeout_vs_RHB_Percentage[j] + c46*2022_Walk_vs_LHB_Percentage[j] + c47*2022_Walk_vs_RHB_Percentage[j] + c48*2022_Delta_Bat_Score_vs_RHB[j] + c49*Japan[j] + c50*Height[j] + d))^2))/TSS;

#The first line is for linear regression, and the second is for quadratic regression; comment out whichever one is not being used
#Note: This constraint is only a sanity check to ensure the program is not computing a regression model that is impossible (i.e., has an r^2 value of greater than 1)
subject to R_Constraint: 1 - (sum {j in Players} ((2023_BF[j] - (c1*2021_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c2*2021_BF[j] + c3*2021_Strikeout_vs_LHB_Percentage[j] + c4*2021_Strikeout_vs_RHB_Percentage[j] + c5*2021_Walk_vs_LHB_Percentage[j] + c6*2021_Walk_vs_RHB_Percentage[j] + c7*2021_Delta_Bat_Score_vs_RHB[j] + c8*2022_Vertical_Movement_vs_LHB[j] + c9*2022_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c10*2022_Launch_Speed_vs_LHB[j] + c11*2022_Launch_Speed_vs_RHB[j] + c12*2022_Release_Spin_Rate_vs_LHB[j] + c13*2022_Release_Extension_vs_LHB[j] + c14*2022_wOBA_Value_vs_LHB[j] + c15*2022_wOBA_Value_vs_RHB[j] + c16*2022_Pitch_Number_vs_LHB[j] + c17*2022_Pitch_Number_vs_RHB[j] + c18*2022_BF[j] + c19*2022_Strikeout_vs_LHB_Percentage[j] + c20*2022_Strikeout_vs_RHB_Percentage[j] + c21*2022_Walk_vs_LHB_Percentage[j] + c22*2022_Walk_vs_RHB_Percentage[j] + c23*2022_Delta_Bat_Score_vs_RHB[j] + c24*Japan[j] + c25*Height[j] + d))^2))/TSS <= 1;
#subject to R_Constraint: 1 - (sum {j in Players} ((2023_BF[j] - (c1*2021_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j]^2 + c2*2021_BF[j]^2 + c3*2021_Strikeout_vs_LHB_Percentage[j]^2 + c4*2021_Strikeout_vs_RHB_Percentage[j]^2 + c5*2021_Walk_vs_LHB_Percentage[j]^2 + c6*2021_Walk_vs_RHB_Percentage[j]^2 + c7*2021_Delta_Bat_Score_vs_RHB[j]^2 + c8*2022_Vertical_Movement_vs_LHB[j]^2 + c9*2022_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j]^2 + c10*2022_Launch_Speed_vs_LHB[j]^2 + c11*2022_Launch_Speed_vs_RHB[j]^2 + c12*2022_Release_Spin_Rate_vs_LHB[j]^2 + c13*2022_Release_Extension_vs_LHB[j]^2 + c14*2022_wOBA_Value_vs_LHB[j]^2 + c15*2022_wOBA_Value_vs_RHB[j]^2 + c16*2022_Pitch_Number_vs_LHB[j]^2 + c17*2022_Pitch_Number_vs_RHB[j]^2 + c18*2022_BF[j]^2 + c19*2022_Strikeout_vs_LHB_Percentage[j]^2 + c20*2022_Strikeout_vs_RHB_Percentage[j]^2 + c21*2022_Walk_vs_LHB_Percentage[j]^2 + c22*2022_Walk_vs_RHB_Percentage[j]^2 + c23*2022_Delta_Bat_Score_vs_RHB[j]^2 + c24*Japan[j]^2 + c25*Height[j]^2 + c26*2021_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c27*2021_BF[j] + c28*2021_Strikeout_vs_LHB_Percentage[j] + c29*2021_Strikeout_vs_RHB_Percentage[j] + c30*2021_Walk_vs_LHB_Percentage[j] + c31*2021_Walk_vs_RHB_Percentage[j] + c32*2021_Delta_Bat_Score_vs_RHB[j] + c33*2022_Vertical_Movement_vs_LHB[j] + c34*2022_Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB[j] + c35*2022_Launch_Speed_vs_LHB[j] + c36*2022_Launch_Speed_vs_RHB[j] + c37*2022_Release_Spin_Rate_vs_LHB[j] + c38*2022_Release_Extension_vs_LHB[j] + c39*2022_wOBA_Value_vs_LHB[j] + c40*2022_wOBA_Value_vs_RHB[j] + c41*2022_Pitch_Number_vs_LHB[j] + c42*2022_Pitch_Number_vs_RHB[j] + c43*2022_BF[j] + c44*2022_Strikeout_vs_LHB_Percentage[j] + c45*2022_Strikeout_vs_RHB_Percentage[j] + c46*2022_Walk_vs_LHB_Percentage[j] + c47*2022_Walk_vs_RHB_Percentage[j] + c48*2022_Delta_Bat_Score_vs_RHB[j] + c49*Japan[j] + c50*Height[j] + d))^2))/TSS <= 1;