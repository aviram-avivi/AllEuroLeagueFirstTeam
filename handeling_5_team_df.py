import pandas as pd
path = "/Users/aviramavivi/PycharmProjects/proj1/first5team_All .csv"
df = pd.read_csv(path, index_col=[0])
for i in range(34, 39):
    df.drop(i, axis=0, inplace=True)

for i in range(0, 5):
    df.drop(i, axis=0, inplace=True)

print("aa")
df.replace("Barca", 'FC Barcelona Regal', inplace=True)
df.replace("Olympiacos", 'Olympiacos Piraeus', inplace=True)
df.replace("Zalgiris", 'Zalgiris Kaunas', inplace=True)
df.replace("Panathinaikos", 'Panathinaikos Athens', inplace=True)
df.replace("KK Crvena Zvezda", 'Crvena Zvezda Telekom Belgrade', inplace=True)
df.replace("Lokomotiv Kuban", 'Lokomotiv Kuban Krasnodar', inplace=True)
df.replace("Maccabi FOX Tel Aviv", 'Maccabi Electra Tel Aviv', inplace=True)
df.loc[3, "team_name"] = "Fenerbahce Beko Istanbul"  # 2019
df.loc[4, "team_name"] = "Fenerbahce Beko Istanbul"
df.loc[8, "team_name"] = "KIROLBET Baskonia Vitoria Gasteiz"
df.loc[15, "team_name"] = "Laboral Kutxa Vitoria Gasteiz"
df.loc[18, "team_name"] = "Fenerbahce Istanbul"  # 2016
df.loc[20, "team_name"] = "Fenerbahce Ulker Istanbul"  # 2015
df.loc[25, "team_name"] = "FC Barcelona"  # 2014
df = df.sort_values(by=['season'], ascending=False)
df = df.reset_index(drop=True)
print(df)
