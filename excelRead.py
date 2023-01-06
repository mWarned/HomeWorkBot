from datetime import time
import numpy as np
import pandas as pd

# the sheet with the homework
sheet_id = '1XT36KHawZKJJ3r-W3GHJkOflrQksZ_aUrsxOH8-bwbY'

# primary dataframe
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")


# dataframe of each day
dfLuni = df.iloc[:, 0:2]
dfMarti = df.iloc[:, 3:5]
dfMiercuri = df.iloc[:, 6:8]
dfJoi = df.iloc[:, 9:11]
dfVineri = df.iloc[:, 12:14]

# lists of subjects and homework for each day
hwLuni = dfLuni[dfLuni["Luni"].notna()][:].replace(np.nan, "Nu sunt teme").values.tolist()
hwMarti = dfMarti[dfMarti["Marți"].notna()][:].replace(np.nan, "Nu sunt teme").values.tolist()
hwMiercuri = dfMiercuri[dfMiercuri["Miercuri"].notna()][:].replace(np.nan, "Nu sunt teme").values.tolist()
hwJoi = dfJoi[dfJoi["Joi"].notna()][:].replace(np.nan, "Nu sunt teme").values.tolist()
hwVineri = dfVineri[dfVineri["Vineri"].notna()][:].replace(np.nan, "Nu sunt teme").values.tolist()

while True:
    df.update(pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"))
    time.sleep(300)
