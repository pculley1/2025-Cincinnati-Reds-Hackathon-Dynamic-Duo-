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

    #--------BATTING SETUP--------
    
    #Compute initial 2022 plate appearance information for future use in case original model produces an PA estimate of 0
    Plate_Appearances_vs_LHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_vs_RHP_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_2022 = Plate_Appearances_vs_LHP_2022 + Plate_Appearances_vs_RHP_2022
    
    #Compute initial 2023 plate appearance information to protect against future divide-by-zero errors
    Plate_Appearances_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Plate_Appearances_2023 = Plate_Appearances_vs_LHP_2023 + Plate_Appearances_vs_RHP_2023
    
    #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
    if Plate_Appearances_vs_LHP_2023 == 0:
        Launch_Speed_vs_LHP_2023 = 0
        Strikeout_vs_LHP_Percentage_2023 = 0
    else:
        Launch_Speed_vs_LHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["launch_speed"].mean(skipna=True)
        Strikeout_vs_LHP_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "strikeout")]["events"].count() / Plate_Appearances_vs_LHP_2023
        
    #If the following stat cannot be computed without a divide-by-zero error, we assign it a value of 0, else we proceed to compute it
    if Plate_Appearances_vs_RHP_2023 == 0:
        ISO_Value_vs_RHP_2023 = 0
    else:
        ISO_Value_vs_RHP_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["iso_value"].mean(skipna=True)

    #Use optimized linear regression model with the max function incorporated to make a prediction for the total number of plate appearance a player will get in 2024; the max function ensures the result is nonnegative
    Plate_Appearances_Prediction_2024 = round(max(0, 4.74160273563879*Launch_Speed_vs_LHP_2023 + 503.605901065577*ISO_Value_vs_RHP_2023 + 0.702441539902257*Plate_Appearances_2023 - 177.624677063973*Strikeout_vs_LHP_Percentage_2023 - 352.294210110046))

    #--------PITCHING SETUP--------
    
    #Compute initial 2022 batters faced information to protect against future divide-by-zero errors
    LH_Batters_Faced_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    RH_Batters_Faced_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Batters_Faced_2022 = LH_Batters_Faced_2022 + RH_Batters_Faced_2022

    #If the following stat cannot be computed without a divide-by-zero error, we assign it a value of 0, else we proceed to compute it
    if LH_Batters_Faced_2022 == 0:
        Release_Speed_vs_LHB_2022 = 0
    else:
        #While release speed is not in the final model, we use it as a means to catch instances of position players pitching and prevent the model from treating a position player like a regular pitcher (i.e., assigning a large number of BF to that player for 2024) 
        Release_Speed_vs_LHB_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_speed"].mean(skipna=True)
    
    #If the following stat cannot be computed without a divide-by-zero error, we assign it a value of 0, else we proceed to compute it
    if RH_Batters_Faced_2022 == 0:
        Release_Speed_vs_RHB_2022 = 0
    else:
        Release_Speed_vs_RHB_2022 = savant_data.loc[(savant_data["game_year"] == 2022) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_speed"].mean(skipna=True)
    
    #Same setup used here as for 2022 pitching data
    #Compute initial 2023 batters faced information to protect against future divide-by-zero errors
    LH_Batters_Faced_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    RH_Batters_Faced_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & ((savant_data["events"] == "catcher_interf") | (savant_data["events"] == "double") | (savant_data["events"] == "double_play") | (savant_data["events"] == "field_error") | (savant_data["events"] == "field_out") | (savant_data["events"] == "fielders_choice") | (savant_data["events"] == "fielders_choice_out") | (savant_data["events"] == "force_out") | (savant_data["events"] == "grounded_into_double_play") | (savant_data["events"] == "hit_by_pitch") | (savant_data["events"] == "home_run") | (savant_data["events"] == "other_out") | (savant_data["events"] == "sac_bunt") | (savant_data["events"] == "sac_bunt_double_play") | (savant_data["events"] == "sac_fly") | (savant_data["events"] == "sac_fly_double_play") | (savant_data["events"] == "single") | (savant_data["events"] == "strikeout") | (savant_data["events"] == "strikeout_double_play") | (savant_data["events"] == "triple") | (savant_data["events"] == "triple_play") | (savant_data["events"] == "walk"))]["events"].count()
    Batters_Faced_2023 = LH_Batters_Faced_2023 + RH_Batters_Faced_2023

    #If the following stat cannot be computed without a divide-by-zero error, we assign it a value of 0, else we proceed to compute it
    if LH_Batters_Faced_2023 == 0:
        Release_Speed_vs_LHB_2023 = 0
    else:
        Release_Speed_vs_LHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_speed"].mean(skipna=True)

    #If the following stats cannot be computed without a divide-by-zero error, we assign them all a value of 0, else we proceed to compute them
    if RH_Batters_Faced_2023 == 0:
        wOBA_Value_vs_RHB_2023 = 0
        Strikeout_vs_RHB_Percentage_2023 = 0
        Release_Speed_vs_RHB_2023 = 0
    else:
        Release_Speed_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_speed"].mean(skipna=True)
        
        #From studying special case data where the model originally projected a player to be a two-way player, we found that setting a minimum average release speed of 81 mph would seperate real pitchers from position players trying to pitch in a blowout
        if Release_Speed_vs_RHB_2023 < 81:
            wOBA_Value_vs_RHB_2023 = 0
            Strikeout_vs_RHB_Percentage_2023 = 0
        else:
            wOBA_Value_vs_RHB_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["woba_value"].mean(skipna=True)
            Strikeout_vs_RHB_Percentage_2023 = savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "strikeout")]["events"].count() / RH_Batters_Faced_2023
            
    #If a player threw 81+ mph against both types of hitters in a single year, we assume that player to be a real pitcher, else we excerise the following statement to prevent position players from being assigned large 2024 BF just solely based on their height
    if ((Release_Speed_vs_LHB_2022 < 81) | (Release_Speed_vs_RHB_2022 < 81)) & ((Release_Speed_vs_LHB_2023 < 81) | (Release_Speed_vs_RHB_2023 < 81)):
        Height = 0
    else:          
        #Taller pitchers in general have a playing time advantage over shorter pitchers according to the model
        Height = lahman_data.loc[(lahman_data["player_mlb_id"] == player_id)]["height"].mean(skipna=True)

    #Use optimized linear regression model with the max function incorporated to make a prediction for the total number of batters faced a player will get in 2024; the max function ensures the result is nonnegative
    Batters_Faced_Prediction_2024 = round(max(0, 0.162877902211647*Batters_Faced_2022 - 201.651123897185*wOBA_Value_vs_RHB_2023 + 0.545683044615035*Batters_Faced_2023 + 235.399443333355*Strikeout_vs_RHB_Percentage_2023 + 8.85005552532604*Height - 614.048697451178))

    #--------MODEL CORRECTIONS--------
    
    #Handle special cases where the original linear regression model for hitting projects 0 PA for 2024 and assign the prediction the unweighted average of PA's for 2022 and 2023
    if Plate_Appearances_Prediction_2024 == 0:
        Plate_Appearances_Prediction_2024 = round((Plate_Appearances_2022 + Plate_Appearances_2023)/2)

    #Handle special cases where the original linear regression model for hitting projects 0 BF for 2024 and assign the prediction the unweighted average of BF's for 2022 and 2023
    if Batters_Faced_Prediction_2024 == 0:
        Batters_Faced_Prediction_2024 = round((Batters_Faced_2022 + Batters_Faced_2023)/2)

    #--------FINAL MODEL--------
    
    #Compute final playing time prediction for a given player in 2024
    Playing_Time_Prediction_2024 = Plate_Appearances_Prediction_2024 + Batters_Faced_Prediction_2024

    #Display the result
    print(str(Playing_Time_Prediction_2024))
