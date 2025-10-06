import pandas as pd
from ds_helper import typeofcolumn, visualize, TextCleaner
df=pd.read_csv(r"C:\Users\DELL\Downloads\Titanic-Dataset.csv")
#Check column types
print("Column Types:\n",typeofcolumn(df))
#visualize the data
print("Visualizing Data")
visualize(df)
#text cleaning on the 'Name' column if it exists
if 'Name' in df.columns:
    cleaner=TextCleaner()
    sample_name=df['Name'].iloc[0]
    print("\nOrginal Name:", sample_name)
    print("Cleaned Name:", cleaner.clean(str(sample_name)))