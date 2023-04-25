import requests
import csv
import json

base_url = 'https://statsapi.web.nhl.com/api/v1/'
type = 'people/'
player_id = '8471214/'
modifier = 'stats?stats=homeAndAway&season='

# https://statsapi.web.nhl.com/api/v1/people/8471214/stats?stats=homeAndAway&season=20162017
# https://statsapi.web.nhl.com/api/v1/people/8471214/stats?stats=homeAndAway&season=20162017

seasons = ["20052006", "20062007", "20072008", "20082009", "20092010", "20102011", "20112012", "20122013", "20132014", 
"20142015", "20152016", "20162017", "20172018", "20182019", "20192020", "20202021", "20212022", "20222023"]

stats = []

for season in seasons :
    url = base_url + type + player_id + modifier + season
    print(url)

    response = requests.get(url)
    jsonResponse = response.json()

    home_stats = jsonResponse['stats'][0]['splits'][0]
    away_stats = jsonResponse['stats'][0]['splits'][1]

    season = home_stats['season']
    
    home_stats = home_stats['stat']
    away_stats = away_stats['stat']

    home_shifts = home_stats['shifts']
    home_toi = home_stats['timeOnIce']
    home_toi_pg = home_stats['timeOnIcePerGame']
    home_games = home_stats['games']
    home_goals = home_stats['goals']
    home_assists = home_stats['assists']
    home_points = home_stats['points']
    home_shots = home_stats['shots']
    home_blocked = home_stats['blocked']
    home_even_toi = home_stats['evenTimeOnIce']
    home_even_toi_pg = home_stats['evenTimeOnIcePerGame']
    home_gwg = home_stats['gameWinningGoals']
    home_hits = home_stats['hits']
    home_otg = home_stats['overTimeGoals']
    home_pims = home_stats['pim']
    home_pm = home_stats['plusMinus']
    home_ppg = home_stats['powerPlayGoals']
    home_ppp = home_stats['powerPlayPoints']
    home_pp_toi = home_stats['powerPlayTimeOnIce']
    home_pp_toi_pg = home_stats['powerPlayTimeOnIcePerGame']
    home_shg = home_stats['shortHandedGoals']
    home_shp = home_stats['shortHandedPoints']
    home_sh_toi = home_stats['shortHandedTimeOnIce']
    home_sh_toi_pg = home_stats['shortHandedTimeOnIcePerGame']

    away_shifts = away_stats['shifts']
    away_toi = away_stats['timeOnIce']
    away_toi_pg = away_stats['timeOnIcePerGame']
    away_games = away_stats['games']
    away_goals = away_stats['goals']
    away_assists = away_stats['assists']
    away_points = away_stats['points']
    away_shots = away_stats['shots']
    away_blocked = away_stats['blocked']
    away_even_toi = away_stats['evenTimeOnIce']
    away_even_toi_pg = away_stats['evenTimeOnIcePerGame']
    away_gwg = away_stats['gameWinningGoals']
    away_hits = away_stats['hits']
    away_otg = away_stats['overTimeGoals']
    away_pims = away_stats['pim']
    away_pm = away_stats['plusMinus']
    away_ppg = away_stats['powerPlayGoals']
    away_ppp = away_stats['powerPlayPoints']
    away_pp_toi = away_stats['powerPlayTimeOnIce']
    away_pp_toi_pg = away_stats['powerPlayTimeOnIcePerGame']
    away_shg = away_stats['shortHandedGoals']
    away_shp = away_stats['shortHandedPoints']
    away_sh_toi = away_stats['shortHandedTimeOnIce']
    away_sh_toi_pg = away_stats['shortHandedTimeOnIcePerGame']

    row = [ season, home_shifts, away_shifts, home_toi, away_toi, home_toi_pg, away_toi_pg, home_games, away_games,
        home_goals, away_goals, home_assists, away_assists, home_points, away_points, home_shots, away_shots, home_blocked,
        away_blocked, home_even_toi, away_even_toi, home_even_toi_pg, away_even_toi_pg, home_gwg, away_gwg, home_hits,
        away_hits, home_otg, away_otg, home_pims, away_pims, home_pm, away_pm, home_ppg, away_ppg, home_ppp, away_ppp,
        home_pp_toi, away_pp_toi, home_pp_toi_pg, away_pp_toi_pg, home_shg, away_shg, home_shp, away_shp, home_sh_toi,
        away_sh_toi, home_sh_toi_pg, away_sh_toi_pg
    ]

    # add to stats array
    stats.append(row)


#Write to csv
with open('home_away.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(["Season", "Home Shifts", "Away Shifts", "Home TOI", "Away TOI", "Home TOI/Game", "Away TOI/Game", 
        "Home Gamaes", "Away Games", "Home Goals", "Away Goals", "Home Assists", "Away Assists", "Home Points", "Away Points", 
        "Home Shots", "Away Shots", "Home Blocked Shots", "Away Blocked Shots", "Home ES TOI", "Away ES TOI", 
        "Home ES TOI/Game", "Away ES TOI/Game", "Home GWG", "Away GWG", "Home Hits", "Away Hits", "Home OT Goals", 
        "Away OT Goals", "Home PIMs", "Away PIMs", "Home +/-", "Away +/-", "Home PPG", "Away PPG", "Home PPP", "Away PPP", 
        "Home PP TOI", "Away PP TOI", "Home PP TOI/Game", "Away PP TOI/Game", "Home SHG", "Away SHG", "Home SHP", "Away SHP", 
        "Home SH TOI", "Away SH TOI", "Home SH TOI/Game", "Away SH TOI/Game"])
    for row in stats :
        writer.writerow(row)