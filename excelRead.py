import pandas as pd

#the sheet with the homework
sheet_id = '1XT36KHawZKJJ3r-W3GHJkOflrQksZ_aUrsxOH8-bwbY'

#dataframe
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")


#smaller dataframes for each day
dfLuni = df.iloc[0:10, 0:2]
dfMarti = df.iloc[0:10, 3:5]
dfMiercuri = df.iloc[0:10, 6:8]
dfJoi = df.iloc[0:10, 9:11]
dfVineri = df.iloc[0:10, 12:14]