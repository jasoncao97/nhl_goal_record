import requests
import csv
import json

#def buildurl(url, ):

# array to store year by year stats
stats = []

# URL construction --> https://statsapi.web.nhl.com/api/v1/people/8471214/stats?stats=yearByYear
base_url = 'https://statsapi.web.nhl.com/api/v1/'
type = 'people/'
player_id = '8471214/'
modifier = 'stats?stats=yearByYear'

url = base_url + type + player_id + modifier
print(url)

# Send GET request to url
response = requests.get(base_url + type + player_id + modifier)
jsonResponse = response.json()
yearByYear = jsonResponse['stats'][0]['splits']

for year in yearByYear :

    if year['league']['name'] == "National Hockey League" :
        season_data = year['stat']
        season_year = year['season']

        games = season_data['games']
        toi = season_data['timeOnIce']
        shifts = season_data['shifts']
        goals = season_data['goals']
        assists = season_data['assists']
        points = season_data['points']
        shots = season_data['shots']
        hits = season_data['hits']
        pims = season_data['pim']
        ppg = season_data['powerPlayGoals']
        ppp = season_data['powerPlayPoints']
        pptoi = season_data['powerPlayTimeOnIce']
        eventoi = season_data['evenTimeOnIce']
        fopct = season_data['faceOffPct']
        shotpct = season_data['shotPct']
        gwg = season_data['gameWinningGoals']
        otg = season_data['overTimeGoals']
        shg = season_data['shortHandedGoals']
        shp = season_data['shortHandedPoints']
        shtoi = season_data['shortHandedTimeOnIce']
        blocked = season_data['blocked']
        plusminus = season_data['plusMinus']


        row = [ season_year, games, toi, shifts, goals, assists, points,
        shots, hits, pims, ppg, ppp, pptoi, eventoi, fopct, shotpct, gwg, otg, shg, 
        shp, shtoi, blocked, plusminus
        ]

        # add to stats array
        stats.append(row)

# Write to csv

with open('season_data.csv', 'w+') as f:
    writer = csv.writer(f)
    writer.writerow(["Season", "Games", "TimeOnIce", "Shifts", "Goals", "Assists", "Points", "Shots", 
    "Hits", "PIMS", "PPG", "PPP", "PP TOI", "Even TOI", "Faceoff %", 
    "Shooting %", "GWG", "OTG", "SHG", "SHP", "SH TOI", "Blocked", "+/-"])
    for row in stats :
        writer.writerow(row)