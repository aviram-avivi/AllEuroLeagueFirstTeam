import pandas as pd

df1 = pd.read_csv("/Users/aviramavivi/PycharmProjects/proj1/df_total.csv", index_col=[0])
df2 = pd.read_csv("/Users/aviramavivi/PycharmProjects/proj1/Top_First_5.csv", index_col=[0])
df2.reset_index(inplace=True, drop=True)

i = 0
count = 0

for row_df2 in df2.index:
    for row_df1 in df1.loc[df1['year_played'] == 2019 - i].index:
        if df1["Player_name"][row_df1].lower() == df2['player_name'][row_df2].lower():
            df1["won"][row_df1] = 1
            count += 1
            if count == 5:
                i += 1
                count = 0
                break
            break
for index, column in enumerate(df1["2FG"]):
    df1["2FG"][index] = float(column[:-1])

for index, column in enumerate(df1["3FG"]):
    df1["3FG"][index] = float(column[:-1])
for index, column in enumerate(df1["FT"]):
    df1["FT"][index] = float(column[:-1])
df1["2FG"] = df1["2FG"].astype(float)
df1["3FG"] = df1["3FG"].astype(float)
df1["FT"] = df1["FT"].astype(float)
df1.to_csv( "fixed_DF.csv", index=True)
