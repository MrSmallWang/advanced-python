import numpy as np
import pandas as pd

txt_path = "sanples.txt"
df = pd.read_csv(txt_path, sep=" ", error_bad_lines=False,
                 names=range(30),
                 )
df.fillna(value=pd.NA)

with open("output_07.txt", mode="w", encoding="utf-8") as f:
    for i, row in df.iterrows():
        if df.iloc[i-1, 3] != "1" and i != df.shape[0] - 1:
            if df.iloc[i, 3] == "1":
                row = row.T
                first_row2write = row.to_string(index=False, )
                f.write(first_row2write + " ")