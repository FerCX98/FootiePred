import pandas as pd
import math
import datetime

def pr(inp):
    if inp=="Balanced":
        inp=0
    elif inp=="Fast":
        inp=1
    elif inp=="Slow":
        inp=2
    elif inp=="Little":
        inp=0
    elif inp=="Normal":
        inp=1
    elif inp=="Lots":
        inp=2
    elif inp=="Mixed":
        inp=0
    elif inp=="Short":
        inp=1
    elif inp=="Long":
        inp=2
    elif inp=="Organised":
        inp=0
    elif inp=="FreeForm":
        inp=1
    elif inp=="Risky":
        inp=0
    elif inp=="Safe":
        inp=2
    elif inp=="Medium":
        inp=0
    elif inp=="Deep":
        inp=1
    elif inp=="High":
        inp=2
    elif inp=="Press":
        inp=0
    elif inp=="Double":
        inp=1
    elif inp=="Contain":
        inp=2
    elif inp=="Wide":
        inp=0
    elif inp=="Narrow":
        inp=2
    elif inp=="Cover":
        inp=0
    elif inp=="OffsideTrap":
        inp=1
    elif not isinstance(inp,str):
        if math.isnan(inp):
            inp="?"
    else:
        pass
        
        
    with open('dt.txt', 'a') as f:
        f.write(str(inp))

matches = pd.read_csv('Match.csv')
teams = pd.read_csv('Team.csv')
team_attributes = pd.read_csv('Team_Attributes.csv')
players = pd.read_csv('Player.csv')
player_attributes = pd.read_csv('Player_Attributes.csv')
players_count = []
teams_count = []
for i in range(1,750586): #create empty list to later overwrite, 750584 is max player_api_id (+2 for some reason to get in range)
    players_count.append([])
for i in range(1,274583): #create empty list to later overwrite, 274581 is max team_api_id (+2 for some reason to get in range)
    teams_count.append([])

for player in player_attributes.iterrows(): #for each player date instance, not for each unique player (here each player will be multiple times)
    player_id=player[1]['player_api_id'] #get player identifier
    players_count[player_id].append(player[1]['id']-1) #append index into correct player list according to player_api_id as id
for team in team_attributes.iterrows(): #for each player date instance, not for each unique player (here each player will be multiple times)
    team_id=team[1]['team_api_id'] #get player identifier
    teams_count[team_id].append(team[1]['id']-1) #append index into correct player list according to player_api_id as id

for match in matches.iterrows(): #go through each match in dataset
    match=match[1]
    print(str(match['id']/len(matches)*100) + '%')
    if match['home_team_goal'] > match['away_team_goal']:
        curr_outcome = 1
    elif match['home_team_goal'] < match['away_team_goal']:
        curr_outcome = 2
    else:
        curr_outcome = 0
    if math.isnan(match['home_team_api_id']) or math.isnan(match['away_team_api_id']):
        pass
    else:
        this_match_players = []
        this_match_teams = []
        date = match['date'] #need match date to match correct player version
        home_id = match['home_team_api_id'] #need team id to get team attributes
        away_id = match['away_team_api_id']
        player_pos_X = []
        player_pos_Y = []
        #player X coordinates for position on map
        player_pos_X.append(match['home_player_X1'])
        player_pos_X.append(match['home_player_X2'])
        player_pos_X.append(match['home_player_X3'])
        player_pos_X.append(match['home_player_X4'])
        player_pos_X.append(match['home_player_X5'])
        player_pos_X.append(match['home_player_X6'])
        player_pos_X.append(match['home_player_X7'])
        player_pos_X.append(match['home_player_X8'])
        player_pos_X.append(match['home_player_X9'])
        player_pos_X.append(match['home_player_X10'])
        player_pos_X.append(match['home_player_X11'])
        player_pos_X.append(match['away_player_X1'])
        player_pos_X.append(match['away_player_X2'])
        player_pos_X.append(match['away_player_X3'])
        player_pos_X.append(match['away_player_X4'])
        player_pos_X.append(match['away_player_X5'])
        player_pos_X.append(match['away_player_X6'])
        player_pos_X.append(match['away_player_X7'])
        player_pos_X.append(match['away_player_X8'])
        player_pos_X.append(match['away_player_X9'])
        player_pos_X.append(match['away_player_X10'])
        player_pos_X.append(match['away_player_X11'])
    
         #player Y coordinates for position on map
        player_pos_Y.append(match['home_player_Y1'])
        player_pos_Y.append(match['home_player_Y2'])
        player_pos_Y.append(match['home_player_Y3'])
        player_pos_Y.append(match['home_player_Y4'])
        player_pos_Y.append(match['home_player_Y5'])
        player_pos_Y.append(match['home_player_Y6'])
        player_pos_Y.append(match['home_player_Y7'])
        player_pos_Y.append(match['home_player_Y8'])
        player_pos_Y.append(match['home_player_Y9'])
        player_pos_Y.append(match['home_player_Y10'])
        player_pos_Y.append(match['home_player_Y11'])
        player_pos_Y.append(match['away_player_Y1'])
        player_pos_Y.append(match['away_player_Y2'])
        player_pos_Y.append(match['away_player_Y3'])
        player_pos_Y.append(match['away_player_Y4'])
        player_pos_Y.append(match['away_player_Y5'])
        player_pos_Y.append(match['away_player_Y6'])
        player_pos_Y.append(match['away_player_Y7'])
        player_pos_Y.append(match['away_player_Y8'])
        player_pos_Y.append(match['away_player_Y9'])
        player_pos_Y.append(match['away_player_Y10'])
        player_pos_Y.append(match['away_player_Y11'])
    
         #getting player identifiers
        home_player_1_id = match['home_player_1']
        home_player_2_id = match['home_player_2']
        home_player_3_id = match['home_player_3']
        home_player_4_id = match['home_player_4']
        home_player_5_id = match['home_player_5']
        home_player_6_id = match['home_player_6']
        home_player_7_id = match['home_player_7']
        home_player_8_id = match['home_player_8']
        home_player_9_id = match['home_player_9']
        home_player_10_id = match['home_player_10']
        home_player_11_id = match['home_player_11']
        away_player_1_id = match['away_player_1']
        away_player_2_id = match['away_player_2']
        away_player_3_id = match['away_player_3']
        away_player_4_id = match['away_player_4']
        away_player_5_id = match['away_player_5']
        away_player_6_id = match['away_player_6']
        away_player_7_id = match['away_player_7']
        away_player_8_id = match['away_player_8']
        away_player_9_id = match['away_player_9']
        away_player_10_id = match['away_player_10']
        away_player_11_id = match['away_player_11']
        this_match_players.append(home_player_1_id)
        this_match_players.append(home_player_2_id)
        this_match_players.append(home_player_3_id)
        this_match_players.append(home_player_4_id)
        this_match_players.append(home_player_5_id)
        this_match_players.append(home_player_6_id)
        this_match_players.append(home_player_7_id)
        this_match_players.append(home_player_8_id)
        this_match_players.append(home_player_9_id)
        this_match_players.append(home_player_10_id)
        this_match_players.append(home_player_11_id)
        this_match_players.append(away_player_1_id)
        this_match_players.append(away_player_2_id)
        this_match_players.append(away_player_3_id)
        this_match_players.append(away_player_4_id)
        this_match_players.append(away_player_5_id)
        this_match_players.append(away_player_6_id)
        this_match_players.append(away_player_7_id)
        this_match_players.append(away_player_8_id)
        this_match_players.append(away_player_9_id)
        this_match_players.append(away_player_10_id)
        this_match_players.append(away_player_11_id)
        this_match_teams.append(home_id)
        this_match_teams.append(away_id)
        curr_match_players_time_id = []
        curr_match_teams_time_id = []
        
        breaker=0
        for player_id in this_match_players: #for every player playing in the current match
            cal=0
            if math.isnan(player_id):
                breaker=1
                break
            for search_player_time in players_count[int(player_id)]: #start loop through different versions of a player
                if datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S').timestamp() < datetime.datetime.strptime(player_attributes.iloc[search_player_time]['date'],'%Y-%m-%d %H:%M:%S').timestamp(): #loop until correct version is found
                    found_player_time = search_player_time  #when timestamp is bigger, dont set, so it stays biggest lower value
                else:
                    pass
                cal=cal+1
                if cal == len(players_count[int(player_id)]) :
                    curr_match_players_time_id.append(found_player_time)
        if breaker==1:
            continue
        
        for team_id in this_match_teams: #for every player playing in the current match
            cal=0
            if math.isnan(team_id):
                breaker=1
                break
            for search_team_time in teams_count[int(team_id)]: #start loop through different versions of a player
                if datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S').timestamp() < datetime.datetime.strptime(team_attributes.iloc[search_team_time]['date'],'%Y-%m-%d %H:%M:%S').timestamp(): #loop until correct version is found
                    found_team_time =  search_team_time #when timestamp is bigger, dont set, so it stays biggest lower value
                else:
                    pass
                cal=cal+1
                if cal == len(teams_count[int(team_id)]) :
                    curr_match_teams_time_id.append(found_team_time)
        if breaker==1:
            continue
        count=0
        for curr_print in  curr_match_players_time_id:
            if count == 0 or count == 11:
                pr('[')
                pr('[')
                pr(player_pos_X[count])
                pr(',')
                pr(player_pos_Y[count])
                pr(',')
                search_player_time = int(curr_match_players_time_id[count])
                pr(player_attributes.iloc[search_player_time]['gk_diving'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['gk_handling'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['gk_kicking'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['gk_positioning'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['gk_reflexes'])
                pr(']')
                pr(',')
                count=count+1
            else:
                pr('[')
                search_player_time = int(curr_match_players_time_id[count])
                pr(player_pos_X[count])
                pr(',')
                pr(player_pos_Y[count])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['crossing'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['finishing'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['overall_rating'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['potential'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['heading_accuracy'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['short_passing'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['volleys'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['dribbling'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['curve'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['free_kick_accuracy'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['long_passing'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['ball_control'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['acceleration'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['sprint_speed'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['agility'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['reactions'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['balance'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['shot_power'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['jumping'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['stamina'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['strength'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['long_shots'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['aggression'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['interceptions'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['positioning'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['vision'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['penalties'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['marking'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['standing_tackle'])
                pr(',')
                pr(player_attributes.iloc[search_player_time]['sliding_tackle'])
                pr(']')
                pr(',')
                count=count+1
            if count == 11:
                pr('[')
                search_team_time = int(curr_match_teams_time_id[0])
                pr(team_attributes.iloc[search_team_time]['buildUpPlaySpeed'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlaySpeedClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayDribbling'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayDribblingClass'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayPassing'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayPassingClass'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayPositioningClass'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationPassing'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationPassingClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationCrossing'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationCrossingClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationShooting'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationShootingClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationPositioningClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defencePressure'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defencePressureClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceAggression'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceAggressionClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceTeamWidth'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceTeamWidthClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceDefenderLineClass'])
                pr(']')
                pr(']')
                pr(',')
            if count == 22:
                pr('[')
                search_team_time = int(curr_match_teams_time_id[1])
                pr(team_attributes.iloc[search_team_time]['buildUpPlaySpeed'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlaySpeedClass'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayDribbling'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayDribblingClass'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayPassing'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayPassingClass'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['buildUpPlayPositioningClass'] )
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationPassing'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationPassingClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationCrossing'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationCrossingClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationShooting'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationShootingClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['chanceCreationPositioningClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defencePressure'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defencePressureClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceAggression'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceAggressionClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceTeamWidth'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceTeamWidthClass'])
                pr(',')
                pr(team_attributes.iloc[search_team_time]['defenceDefenderLineClass'])
                pr(']')
                pr(']')
                pr(',')
            if count== 22:
                pr(curr_outcome)
                pr('\n')