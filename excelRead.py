import pandas as pd

# the sheet with the homework
sheet_id = '1XT36KHawZKJJ3r-W3GHJkOflrQksZ_aUrsxOH8-bwbY'

# dataframe
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")


# lists of subjects and homework for each day
hwLuni = df.iloc[0:10, 0:2].values.tolist()
hwMarti = df.iloc[0:10, 3:5].values.tolist()
hwMiercuri = df.iloc[0:10, 6:8].values.tolist()
hwJoi = df.iloc[0:10, 9:11].values.tolist()
hwVineri = df.iloc[0:10, 12:14].values.tolist()
