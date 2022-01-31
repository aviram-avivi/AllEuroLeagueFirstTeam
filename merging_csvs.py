import os
import pandas as pd

for i in [x for x in range(11) if x != 2]:

    print(i)

# Path
root = "/Users/aviramavivi/PycharmProjects/proj1/final_csvs"

# Join various path components
filenames = []
path = os.path.join(root, root) #stackoverflow
for path, subdirs, files in os.walk(root):
    for name in files:
        filenames.append(os.path.join(path, name))
for i in filenames:
    print(i)

combined_csv = pd.concat( [ pd.read_csv(f) for f in filenames if f != 0 ] )
combined_csv.reset_index(inplace=True)
combined_csv.drop('index', axis=1, inplace=True)
combined_csv.drop("Unnamed: 0", axis=1, inplace=True)
combined_csv.to_csv( "combined_csv.csv", index=True)