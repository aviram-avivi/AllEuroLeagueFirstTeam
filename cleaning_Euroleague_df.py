import numpy as np
import pandas as pd

def remove_corrupt_rows(df, num_max_missing_cols):
    limit = (df.shape[1]) - (num_max_missing_cols)
    df.dropna(axis=0, thresh=limit, inplace = True)
    df = df.reset_index(drop=True)
    return df

def fix_min(df_col):
    for i, index in enumerate(df_col):
        df_col[i] = index[:-3]
    return df

if __name__ == '__main__':
    path = "/Users/aviramavivi/PycharmProjects/proj1/combined_csv.csv"
    df = pd.read_csv(path, index_col=[0])
    df.replace(0, np.nan, inplace=True)
    df = remove_corrupt_rows(df, 4)
    df.rename(columns={'R.deffensive': 'R.defensive', 'Steal' : "Steals"}, inplace=True)
    df.replace(np.nan, 0, inplace=True)
    df.sort_values(by=['year_played'],inplace=True,ascending=False)
    df = df.reset_index(drop=True)

    df["games"] = df["games"].astype(int)
    df["GS"] = df["GS"].astype(int)
    df = fix_min(df["minutes"])

    df['height'] = df['height'].apply(lambda x: "{:.2f}".format(x))
    df['points'] = df['points'].apply(lambda x: "{:.2f}".format(x))
    df['R.offensive'] = df['R.offensive'].apply(lambda x: "{:.2f}".format(x))
    df['R.defensive'] = df['R.defensive'].apply(lambda x: "{:.2f}".format(x))
    df['R.total'] = df['R.total'].apply(lambda x: "{:.2f}".format(x))
    df['Assists'] = df['Assists'].apply(lambda x: "{:.2f}".format(x))
    df['Steals'] = df['Steals'].apply(lambda x: "{:.2f}".format(x))
    df['turn_over'] = df['turn_over'].apply(lambda x: "{:.2f}".format(x))
    df['Fv'] = df['Fv'].apply(lambda x: "{:.2f}".format(x))
    df['Ag'] = df['Ag'].apply(lambda x: "{:.2f}".format(x))
    df['Cm'] = df['Cm'].apply(lambda x: "{:.2f}".format(x))
    df['Rv'] = df['Rv'].apply(lambda x: "{:.2f}".format(x))
    df['PIR'] = df['PIR'].apply(lambda x: "{:.2f}".format(x))
    df.to_csv( "df_total.csv", index=True)

    print(df)