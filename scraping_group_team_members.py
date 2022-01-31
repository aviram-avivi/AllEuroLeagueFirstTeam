import requests
import pandas as pd
from bs4 import BeautifulSoup
from scraping_player_profile import get_player_details_for_given_url

def get_team_details_for_given_url(url, team_name, columns_header):
    df = pd.DataFrame(columns=columns_header)

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    open('team_members.html', 'wb').write(r.content)
    elements = soup.find_all("div", {"class": "name"})
    list_of_url_players = []
    for element in elements:
        if element:
            relative_url = element.find_all("a", href=True)[0]["href"]
            full_url = "https://www.euroleague.net/" + relative_url
            list_of_url_players.append(full_url)
    year_played = str(int(relative_url[-4:]) + 1)
    for row_idx, player_url in enumerate(list_of_url_players[:-1]):
        print(player_url)

        output = get_player_details_for_given_url(player_url,team_name, year_played)
        df.loc[len(df)] = output

    return df