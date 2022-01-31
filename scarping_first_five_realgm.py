import pandas as pd
import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':

    columns_header_df = ["Player_name", "season", "team_name"]
    total_teams_df = pd.DataFrame(columns=columns_header_df)
    url = "https://basketball.realgm.com/international/league/1/Euroleague/awards/by_type/All-Euroleague-First-Team/4"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    seasons = []
    players = []
    teams = []
    table = soup.find("table", {"class": 'tablesaw'})
    tr_class = table.find_all('tr')
    for tr in range(1, len(tr_class)):
        seasons.append(int(tr_class[tr].contents[1].attrs['rel']))
        players.append(tr_class[tr].contents[3].attrs['rel'])
        teams.append(tr_class[tr].contents[5].attrs['rel'])

    first_five = pd.DataFrame(
        {'season': seasons,
         'player_name': players,
         'team_name': teams
         })

    first_five.rename(columns={'Seasons': 'year_played','Player': 'player_name','Club': 'team_name'},inplace=True)

    first_five.to_csv("csvs/first5team5.csv")

