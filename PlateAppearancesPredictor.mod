#Define the player set
set Players;

#Total sum of squares
param TSS;

#Input data
param 2021_Hit_Distance_vs_LHP {j in Players};
param 2021_Hit_Distance_vs_RHP {j in Players};
param 2021_Launch_Speed_vs_LHP {j in Players};
param 2021_Launch_Speed_vs_RHP {j in Players};
param 2021_Estimated_Batting_Average_Using_Speedangle_vs_RHP {j in Players};
param 2021_Estimated_wOBA_Using_Speedangle_vs_LHP {j in Players};
param 2021_wOBA_Value_vs_LHP {j in Players};
param 2021_BABIP_Value_vs_RHP {j in Players};
param 2021_ISO_Value_vs_LHP {j in Players};
param 2021_ISO_Value_vs_RHP {j in Players};
param 2021_PA {j in Players};
param 2021_Double_vs_LHP_Percentage {j in Players};
param 2021_Double_vs_RHP_Percentage {j in Players};
param 2021_Single_vs_LHP_Percentage {j in Players};
param 2021_Strikeout_vs_LHP_Percentage {j in Players};
param 2021_Strikeout_vs_RHP_Percentage {j in Players};
param 2021_Walk_vs_RHP_Percentage {j in Players};
param 2021_Barrel_vs_RHP_Percentage	{j in Players};
param 2021_Delta_Bat_Score_vs_LHP {j in Players};
param 2021_Delta_Bat_Score_vs_RHP {j in Players};
param 2022_Hit_Distance_vs_LHP {j in Players};
param 2022_Hit_Distance_vs_RHP {j in Players};
param 2022_Launch_Speed_vs_LHP {j in Players};
param 2022_Launch_Speed_vs_RHP {j in Players};
param 2022_Estimated_Batting_Average_Using_Speedangle_vs_RHP {j in Players};
param 2022_Estimated_wOBA_Using_Speedangle_vs_LHP {j in Players};
param 2022_wOBA_Value_vs_LHP {j in Players};
param 2022_BABIP_Value_vs_RHP {j in Players};
param 2022_ISO_Value_vs_LHP {j in Players};
param 2022_ISO_Value_vs_RHP {j in Players};
param 2022_PA {j in Players};
param 2022_Double_vs_LHP_Percentage {j in Players};
param 2022_Double_vs_RHP_Percentage {j in Players};
param 2022_Single_vs_LHP_Percentage {j in Players};
param 2022_Strikeout_vs_LHP_Percentage {j in Players};
param 2022_Strikeout_vs_RHP_Percentage {j in Players};
param 2022_Walk_vs_RHP_Percentage {j in Players};
param 2022_Barrel_vs_RHP_Percentage {j in Players};
param 2022_Delta_Bat_Score_vs_LHP {j in Players};
param 2022_Delta_Bat_Score_vs_RHP {j in Players};

#Output data
param 2023_PA {j in Players};

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
var c51;
var c52;
var c53;
var c54;
var c55;
var c56;
var c57;
var c58;
var c59;
var c60;
var c61;
var c62;
var c63;
var c64;
var c65;
var c66;
var c67;
var c68;
var c69;
var c70;
var c71;
var c72;
var c73;
var c74;
var c75;
var c76;
var c77;
var c78;
var c79;
var c80;
var d;

#Objective function (r^2 = (1 - (residual sum of squares)/(total sum of squares)))
#Residual sum of squares: sum((actual Y - predicted Y)^2)
#Total sum of squares: sum((actual Yi - mean actual Y)^2)

#The first line is for linear regression, and the second is for quadratic regression; comment out whichever one is not being used
maximize R_Squared: 1 - (sum {j in Players} ((2023_PA[j] - (c1*2021_Hit_Distance_vs_LHP[j] + c2*2021_Hit_Distance_vs_RHP[j] + c3*2021_Launch_Speed_vs_LHP[j] + c4*2021_Launch_Speed_vs_RHP[j] + c5*2021_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c6*2021_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c7*2021_wOBA_Value_vs_LHP[j] + c8*2021_BABIP_Value_vs_RHP[j] + c9*2021_ISO_Value_vs_LHP[j] + c10*2021_ISO_Value_vs_RHP[j] + c11*2021_PA[j] + c12*2021_Double_vs_LHP_Percentage[j] + c13*2021_Double_vs_RHP_Percentage[j] + c14*2021_Single_vs_LHP_Percentage[j] + c15*2021_Strikeout_vs_LHP_Percentage[j] + c16*2021_Strikeout_vs_RHP_Percentage[j] + c17*2021_Walk_vs_RHP_Percentage[j] + c18*2021_Barrel_vs_RHP_Percentage[j] + c19*2021_Delta_Bat_Score_vs_LHP[j] + c20*2021_Delta_Bat_Score_vs_RHP[j] + c21*2022_Hit_Distance_vs_LHP[j] + c22*2022_Hit_Distance_vs_RHP[j] + c23*2022_Launch_Speed_vs_LHP[j] + c24*2022_Launch_Speed_vs_RHP[j] + c25*2022_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c26*2022_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c27*2022_wOBA_Value_vs_LHP[j] + c28*2022_BABIP_Value_vs_RHP[j] + c29*2022_ISO_Value_vs_LHP[j] + c30*2022_ISO_Value_vs_RHP[j] + c31*2022_PA[j] + c32*2022_Double_vs_LHP_Percentage[j] + c33*2022_Double_vs_RHP_Percentage[j] + c34*2022_Single_vs_LHP_Percentage[j] + c35*2022_Strikeout_vs_LHP_Percentage[j] + c36*2022_Strikeout_vs_RHP_Percentage[j] + c37*2022_Walk_vs_RHP_Percentage[j] + c38*2022_Barrel_vs_RHP_Percentage[j] + c39*2022_Delta_Bat_Score_vs_LHP[j] + c40*2022_Delta_Bat_Score_vs_RHP[j] + d))^2))/TSS;
#maximize R_Squared: 1 - (sum {j in Players} ((2023_PA[j] - (c1*2021_Hit_Distance_vs_LHP[j]^2 + c2*2021_Hit_Distance_vs_RHP[j]^2 + c3*2021_Launch_Speed_vs_LHP[j]^2 + c4*2021_Launch_Speed_vs_RHP[j]^2 + c5*2021_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j]^2 + c6*2021_Estimated_wOBA_Using_Speedangle_vs_LHP[j]^2 + c7*2021_wOBA_Value_vs_LHP[j]^2 + c8*2021_BABIP_Value_vs_RHP[j]^2 + c9*2021_ISO_Value_vs_LHP[j]^2 + c10*2021_ISO_Value_vs_RHP[j]^2 + c11*2021_PA[j]^2 + c12*2021_Double_vs_LHP_Percentage[j]^2 + c13*2021_Double_vs_RHP_Percentage[j]^2 + c14*2021_Single_vs_LHP_Percentage[j]^2 + c15*2021_Strikeout_vs_LHP_Percentage[j]^2 + c16*2021_Strikeout_vs_RHP_Percentage[j]^2 + c17*2021_Walk_vs_RHP_Percentage[j]^2 + c18*2021_Barrel_vs_RHP_Percentage[j]^2 + c19*2021_Delta_Bat_Score_vs_LHP[j]^2 + c20*2021_Delta_Bat_Score_vs_RHP[j]^2 + c21*2022_Hit_Distance_vs_LHP[j]^2 + c22*2022_Hit_Distance_vs_RHP[j]^2 + c23*2022_Launch_Speed_vs_LHP[j]^2 + c24*2022_Launch_Speed_vs_RHP[j]^2 + c25*2022_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j]^2 + c26*2022_Estimated_wOBA_Using_Speedangle_vs_LHP[j]^2 + c27*2022_wOBA_Value_vs_LHP[j]^2 + c28*2022_BABIP_Value_vs_RHP[j]^2 + c29*2022_ISO_Value_vs_LHP[j]^2 + c30*2022_ISO_Value_vs_RHP[j]^2 + c31*2022_PA[j]^2 + c32*2022_Double_vs_LHP_Percentage[j]^2 + c33*2022_Double_vs_RHP_Percentage[j]^2 + c34*2022_Single_vs_LHP_Percentage[j]^2 + c35*2022_Strikeout_vs_LHP_Percentage[j]^2 + c36*2022_Strikeout_vs_RHP_Percentage[j]^2 + c37*2022_Walk_vs_RHP_Percentage[j]^2 + c38*2022_Barrel_vs_RHP_Percentage[j]^2 + c39*2022_Delta_Bat_Score_vs_LHP[j]^2 + c40*2022_Delta_Bat_Score_vs_RHP[j]^2 + c41*2021_Hit_Distance_vs_LHP[j] + c42*2021_Hit_Distance_vs_RHP[j] + c43*2021_Launch_Speed_vs_LHP[j] + c44*2021_Launch_Speed_vs_RHP[j] + c45*2021_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c46*2021_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c47*2021_wOBA_Value_vs_LHP[j] + c48*2021_BABIP_Value_vs_RHP[j] + c49*2021_ISO_Value_vs_LHP[j] + c50*2021_ISO_Value_vs_RHP[j] + c51*2021_PA[j] + c52*2021_Double_vs_LHP_Percentage[j] + c53*2021_Double_vs_RHP_Percentage[j] + c54*2021_Single_vs_LHP_Percentage[j] + c55*2021_Strikeout_vs_LHP_Percentage[j] + c56*2021_Strikeout_vs_RHP_Percentage[j] + c57*2021_Walk_vs_RHP_Percentage[j] + c58*2021_Barrel_vs_RHP_Percentage[j] + c59*2021_Delta_Bat_Score_vs_LHP[j] + c60*2021_Delta_Bat_Score_vs_RHP[j] + c61*2022_Hit_Distance_vs_LHP[j] + c62*2022_Hit_Distance_vs_RHP[j] + c63*2022_Launch_Speed_vs_LHP[j] + c64*2022_Launch_Speed_vs_RHP[j] + c65*2022_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c66*2022_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c67*2022_wOBA_Value_vs_LHP[j] + c68*2022_BABIP_Value_vs_RHP[j] + c69*2022_ISO_Value_vs_LHP[j] + c70*2022_ISO_Value_vs_RHP[j] + c71*2022_PA[j] + c72*2022_Double_vs_LHP_Percentage[j] + c73*2022_Double_vs_RHP_Percentage[j] + c74*2022_Single_vs_LHP_Percentage[j] + c75*2022_Strikeout_vs_LHP_Percentage[j] + c76*2022_Strikeout_vs_RHP_Percentage[j] + c77*2022_Walk_vs_RHP_Percentage[j] + c78*2022_Barrel_vs_RHP_Percentage[j] + c79*2022_Delta_Bat_Score_vs_LHP[j] + c80*2022_Delta_Bat_Score_vs_RHP[j] + d))^2))/TSS;

#The first line is for linear regression, and the second is for quadratic regression; comment out whichever one is not being used
#Note: This constraint is only a sanity check to ensure the program is not computing a regression model that is impossible (i.e., has an r^2 value of greater than 1)
subject to R_Constraint: 1 - (sum {j in Players} ((2023_PA[j] - (c1*2021_Hit_Distance_vs_LHP[j] + c2*2021_Hit_Distance_vs_RHP[j] + c3*2021_Launch_Speed_vs_LHP[j] + c4*2021_Launch_Speed_vs_RHP[j] + c5*2021_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c6*2021_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c7*2021_wOBA_Value_vs_LHP[j] + c8*2021_BABIP_Value_vs_RHP[j] + c9*2021_ISO_Value_vs_LHP[j] + c10*2021_ISO_Value_vs_RHP[j] + c11*2021_PA[j] + c12*2021_Double_vs_LHP_Percentage[j] + c13*2021_Double_vs_RHP_Percentage[j] + c14*2021_Single_vs_LHP_Percentage[j] + c15*2021_Strikeout_vs_LHP_Percentage[j] + c16*2021_Strikeout_vs_RHP_Percentage[j] + c17*2021_Walk_vs_RHP_Percentage[j] + c18*2021_Barrel_vs_RHP_Percentage[j] + c19*2021_Delta_Bat_Score_vs_LHP[j] + c20*2021_Delta_Bat_Score_vs_RHP[j] + c21*2022_Hit_Distance_vs_LHP[j] + c22*2022_Hit_Distance_vs_RHP[j] + c23*2022_Launch_Speed_vs_LHP[j] + c24*2022_Launch_Speed_vs_RHP[j] + c25*2022_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c26*2022_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c27*2022_wOBA_Value_vs_LHP[j] + c28*2022_BABIP_Value_vs_RHP[j] + c29*2022_ISO_Value_vs_LHP[j] + c30*2022_ISO_Value_vs_RHP[j] + c31*2022_PA[j] + c32*2022_Double_vs_LHP_Percentage[j] + c33*2022_Double_vs_RHP_Percentage[j] + c34*2022_Single_vs_LHP_Percentage[j] + c35*2022_Strikeout_vs_LHP_Percentage[j] + c36*2022_Strikeout_vs_RHP_Percentage[j] + c37*2022_Walk_vs_RHP_Percentage[j] + c38*2022_Barrel_vs_RHP_Percentage[j] + c39*2022_Delta_Bat_Score_vs_LHP[j] + c40*2022_Delta_Bat_Score_vs_RHP[j] + d))^2))/TSS <= 1;
#subject to R_Constraint: 1 - (sum {j in Players} ((2023_PA[j] - (c1*2021_Hit_Distance_vs_LHP[j]^2 + c2*2021_Hit_Distance_vs_RHP[j]^2 + c3*2021_Launch_Speed_vs_LHP[j]^2 + c4*2021_Launch_Speed_vs_RHP[j]^2 + c5*2021_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j]^2 + c6*2021_Estimated_wOBA_Using_Speedangle_vs_LHP[j]^2 + c7*2021_wOBA_Value_vs_LHP[j]^2 + c8*2021_BABIP_Value_vs_RHP[j]^2 + c9*2021_ISO_Value_vs_LHP[j]^2 + c10*2021_ISO_Value_vs_RHP[j]^2 + c11*2021_PA[j]^2 + c12*2021_Double_vs_LHP_Percentage[j]^2 + c13*2021_Double_vs_RHP_Percentage[j]^2 + c14*2021_Single_vs_LHP_Percentage[j]^2 + c15*2021_Strikeout_vs_LHP_Percentage[j]^2 + c16*2021_Strikeout_vs_RHP_Percentage[j]^2 + c17*2021_Walk_vs_RHP_Percentage[j]^2 + c18*2021_Barrel_vs_RHP_Percentage[j]^2 + c19*2021_Delta_Bat_Score_vs_LHP[j]^2 + c20*2021_Delta_Bat_Score_vs_RHP[j]^2 + c21*2022_Hit_Distance_vs_LHP[j]^2 + c22*2022_Hit_Distance_vs_RHP[j]^2 + c23*2022_Launch_Speed_vs_LHP[j]^2 + c24*2022_Launch_Speed_vs_RHP[j]^2 + c25*2022_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j]^2 + c26*2022_Estimated_wOBA_Using_Speedangle_vs_LHP[j]^2 + c27*2022_wOBA_Value_vs_LHP[j]^2 + c28*2022_BABIP_Value_vs_RHP[j]^2 + c29*2022_ISO_Value_vs_LHP[j]^2 + c30*2022_ISO_Value_vs_RHP[j]^2 + c31*2022_PA[j]^2 + c32*2022_Double_vs_LHP_Percentage[j]^2 + c33*2022_Double_vs_RHP_Percentage[j]^2 + c34*2022_Single_vs_LHP_Percentage[j]^2 + c35*2022_Strikeout_vs_LHP_Percentage[j]^2 + c36*2022_Strikeout_vs_RHP_Percentage[j]^2 + c37*2022_Walk_vs_RHP_Percentage[j]^2 + c38*2022_Barrel_vs_RHP_Percentage[j]^2 + c39*2022_Delta_Bat_Score_vs_LHP[j]^2 + c40*2022_Delta_Bat_Score_vs_RHP[j]^2 + c41*2021_Hit_Distance_vs_LHP[j] + c42*2021_Hit_Distance_vs_RHP[j] + c43*2021_Launch_Speed_vs_LHP[j] + c44*2021_Launch_Speed_vs_RHP[j] + c45*2021_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c46*2021_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c47*2021_wOBA_Value_vs_LHP[j] + c48*2021_BABIP_Value_vs_RHP[j] + c49*2021_ISO_Value_vs_LHP[j] + c50*2021_ISO_Value_vs_RHP[j] + c51*2021_PA[j] + c52*2021_Double_vs_LHP_Percentage[j] + c53*2021_Double_vs_RHP_Percentage[j] + c54*2021_Single_vs_LHP_Percentage[j] + c55*2021_Strikeout_vs_LHP_Percentage[j] + c56*2021_Strikeout_vs_RHP_Percentage[j] + c57*2021_Walk_vs_RHP_Percentage[j] + c58*2021_Barrel_vs_RHP_Percentage[j] + c59*2021_Delta_Bat_Score_vs_LHP[j] + c60*2021_Delta_Bat_Score_vs_RHP[j] + c61*2022_Hit_Distance_vs_LHP[j] + c62*2022_Hit_Distance_vs_RHP[j] + c63*2022_Launch_Speed_vs_LHP[j] + c64*2022_Launch_Speed_vs_RHP[j] + c65*2022_Estimated_Batting_Average_Using_Speedangle_vs_RHP[j] + c66*2022_Estimated_wOBA_Using_Speedangle_vs_LHP[j] + c67*2022_wOBA_Value_vs_LHP[j] + c68*2022_BABIP_Value_vs_RHP[j] + c69*2022_ISO_Value_vs_LHP[j] + c70*2022_ISO_Value_vs_RHP[j] + c71*2022_PA[j] + c72*2022_Double_vs_LHP_Percentage[j] + c73*2022_Double_vs_RHP_Percentage[j] + c74*2022_Single_vs_LHP_Percentage[j] + c75*2022_Strikeout_vs_LHP_Percentage[j] + c76*2022_Strikeout_vs_RHP_Percentage[j] + c77*2022_Walk_vs_RHP_Percentage[j] + c78*2022_Barrel_vs_RHP_Percentage[j] + c79*2022_Delta_Bat_Score_vs_LHP[j] + c80*2022_Delta_Bat_Score_vs_RHP[j] + d))^2))/TSS <= 1;