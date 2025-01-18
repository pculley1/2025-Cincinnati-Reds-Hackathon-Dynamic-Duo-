import pandas as pd

#Import the Baseball Savant and Lahman databases
savant_data = pd.read_csv("C:\\Users\\peter\\Downloads\\savant_data_2021_2023.csv")
lahman_data = pd.read_csv("C:\\Users\\peter\\Downloads\\lahman_people.csv")

#Import the sample submission file that contains a list of all the players for which to make playing time predictions
sample_submission = pd.read_csv("C:\\Users\\peter\\Downloads\\sample_submission.csv")

#Produce requested data for every player in the prediction list
for player_id in sample_submission["PLAYER_ID"].unique():
    
    #Display current player
    print(str(player_id), end=  " ")

    #Compute initial 2022 plate appearance information to protect against future divide-by-zero errors
    Plate_Appearances_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_2022 = Plate_Appearances_vs_LHP_2022 + Plate_Appearances_vs_RHP_2022
    
    #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
    if Plate_Appearances_vs_LHP_2022 == 0:
        Hit_Distance_vs_LHP_2022 = 0
        Launch_Speed_vs_LHP_2022 = 0
        Estimated_wOBA_Using_Speedangle_vs_LHP_2022 = 0
        wOBA_Value_vs_LHP_2022 = 0
        ISO_Value_vs_LHP_2022 = 0
        Double_vs_LHP_Percentage_2022 = 0
        Single_vs_LHP_Percentage_2022 = 0
        Strikeout_vs_LHP_Percentage_2022 = 0
        Delta_Bat_Score_vs_LHP_2022 = 0
    else:
        Hit_Distance_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["hit_distance_sc"].mean(skipna=True)
        Launch_Speed_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["launch_speed"].mean(skipna=True)
        Estimated_wOBA_Using_Speedangle_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["estimated_woba_using_speedangle"].mean(skipna=True)
        wOBA_Value_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["woba_value"].mean(skipna=True)
        ISO_Value_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["iso_value"].mean(skipna=True)
        Double_vs_LHP_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "double")]["events"].count() / Plate_Appearances_vs_LHP_2022
        Single_vs_LHP_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "single")]["events"].count() / Plate_Appearances_vs_LHP_2022
        Strikeout_vs_LHP_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "strikeout")]["events"].count() / Plate_Appearances_vs_LHP_2022
        Delta_Bat_Score_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["post_bat_score"].mean(skipna=True) - savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["bat_score"].mean(skipna=True)
    
    #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
    if Plate_Appearances_vs_RHP_2022 == 0:
        Hit_Distance_vs_RHP_2022 = 0
        Launch_Speed_vs_RHP_2022 = 0
        Estimated_Batting_Average_Using_Speedangle_vs_RHP_2022 = 0
        BABIP_Value_vs_RHP_2022 = 0
        ISO_Value_vs_RHP_2022 = 0
        Double_vs_RHP_Percentage_2022 = 0
        Strikeout_vs_RHP_Percentage_2022 = 0
        Walk_vs_RHP_Percentage_2022 = 0
        Barrel_vs_RHP_Percentage_2022 = 0
        Delta_Bat_Score_vs_RHP_2022 = 0
    else:
        Hit_Distance_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["hit_distance_sc"].mean(skipna=True)
        Launch_Speed_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["launch_speed"].mean(skipna=True)
        Estimated_Batting_Average_Using_Speedangle_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["estimated_ba_using_speedangle"].mean(skipna=True)
        BABIP_Value_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["babip_value"].mean(skipna=True)
        ISO_Value_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["iso_value"].mean(skipna=True)
        Double_vs_RHP_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "double")]["events"].count() / Plate_Appearances_vs_RHP_2022
        Strikeout_vs_RHP_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "strikeout")]["events"].count() / Plate_Appearances_vs_RHP_2022
        Walk_vs_RHP_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "walk")]["events"].count() / Plate_Appearances_vs_RHP_2022
        
        #Another attempt to protect against a divide-by-zero error for a more specialized statistic; even if a player has batted, that doesn't imply that player ever made contact with the ball, hence the following statements
        Swings_Making_Contact_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & ((savant_data["launch_speed_angle"] == 1) | (savant_data["launch_speed_angle"] == 2) | (savant_data["launch_speed_angle"] == 3) | (savant_data["launch_speed_angle"] == 4) | (savant_data["launch_speed_angle"] == 5) | (savant_data["launch_speed_angle"] == 6))]["launch_speed_angle"].count()
        
        if Swings_Making_Contact_2022 == 0:
            Barrel_vs_RHP_Percentage_2022 = 0
        else:
            Barrel_vs_RHP_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 6)]["launch_speed_angle"].count() / Swings_Making_Contact_2022
        
        Delta_Bat_Score_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["post_bat_score"].mean(skipna=True) - savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["bat_score"].mean(skipna=True)

    #Same setup used here as for 2022 hitting data
    #Compute initial 2023 plate appearance information to protect against future divide-by-zero errors
    Plate_Appearances_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_2023 = Plate_Appearances_vs_LHP_2023 + Plate_Appearances_vs_RHP_2023
    
    #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
    if Plate_Appearances_vs_LHP_2023 == 0:
        Hit_Distance_vs_LHP_2023 = 0
        Launch_Speed_vs_LHP_2023 = 0
        Estimated_wOBA_Using_Speedangle_vs_LHP_2023 = 0
        wOBA_Value_vs_LHP_2023 = 0
        ISO_Value_vs_LHP_2023 = 0
        Double_vs_LHP_Percentage_2023 = 0
        Single_vs_LHP_Percentage_2023 = 0
        Strikeout_vs_LHP_Percentage_2023 = 0
        Delta_Bat_Score_vs_LHP_2023 = 0
    else:
        Hit_Distance_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["hit_distance_sc"].mean(skipna=True)
        Launch_Speed_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["launch_speed"].mean(skipna=True)
        Estimated_wOBA_Using_Speedangle_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["estimated_woba_using_speedangle"].mean(skipna=True)
        wOBA_Value_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["woba_value"].mean(skipna=True)
        ISO_Value_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["iso_value"].mean(skipna=True)
        Double_vs_LHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "double")]["events"].count() / Plate_Appearances_vs_LHP_2023
        Single_vs_LHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "single")]["events"].count() / Plate_Appearances_vs_LHP_2023
        Strikeout_vs_LHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "strikeout")]["events"].count() / Plate_Appearances_vs_LHP_2023
        Delta_Bat_Score_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["post_bat_score"].mean(skipna=True) - savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["bat_score"].mean(skipna=True)
    
    #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
    if Plate_Appearances_vs_RHP_2023 == 0:
        Hit_Distance_vs_RHP_2023 = 0
        Launch_Speed_vs_RHP_2023 = 0
        Estimated_Batting_Average_Using_Speedangle_vs_RHP_2023 = 0
        BABIP_Value_vs_RHP_2023 = 0
        ISO_Value_vs_RHP_2023 = 0
        Double_vs_RHP_Percentage_2023 = 0
        Strikeout_vs_RHP_Percentage_2023 = 0
        Walk_vs_RHP_Percentage_2023 = 0
        Barrel_vs_RHP_Percentage_2023 = 0
        Delta_Bat_Score_vs_RHP_2023 = 0
    else:
        Hit_Distance_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["hit_distance_sc"].mean(skipna=True)
        Launch_Speed_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["launch_speed"].mean(skipna=True)
        Estimated_Batting_Average_Using_Speedangle_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["estimated_ba_using_speedangle"].mean(skipna=True)
        BABIP_Value_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["babip_value"].mean(skipna=True)
        ISO_Value_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["iso_value"].mean(skipna=True)
        Double_vs_RHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "double")]["events"].count() / Plate_Appearances_vs_RHP_2023
        Strikeout_vs_RHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "strikeout")]["events"].count() / Plate_Appearances_vs_RHP_2023
        Walk_vs_RHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "walk")]["events"].count() / Plate_Appearances_vs_RHP_2023
        
        #Another attempt to protect against a divide-by-zero error for a more specialized statistic; even if a player has batted, that doesn't imply that player ever made contact with the ball, hence the following statements
        Swings_Making_Contact_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & ((savant_data["launch_speed_angle"] == 1) | (savant_data["launch_speed_angle"] == 2) | (savant_data["launch_speed_angle"] == 3) | (savant_data["launch_speed_angle"] == 4) | (savant_data["launch_speed_angle"] == 5) | (savant_data["launch_speed_angle"] == 6))]["launch_speed_angle"].count()

        if Swings_Making_Contact_2023 == 0:
            Barrel_vs_RHP_Percentage_2023 = 0
        else:
            Barrel_vs_RHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 6)]["launch_speed_angle"].count() / Swings_Making_Contact_2023
        
        Delta_Bat_Score_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["post_bat_score"].mean(skipna=True) - savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["bat_score"].mean(skipna=True)

    #Use optimized linear regression model with the max function incorporated to make a prediction for the total number of plate appearance a player will get in 2024; the max function ensures the result is nonnegative
    Plate_Appearances_Prediction_2024 = round(max(0, 0.665651*Hit_Distance_vs_LHP_2022 - 0.47379*Hit_Distance_vs_RHP_2022 - 2.43703*Launch_Speed_vs_LHP_2022 + 2.41599*Launch_Speed_vs_RHP_2022 + 95.7543*Estimated_Batting_Average_Using_Speedangle_vs_RHP_2022 - 140.15*Estimated_wOBA_Using_Speedangle_vs_LHP_2022 + 97.6149*wOBA_Value_vs_LHP_2022 - 60.2109*BABIP_Value_vs_RHP_2022 - 54.711*ISO_Value_vs_LHP_2022 + 248.293*ISO_Value_vs_RHP_2022 + 0.034175*Plate_Appearances_2022 + 300.419*Double_vs_LHP_Percentage_2022 - 166.677*Double_vs_RHP_Percentage_2022 + 285.51*Single_vs_LHP_Percentage_2022 + 58.9504*Strikeout_vs_LHP_Percentage_2022 - 76.6566*Strikeout_vs_RHP_Percentage_2022 + 348.327*Walk_vs_RHP_Percentage_2022 + 32.9904*Barrel_vs_RHP_Percentage_2022 - 764.36*Delta_Bat_Score_vs_LHP_2022 - 465.359*Delta_Bat_Score_vs_RHP_2022 + 0.415185*Hit_Distance_vs_LHP_2023 - 0.15114*Hit_Distance_vs_RHP_2023 + 3.29479*Launch_Speed_vs_LHP_2023 + 2.66726*Launch_Speed_vs_RHP_2023 - 121.663*Estimated_Batting_Average_Using_Speedangle_vs_RHP_2023 - 48.2056*Estimated_wOBA_Using_Speedangle_vs_LHP_2023 + 92.8928*wOBA_Value_vs_LHP_2023 + 77.9598*BABIP_Value_vs_RHP_2023 + 136.633*ISO_Value_vs_LHP_2023 + 202.162*ISO_Value_vs_RHP_2023 + 0.617495*Plate_Appearances_2023 - 135.249*Double_vs_LHP_Percentage_2023 + 450.403*Double_vs_RHP_Percentage_2023 + 91.2746*Single_vs_LHP_Percentage_2023 - 150.458*Strikeout_vs_LHP_Percentage_2023 - 13.8309*Strikeout_vs_RHP_Percentage_2023 - 82.0227*Walk_vs_RHP_Percentage_2023 + 229.58*Barrel_vs_RHP_Percentage_2023 - 486.484*Delta_Bat_Score_vs_LHP_2023 + 1179.44*Delta_Bat_Score_vs_RHP_2023 - 591.871))

    #After some analysis of the players the model originally predicted would be two-way players, we found only one actually had the qualifications to be a real two-way player; the rest were position players who pitched a game or two in the last two years
    #Our analysis determined player ID 18396fcf5f98aac97ec6127f7924868d3ef7bd9e must correspond to Shohei Ohtani since no one else received 500+ PA and faced 500+ batters
    #Since Ohtani could not pitch in 2024 due to injury, we specifically set only his predicted BF for 2024 to be 0 without checking more specific information
    if player_id == "18396fcf5f98aac97ec6127f7924868d3ef7bd9e":
        Batters_Faced_Prediction_2024 = 0
    else:    
        
        #Compute initial 2022 batters faced information to protect against future divide-by-zero errors
        LH_Batters_Faced_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
        RH_Batters_Faced_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
        Batters_Faced_2022 = LH_Batters_Faced_2022 + RH_Batters_Faced_2022

        #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
        if LH_Batters_Faced_2022 == 0:
            Release_Speed_vs_LHB_2022 = 0
            Strikeout_vs_LHB_Percentage_2022 = 0
            Walk_vs_LHB_Percentage_2022 = 0
        else:

            #While release speed is not in the final model, we use it as a means to catch instances of position players pitching and prevent the model from treating a position player like a regular pitcher (i.e., assigning a large number of BF to that player for 2024) 
            Release_Speed_vs_LHB_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_speed"].mean(skipna=True)
            
            #From studying special case data where the model originally projected a player to be a two-way player, we found that setting a minimum average release speed of 81 mph would seperate real pitchers from position players trying to pitch in a blowout
            if Release_Speed_vs_LHB_2022 < 81:
                Strikeout_vs_LHB_Percentage_2022 = 0
                Walk_vs_LHB_Percentage_2022 = 0
            else:
                Strikeout_vs_LHB_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "strikeout")]["events"].count() / LH_Batters_Faced_2022
                Walk_vs_LHB_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "walk")]["events"].count() / LH_Batters_Faced_2022

        #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
        if RH_Batters_Faced_2022 == 0:
            Release_Speed_vs_RHB_2022 = 0
            Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2022 = 0
            Strikeout_vs_RHB_Percentage_2022 = 0
            Walk_vs_RHB_Percentage_2022 = 0
            Delta_Bat_Score_vs_RHB_2022 = 0
        else:
            Release_Speed_vs_RHB_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_speed"].mean(skipna=True)
            if Release_Speed_vs_RHB_2022 < 81:
                Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2022 = 0
                Strikeout_vs_RHB_Percentage_2022 = 0
                Walk_vs_RHB_Percentage_2022 = 0
                Delta_Bat_Score_vs_RHB_2022 = 0
            else:
                Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["plate_z"].mean(skipna=True)
                Strikeout_vs_RHB_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "strikeout")]["events"].count() / RH_Batters_Faced_2022
                Walk_vs_RHB_Percentage_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "walk")]["events"].count() / RH_Batters_Faced_2022
                Delta_Bat_Score_vs_RHB_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["post_bat_score"].mean(skipna=True) - savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["bat_score"].mean(skipna=True)

        #Same setup used here as for 2022 pitching data
        #Compute initial 2022 batters faced information to protect against future divide-by-zero errors
        LH_Batters_Faced_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
        RH_Batters_Faced_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
        Batters_Faced_2023 = LH_Batters_Faced_2023 + RH_Batters_Faced_2023

        #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
        if LH_Batters_Faced_2023 == 0:
            Release_Speed_vs_LHB_2023 = 0
            Vertical_Movement_vs_LHB_2023 = 0
            Launch_Speed_vs_LHB_2023 = 0
            Release_Spin_Rate_vs_LHB_2023 = 0
            Release_Extension_vs_LHB_2023 = 0
            wOBA_Value_vs_LHB_2023 = 0
            Pitch_Number_vs_LHB_2023 = 0
            Strikeout_vs_LHB_Percentage_2023 = 0
            Walk_vs_LHB_Percentage_2023 = 0
        else:
            Release_Speed_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_speed"].mean(skipna=True)
            if Release_Speed_vs_LHB_2023 < 81:
                Vertical_Movement_vs_LHB_2023 = 0
                Launch_Speed_vs_LHB_2023 = 0
                Release_Spin_Rate_vs_LHB_2023 = 0
                Release_Extension_vs_LHB_2023 = 0
                wOBA_Value_vs_LHB_2023 = 0
                Pitch_Number_vs_LHB_2023 = 0
                Strikeout_vs_LHB_Percentage_2023 = 0
                Walk_vs_LHB_Percentage_2023 = 0
            else:
                Vertical_Movement_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["pfx_z"].mean(skipna=True)
                Launch_Speed_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["launch_speed"].mean(skipna=True)
                Release_Spin_Rate_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_spin_rate"].mean(skipna=True)
                Release_Extension_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_extension"].mean(skipna=True)
                wOBA_Value_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["woba_value"].mean(skipna=True)
                Pitch_Number_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["pitch_number"].mean(skipna=True)
                Strikeout_vs_LHB_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "strikeout")]["events"].count() / LH_Batters_Faced_2023
                Walk_vs_LHB_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "walk")]["events"].count() / LH_Batters_Faced_2023

        #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
        if RH_Batters_Faced_2023 == 0:
            Release_Speed_vs_RHB_2023 = 0
            Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2023 = 0
            Launch_Speed_vs_RHB_2023 = 0
            wOBA_Value_vs_RHB_2023 = 0
            Pitch_Number_vs_RHB_2023 = 0
            Strikeout_vs_RHB_Percentage_2023 = 0
            Walk_vs_RHB_Percentage_2023 = 0
            Delta_Bat_Score_vs_RHB_2023 = 0
        else:
            Release_Speed_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_speed"].mean(skipna=True)
            if Release_Speed_vs_RHB_2023 < 81:
                Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2023 = 0
                Launch_Speed_vs_RHB_2023 = 0
                wOBA_Value_vs_RHB_2023 = 0
                Pitch_Number_vs_RHB_2023 = 0
                Strikeout_vs_RHB_Percentage_2023 = 0
                Walk_vs_RHB_Percentage_2023 = 0
                Delta_Bat_Score_vs_RHB_2023 = 0
            else:
                Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["plate_z"].mean(skipna=True)
                Launch_Speed_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["launch_speed"].mean(skipna=True)
                wOBA_Value_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["woba_value"].mean(skipna=True)
                Pitch_Number_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["pitch_number"].mean(skipna=True)
                Strikeout_vs_RHB_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "strikeout")]["events"].count() / RH_Batters_Faced_2023
                Walk_vs_RHB_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "walk")]["events"].count() / RH_Batters_Faced_2023
                Delta_Bat_Score_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["post_bat_score"].mean(skipna=True) - savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["bat_score"].mean(skipna=True)

        #If a player threw 81+ mph against both types of hitters in a single year, we assume that player to be a real pitcher, else we excerise the following statements to prevent position players from being assigned large 2024 BF just solely based on their nationality and height
        if ((Release_Speed_vs_LHB_2022 < 81) | (Release_Speed_vs_RHB_2022 < 81)) & ((Release_Speed_vs_LHB_2023 < 81) | (Release_Speed_vs_RHB_2023 < 81)):
            Japan = 0
            Height = 0
        else:
            
            #If a real pitcher is Japanese, that gives that pitcher a significant increase in the projected number of BF for 2024
            Nationality = str(lahman_data.loc[(lahman_data["player_mlb_id"] == player_id)]["birthCountry"])
            if "Japan" in Nationality:
                Japan = 1
            else:
                Japan = 0
            
            #Taller pitchers in general have a playing time advantage over shorter pitchers according to the model
            Height = lahman_data.loc[(lahman_data["player_mlb_id"] == player_id)]["height"].mean(skipna=True)

        #Use optimized linear regression model with the max function incorporated to make a prediction for the total number of batters faced a player will get in 2024; the max function ensures the result is nonnegative
        Batters_Faced_Prediction_2024 = round(max(0, -19.0598*Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2022 + 0.172054*Batters_Faced_2022 + 24.4149*Strikeout_vs_LHB_Percentage_2022 - 192.214*Strikeout_vs_RHB_Percentage_2022 - 42.7111*Walk_vs_LHB_Percentage_2022 + 140.701*Walk_vs_RHB_Percentage_2022 - 266.172*Delta_Bat_Score_vs_RHB_2022 - 17.7523*Vertical_Movement_vs_LHB_2023 - 38.4902*Vertical_Position_of_Ball_Crossing_Home_Plate_vs_RHB_2023 - 0.844144*Launch_Speed_vs_LHB_2023 - 3.96826*Launch_Speed_vs_RHB_2023 + 0.0304721*Release_Spin_Rate_vs_LHB_2023 + 22.0294*Release_Extension_vs_LHB_2023 - 135.385*wOBA_Value_vs_LHB_2023 - 295.126*wOBA_Value_vs_RHB_2023 - 26.9569*Pitch_Number_vs_LHB_2023 + 41.297*Pitch_Number_vs_RHB_2023 + 0.537172*Batters_Faced_2023 + 110.942*Strikeout_vs_LHB_Percentage_2023 + 130.2*Strikeout_vs_RHB_Percentage_2023 + 84.7407*Walk_vs_LHB_Percentage_2023 + 32.4222*Walk_vs_RHB_Percentage_2023 + 300.528*Delta_Bat_Score_vs_RHB_2023 + 93.2082*Japan + 7.57239*Height - 137.069))

    #Compute final playing time prediction for a given player in 2024
    Playing_Time_Prediction_2024 = Plate_Appearances_Prediction_2024 + Batters_Faced_Prediction_2024

    #Display the result
    print(str(Playing_Time_Prediction_2024))