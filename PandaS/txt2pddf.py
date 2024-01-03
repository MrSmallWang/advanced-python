import pandas as pd
import numpy as np


txt = "sanples.txt"

df = pd.read_csv(txt, sep=" ", error_bad_lines=False, names=range(30))
df.fillna(value=pd.NA)

df_row = df.iloc[1]

print(df[:3])
print(df.columns)
print(df.index)
print(df_row, "\n", df_row[29], type(df_row[29]))
print(df.shape[0])