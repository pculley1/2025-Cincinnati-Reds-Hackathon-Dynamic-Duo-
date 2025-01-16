import pandas as pd

#Import the Baseball Savant database
savant_data = pd.read_csv("C:\\Users\\peter\\Downloads\\savant_data_2021_2023.csv")

#Create row count variable i to track progress of the query
i = 1

#Produce requested data for every batter who appeared in 2023
for player_id in savant_data.loc[(savant_data["game_year"] == 2023), "pitcher"].unique():

    #Row label
    print(str(i), end = " ")

    #Player ID
    print(str(player_id), end=" ")

    #Raw pitcher characteristic data vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_pos_x"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_pos_x"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_pos_z"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_pos_z"].mean(skipna=True)), end=" ")

    #Raw plate appearance outcome counts vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "catcher_interf")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "catcher_interf")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "double")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "double")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "field_error")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "field_error")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "field_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "field_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "fielders_choice")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "fielders_choice")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "fielders_choice_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "fielders_choice_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "force_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "force_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "grounded_into_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "grounded_into_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "hit_by_pitch")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "hit_by_pitch")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "home_run")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "home_run")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "other_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "other_out")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "sac_bunt")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "sac_bunt")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "sac_bunt_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "sac_bunt_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "sac_fly")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "sac_fly")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "sac_fly_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "sac_fly_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "single")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "single")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "strikeout")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "strikeout")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "strikeout_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "strikeout_double_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "triple")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "triple")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "triple_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "triple_play")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["events"] == "walk")]["events"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["events"] == "walk")]["events"].count()), end=" ")

    #Raw batted ball type counts vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["bb_type"] == "ground_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["bb_type"] == "ground_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["bb_type"] == "line_drive")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["bb_type"] == "line_drive")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["bb_type"] == "fly_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["bb_type"] == "fly_ball")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["bb_type"] == "popup")]["bb_type"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["bb_type"] == "popup")]["bb_type"].count()), end=" ")

    #Additional raw pitcher characteristic data (as perceived by the hitter or catcher) vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["pfx_x"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["pfx_x"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["pfx_z"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["pfx_z"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["plate_x"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["plate_x"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["plate_z"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["plate_z"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["vx0"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["vx0"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["vy0"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["vy0"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["vz0"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["vz0"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["ax"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["ax"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["ay"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["ay"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["az"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["az"].mean(skipna=True)), end=" ")

    #Raw average Statcast data vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["hit_distance_sc"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["hit_distance_sc"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["launch_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["launch_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["launch_angle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["launch_angle"].mean(skipna=True)), end=" ")

    #Additional raw pitcher characteristic data vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["effective_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["effective_speed"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_spin_rate"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_spin_rate"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_extension"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_extension"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["release_pos_y"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["release_pos_y"].mean(skipna=True)), end=" ")

    #Additional raw average Statcast data vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["estimated_ba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["estimated_ba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["estimated_woba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["estimated_woba_using_speedangle"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["woba_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["woba_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["woba_denom"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["woba_denom"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["babip_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["babip_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["iso_value"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["iso_value"].mean(skipna=True)), end=" ")

    #Raw contact type counts vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["launch_speed_angle"] == 1)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["launch_speed_angle"] == 1)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["launch_speed_angle"] == 2)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["launch_speed_angle"] == 2)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["launch_speed_angle"] == 3)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["launch_speed_angle"] == 3)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["launch_speed_angle"] == 4)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["launch_speed_angle"] == 4)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["launch_speed_angle"] == 5)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["launch_speed_angle"] == 5)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L") & (savant_data["launch_speed_angle"] == 6)]["launch_speed_angle"].count()), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R") & (savant_data["launch_speed_angle"] == 6)]["launch_speed_angle"].count()), end=" ")

    #Other miscellanous information vs. LHB and RHB
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["pitch_number"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["pitch_number"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["post_bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["post_bat_score"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["spin_axis"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["spin_axis"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["delta_home_win_exp"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["delta_home_win_exp"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "L")]["delta_run_exp"].mean(skipna=True)), end=" ")
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["stand"] == "R")]["delta_run_exp"].mean(skipna=True)), end=" ")
    
    #Average number of pitches thrown per game played
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id)]["pitch_number_appearance"].count() / savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["pitch_number_appearance"] == 1)]["pitch_number_appearance"].count()), end=" ")
    
    #Average number of batters faced per game played
    print(str(savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["pitch_number"] == 1)]["pitch_number"].count() / savant_data.loc[(savant_data["game_year"] == 2023) & (savant_data["pitcher"] == player_id) & (savant_data["pitch_number_appearance"] == 1)]["pitch_number_appearance"].count()))
    
    #Iterate to next row
    i += 1