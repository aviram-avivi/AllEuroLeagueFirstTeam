import re
import requests
import numpy as np
from bs4 import BeautifulSoup

def replace(string, char): #geeksforgeeks
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string)
    return string

def get_player_details_for_given_url(url, team_name, year_played):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    open('player.html', 'wb').write(r.content)
    element = soup.find("div", {"class": "name"})

    if element:
        player_name = element.text
        print(player_name)
        element = soup.find("div", {"class": "summary-second"})
        player_details = element.text.strip().split()
    if player_details[0] == 'Born:':

        player_birth_year = int(player_details[3])
        player_nationality = element.contents[3].contents[0].split(":")[1]
        element = soup.find("div", {"class": "summary-first"})
        player_position = replace(element.text, "\n").split("\n")[3]
        element = soup.find("div",{"class": "PlayerAccumulatedAveragesStatisticsMainContainer table-responsive-container"})
        if element is not None:
            string = element.text
            char = '\n'
            output = replace(string, char).replace(u'\xa0', u' ').strip().split("\n")
            player_stats_average = np.array(output[22:]).reshape(2, -1)[1, 1:]  # reshape for only average row
        else:
            player_stats_average = np.array([0]*(26 - 8))
        player_profile = np.array(
            [player_name, player_nationality, player_birth_year, np.nan, player_position, team_name, year_played, 0])
        player_profile = np.concatenate((player_profile, player_stats_average), axis=None)

    else:
        element = soup.find("div", {"class": "summary-first"})
        if element and len(element.text.split("\n")) > 3 :
            player_position = replace(element.text, "\n").split("\n")[3]
        else:
            player_position = np.nan
        element = soup.find("div", {"class": "summary-second"})
        if element:
            player_details = element.text.strip().split("\n")
            player_height = float(player_details[0].split(":")[1].strip())
            player_birth_year = int(player_details[1].split(":")[1].strip().split(",")[1].strip())
            player_nationality = player_details[2].split(":")[1].strip()

        element = soup.find("div", {"class": "PlayerAccumulatedAveragesStatisticsMainContainer table-responsive-container"})

        if element is not None:
            string = element.text
            char = '\n'
            output = replace(string, char).replace(u'\xa0', u' ').strip().split("\n")
            player_stats_average = np.array(output[22:]).reshape(2, -1)[1, 1:] # reshape for only average row
        else:
            player_stats_average = np.array([0]*(26 - 8))
        player_profile = np.array([player_name, player_nationality, player_birth_year, player_height, player_position,
                                   team_name ,year_played, 0])
        player_profile = np.concatenate((player_profile, player_stats_average), axis=None)

    return player_profile
