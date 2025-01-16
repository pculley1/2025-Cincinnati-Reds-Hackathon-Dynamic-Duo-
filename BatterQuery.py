import pandas as pd

#Import the Baseball Savant database
savant_data = pd.read_csv("C:\\Users\\peter\\Downloads\\savant_data_2021_2023.csv")

#Create row count variable i to track progress of the query
i = 1

#Produce requested data for every batter who appeared in 2023
for player_id in savant_data.loc[(savant_data["game_year"] == 2023), "batter"].unique():

    #Row label
    print(str(i), end = " ")

    #Player ID
    print(str(player_id), end=  " ")

    #Raw plate appearance outcome counts vs. LHP and RHP
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "catcher_interf")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "catcher_interf")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "double")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "double")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "field_error")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "field_error")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "field_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "field_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "fielders_choice")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "fielders_choice")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "fielders_choice_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "fielders_choice_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "force_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "force_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "grounded_into_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "grounded_into_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "hit_by_pitch")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "hit_by_pitch")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "home_run")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "home_run")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "other_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "other_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "sac_bunt")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "sac_bunt")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "sac_bunt_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "sac_bunt_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "sac_fly")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "sac_fly")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "sac_fly_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "sac_fly_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "single")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "single")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "strikeout")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "strikeout")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "strikeout_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "strikeout_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "triple")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "triple")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "triple_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "triple_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["events"] == "walk")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["events"] == "walk")]["events"].count()), end=" ")

    #Raw batted ball type counts vs. LHP and RHP
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["bb_type"] == "ground_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["bb_type"] == "ground_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["bb_type"] == "line_drive")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["bb_type"] == "line_drive")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["bb_type"] == "fly_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["bb_type"] == "fly_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["bb_type"] == "popup")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["bb_type"] == "popup")]["bb_type"].count()), end=" ")

    #Raw average Statcast data vs. LHP and RHP
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["hit_distance_sc"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["hit_distance_sc"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["launch_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["launch_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["launch_angle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["launch_angle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["estimated_ba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["estimated_ba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["estimated_woba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["estimated_woba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["woba_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["woba_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["woba_denom"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["woba_denom"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["babip_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["babip_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["iso_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["iso_value"].mean(skipna=True)), end=" ")

    #Raw contact type counts vs. LHP and RHP
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["launch_speed_angle"] == 1)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 1)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["launch_speed_angle"] == 2)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 2)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["launch_speed_angle"] == 3)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 3)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["launch_speed_angle"] == 4)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 4)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["launch_speed_angle"] == 5)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 5)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L") & (savant_data["launch_speed_angle"] == 6)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R") & (savant_data["launch_speed_angle"] == 6)]["launch_speed_angle"].count()), end=" ")

    #Other miscellanous information vs. LHP and RHP
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["pitch_number"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["pitch_number"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["post_bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["post_bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["delta_home_win_exp"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["delta_home_win_exp"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "L")]["delta_run_exp"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["batter"] == player_id) & (savant_data["p_throws"] == "R")]["delta_run_exp"].mean(skipna=True)))
    
    #Iterate to next row
    i += 1