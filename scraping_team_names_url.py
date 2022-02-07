print("Parsing teams url")
import pandas as pd
import requests
from bs4 import BeautifulSoup
from scraping_group_team_members import get_team_details_for_given_url

def getting_teams_data(url, page_number):

    columns_header_df = ["Player_name", "nationality", "birth_year", "height", "position", "team_name", "year_played", "won", "games", "GS",
                         "minutes",
                         "points", "2FG", "3FG", "FT", "R.offensive", "R.deffensive", "R.total", "Assists", "Steal",
                         "turn_over", "Fv", "Ag", "Cm", "Rv", "PIR"]
    total_teams_df = pd.DataFrame(columns=columns_header_df)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    open('teams.html', 'wb').write(r.content)
    elements = soup.find_all("div", {"class": "RoasterName"})
    if elements:
        for element in elements:
            team_name = element.text.strip()
            team_url = element.contents[1]["href"]
            year_played = int(team_url[-4:])
            full_team_url = "https://www.euroleague.net" + team_url
            team_df = get_team_details_for_given_url(full_team_url, team_name, columns_header_df)
            total_teams_df = pd.concat([total_teams_df, team_df])

    total_teams_df.reset_index(inplace=True)
    total_teams_df.drop('index', axis=1, inplace=True)
    total_teams_df["Player_name"].str.lower()
    total_teams_df.to_csv(f"csvs/collection_of_teams{page_number}.csv")
